# Brain-computer interface HID reference for connecting to Apple platforms

**Framework**: Accessibility

An overview of the human interface device (HID) descriptor for interfacing between brain-computer interface (BCI) hardware devices and Apple devices.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- visionOS 26.0+

#### Overview

This document provides a reference for manufacturers of third-party brain-computer interface hardware devices who want to build in firmware support for interfacing with Apple devices, such as an iPhone.

A *brain-computer interface (BCI)* establishes a signal link between the brain’s electrical activity and an external hardware component. A *BCI hardware device* is a proprietary controller component for hardware that maintains a direct connection to an implanted or external brain wave sensor array or other similar technology.

The BCI hardware device interfaces with a *host computing device*, such as an iPhone, functioning as an input type for system control and interaction with on-device assistive technology features like Switch Control and AssistiveTouch. This technology supports user control of the host computing device and its apps through neural activity corresponding to specific mental states or tasks.

#### Hid Descriptor Background

To be universally compatible, a BCI hardware device needs to translate its complex signals into the *human interface device (HID)* protocol. By identifying as a human interface device through a *HID descriptor*, the BCI hardware device can be recognized by a host computing device, allowing it to work seamlessly without requiring specialized drivers.

- The primary benefit of this approach is that assistive technology features, like switch software for those with limited mobility (including quadriplegia and ALS), can recognize the device as a dedicated accessibility control interface. The HID descriptor this document outlines allows the host computing device (such as an iPhone) to interpret signals more intelligently — not just as generic input, but as specific commands to call accessibility functions or represent BCI-specific data visually in the UI.
- The descriptor acts as a versatile tool, capable of sending button presses, keyboard events, pointer movements, and an extensible collection of custom neural activity data.
- The descriptor can support bidirectional communication, letting the BCI hardware device receive contextual information back from the host computing device, and allowing the BCI hardware device to update its own state (for example, switching decoding models) depending on how a person is interacting with their device.
- The descriptor provides a way to send high-level commands to the operating system. It’s up to the BCI hardware device manufacturer to decide how to interpret the relevant signals, and convert them to commands that the operating system can understand as user intent.

#### Hid Descriptor

The HID descriptor describes what the BCI hardware device can input and output. It defines the following input and output reports:

- [`Report ID 1: BCI input signal report`](brain-computer-interface-hid-reference-for-connecting-to-apple-platforms#Report-ID-1-BCI-input-signal-report.md)
- [`Report ID 2: BCI input button report`](brain-computer-interface-hid-reference-for-connecting-to-apple-platforms#Report-ID-2-BCI-input-button-report.md)
- [`Report ID 3: BCI input pointer report`](brain-computer-interface-hid-reference-for-connecting-to-apple-platforms#Report-ID-3-BCI-input-pointer-report.md)
- [`Report ID 4: BCI input item selection report`](brain-computer-interface-hid-reference-for-connecting-to-apple-platforms#Report-ID-4-BCI-input-item-selection-report.md)
- [`Report ID 4: BCI output scan information report`](brain-computer-interface-hid-reference-for-connecting-to-apple-platforms#Report-ID-4-BCI-output-scan-information-report.md)

##### Report Id 1 Bci Input Signal Report

This report provides real-time data on the interpretability and fidelity of neural signals the BCI hardware device acquires. This information helps the host computing device offer immediate user feedback through a visual indicator. When the host computing device receives a signal quality message, it can communicate that information in the UI. For example, iOS represents this information by an animated overlay visual when the Switch Control cursor has focus on an element.

###### Technical Summary

This section defines an input report (report ID = 1) for signal quality (BCI Usage 0x02).

- `signalQuality[0]` represents a *button number ID*.
- `signalQuality[1]` represents *neural activity strength*, which you scale from a percentage (`0-100`) to the full `0` to `255` range.

###### Sending Signal Quality Reports

The following code shows general examples of HID events a BCI hardware device might send to a host computing device. Since the firmware stack for HID messages might vary from manufacturer to manufacturer, follow these examples and modify them as necessary to the BCI hardware device’s framework. For example, some frameworks require the report ID in the first index of each report, so a signal quality report might use a three-element array instead of two.

```c
/**
 * Sends a BCI Signal Quality report focusing on neural activity strength
 * using IOHIDUserDeviceHandleReportWithTimeStamp.
 * 
 * @param hid_user_device A reference to your IOHIDUserDevice.
 * @param button_id The button number ID (e.g., 0, 1, 2, 3 as per descriptor comments).
 * @param neural_strength_percent Neural activity strength as a percentage (0-100).
 *                                This is scaled to the 0-255 range.
 * @param timestamp The timestamp for this report, typically from mach_absolute_time().
 */
void send_bci_neural_strength_report(void* hid_user_device, uint8_t button_id, uint8_t neural_strength_percent, uint64_t timestamp) {
    BCIInputSignalReport report;
    bzero(&report, sizeof(report));
    
    // 1. Set the Report ID.
    report.reportId = 1;

    // 2. Set the specific fields:
    //    signalQuality[0] for "button number ID"
    report.signalQuality[0] = button_id;

    //    signalQuality[1] for "neural activity strength"
    //    Scale the percentage (0-100) to the 0-255 range.
    //    Using floating point for precision, then cast back to uint8_t.
    report.signalQuality[1] = (uint8_t)((float)neural_strength_percent * 255.0 / 100.0);

    // 3. Send the report.
    IOHIDUserDeviceHandleReportWithTimeStamp(
        hid_user_device,
        timestamp,
        (uint8_t*)&report,
        sizeof(report)
    );
}
```

##### Report Id 2 Bci Input Button Report

This report allows the BCI hardware device to simulate button presses and releases, for either sending basic system inputs (like navigation actions or performing a selection) or high-level system actions relevant to the host computing device’s operating system. The host computing device can map these button events to assistive technology features (such as Switch Control) or to various actions such as marking the current element as selected, navigating to the next element, navigating to the previous element, or other custom commands.

###### Technical Summary

This section defines an input report (report ID = 2) for 32 buttons (HID Button Usage Page).

- Each button’s state is a single bit: `0` for button up (released) and `1` for button down (pressed).
- These 32 individual bits are in 4 bytes (`UInt8 buttons[4]`).
- The button states are *absolute*, meaning the report sends the current state of all 32 buttons, not just changes.
- For iOS, the button events mappings are as follows:

```c
List of actions:
{
    Select,
    MoveToNextItem,
    MoveToPreviousItem,
    ToggleAssistiveTechnologyMenu,
    Activate,
    StartSequentialNavigation,
    StopSequentialNavigation,
    TriggerAutomation, 
    ToggleAppSwitcher,
    Home,
    ToggleNotificationsView,
    Assistant,
    VolumeDown,
    VolumeUp,
    ToggleDictation,
    ToggleAccessibilityFeature,
    ToggleQuickSettingsView,
    Escape,
    ScrollUp,
    ScrollDown,
    ScrollLeft,
    ScrollRight
}
```

###### Sending Button Event Reports

```c
/**
 * Sends a report with the button pressed, then immediately sends another
 * report with the button released, while preserving the state of other buttons.
 *
 * @param hid_user_device A reference to your IOHIDUserDevice.
 * @param button_index The 0-based index of the button to click (0 to 31).
 * @param press_timestamp The timestamp for the button press report.
 * @param release_timestamp The timestamp for the button release report.
 *                          Typically, release_timestamp is >= press_timestamp.
 */
void send_bci_button_click(void* hid_user_device, uint8_t button_index, uint64_t press_timestamp, uint64_t release_timestamp) {
    if (button_index >= 32) {
        // Error: Invalid button index. Must be between 0 and 31.
        return;
    }

    // Determine which byte in the 'buttons' array holds this button's state.
    uint8_t byte_index = button_index / 8;
    // Determine the position (bit mask) within that byte.
    uint8_t bit_mask = 1 << (button_index % 8);

    // --- Step 1: Send Button Pressed Report ---
    // Create a temporary report copy based on the current overall state.
    BCIInputButtonReport press_report;
    memcpy(&press_report, &currentButtonState, sizeof(BCIInputButtonReport));
    press_report.reportId = 2; // Ensure Report ID is set.

    // Set the specific button's bit to 1 (pressed) in the temporary report.
    press_report.buttons[byte_index] |= bit_mask;

    // Send the report indicating the button is pressed.
    IOHIDUserDeviceHandleReportWithTimeStamp(
        hid_user_device,
        press_timestamp,
        (uint8_t*)&press_report,
        sizeof(press_report)
    );

    // --- Step 2: Send Button Released Report ---
    // The previous 'press_report' already contains the correct state for other buttons.
    // Now, just clear the specific button's bit in that same temporary report.
    // This ensures only the pressed button changes state.
    press_report.buttons[byte_index] &= ~bit_mask;

    // Send the report indicating the button is released.
    IOHIDUserDeviceHandleReportWithTimeStamp(
        hid_user_device,
        release_timestamp,
        (uint8_t*)&press_report,
        sizeof(press_report)
    );
}
```

##### Report Id 3 Bci Input Pointer Report

This report functions as a cursor onscreen for features such as Switch Control. This can be a 2D or 3D pointer. The host computing device can use this information to:

- Move an onscreen cursor.
- Control a point scanner absolutely if the host computing device supports such a mode. Switch Control in iOS, iPadOS, and visionOS supports this mode with gliding cursor. This allows the BCI device to control the pointer manually.

###### Technical Summary

This section defines an input report (report ID = 3) for a pointer (HID Generic Desktop Usage Page).

- It includes three 8-bit signed values (`SInt8`) for x, y, and z axis movement. These values range from `-127` to `127`.
- All x, y, and z values are *relative changes* (deltas) from the previous state, not absolute positions. For example, a value of `5` for x represents a movement of 5 units to the right, not an absolute coordinate of 5.

###### Sending Pointer Event Reports

To send pointer movement data, you populate the `BCIInputPointerReport` structure with the deltas for x, y, and z.

```c
/**
 * Sends a BCI Pointer Report with relative movement data using
 * IOHIDUserDeviceHandleReportWithTimeStamp.
 *
 * @param hid_user_device A reference to your IOHIDUserDevice.
 * @param delta_x The relative movement along the x-axis (-127 to 127).
 * @param delta_y The relative movement along the y-axis (-127 to 127).
 * @param delta_z The relative movement along the z-axis (-127 to 127).
 * @param timestamp The timestamp for this report, typically from mach_absolute_time().
 */
void send_bci_pointer_report(void* hid_user_device, int8_t delta_x, int8_t delta_y, int8_t delta_z, uint8_t p_id, uint64_t timestamp) {
    BCIInputPointerReport report;

    // 1. Set the Report ID.
    report.reportId = 3;

    // 2. Set the position deltas.
    report.position[0] = delta_x; // x-axis movement
    report.position[1] = delta_y; // y-axis movement
    report.position[2] = delta_z; // z-axis movement

    // 3. Send the report.
    IOHIDUserDeviceHandleReportWithTimeStamp(
        hid_user_device,
        timestamp,
        (uint8_t*)&report,
        sizeof(report)
    );
}
```

##### Report Id 4 Bci Input Item Selection Report

This report allows the BCI hardware device to directly influence the element selection of accessibility features (like Switch Control). By sending a specific `itemIndex`, the BCI hardware device can instruct the host computing device to activate a particular UI item.

The BCI hardware device can obtain an understanding of the current UI context and determine which item to select by observing the corresponding output reports for item selection ([`Report ID 4: BCI output scan information report`](brain-computer-interface-hid-reference-for-connecting-to-apple-platforms#Report-ID-4-BCI-output-scan-information-report.md)).

###### Technical Summary

This section defines an input report for item selection (BCI Usage 0x04). It contains a single 8-bit field, `itemIndex`, which has a logical range from `0` to `255`.

###### Sending Item Selection Event Reports

```c
/**
 * Sends a BCI Item Selection Report using IOHIDUserDeviceHandleReportWithTimeStamp.
 * Use this report to direct an accessibility feature like Switch Control
 * to move focus to a specific item.
 *
 * @param hid_user_device A reference to your IOHIDUserDevice.
 * @param item_index The index of the item to select or focus on (0 to 255).
 * @param timestamp The timestamp for this report, typically from mach_absolute_time().
 */
void send_bci_item_selection_report(void* hid_user_device, uint8_t item_index, uint64_t timestamp) {
    BCIInputItemSelection report;
    bzero(&report, sizeof(report));
    // 1. Set the Report ID.
    report.reportId = 4;

    // 2. Set the item index.
    report.itemIndex = item_index;

    // 3. Send the report.
    IOHIDUserDeviceHandleReportWithTimeStamp(
        hid_user_device,
        timestamp,
        (uint8_t*)&report,
        sizeof(report)
    );
}
```

##### Report Id 4 Bci Output Scan Information Report

This report allows the host computing device (such as an iPhone with Switch Control on) to provide feedback and contextual information to the BCI hardware device about the current state of the interval-based sequential navigation process, also known as a *switch scanning mode*. The BCI hardware device can use this information to:

- Understand the context of the scanning cycle (for example, number of items or type of control)
- Select items using the BCI input item selection report ([`Report ID 4: BCI input item selection report`](brain-computer-interface-hid-reference-for-connecting-to-apple-platforms#Report-ID-4-BCI-input-item-selection-report.md))
- Adjust its behavior depending on the currently focused item

> **Note**: The host computing device doesn’t send information about the focused item if it’s a keyboard key (for example, from a software keyboard) to protect user privacy.

###### Technical Summary

This section defines an output report (report ID = 4), which is data the host computing device sends this data to the BCI hardware device. It describes a total of 6 bytes of information with a range from `0` to `255`:

| Byte | Type | Name | Description |
| --- | --- | --- | --- |
| 1 | `UInt8` | `selectedItem` | The index of the item that’s currently in focus by Switch Control. |
| 2 | `UInt8` | `numberOfItems` | The total number of items in the current scan cycle in Switch Control. |
| 3 | `UInt8` | `seed` | A unique identifier for the current scan cycle. You can use this value to distinguish between different scanning passes or groups. |
| 4 | `UInt8` | `itemControlType` | The type of the currently focused item or group. `0` indicates a discrete item, and `1` indicates a continuous control (like a scrollable item or a slider). |
| 5 | `UInt8` | `uiScanningLatencyInt` | The integer part of the UI scanning latency. This value represents the time between the host handling packet responses from the device and when “Move next/previous” commands are processed internally. |
| 6 | `UInt8` | `uiScanningLatencyFrac` | The fractional part of the UI scanning latency. This value is `x/255`, where `x` is the byte’s value. |

###### Receiving Selected Item Reports

```c
typedef struct {
    uint8_t reportId;
    uint8_t selectedItem;
    uint8_t numberOfItems;
    uint8_t seed;
    uint8_t itemControlType;
    uint8_t uiScanningLatencyInt;
    uint8_t uiScanningLatencyFrac;
} BCIOutputScanInfoReport;


// --- Register the Callback Function ---
void setup_and_register_callback(IOHIDUserDeviceRef userDevice) {
    // Allocate a buffer for incoming reports. Make sure its size is at least
    // as large as the biggest Output Report (including the Report ID byte).
    // This example uses a static buffer.
    static uint8_t outputReportBuffer[sizeof(BCIOutputScanInfoReport)];

    // Register the callback function with the system.
    IOHIDUserDeviceRegisterInputReportCallback(
        userDevice,
        outputReportBuffer,
        sizeof(outputReportBuffer),
        output_report_callback,
        NULL // optional context
    );
}

// --- Define the Callback Function ---
void output_report_callback(void* context, IOReturn result, void* sender, IOHIDReportType type, uint32_t reportID, uint8_t* report, CFIndex reportLength) {
    // Check if the callback was successful and the report type is correct.
    if (result != kIOReturnSuccess || type != kIOHIDReportTypeOutput) {
        fprintf(stderr, "Callback received an error or unexpected report type.\n");
        return;
    }

    if (reportID == 4) {
        printf("Received Output Report with ID 4.\n");

        // Cast the raw report buffer to the structured type for easy access.
        BCIOutputScanInfoReport* received_info = (BCIOutputScanInfoReport*)report;

        // Process the data (similar to the handle_bci_output_scan_info_report function).
        float reconstructed_latency = (float)received_info->uiScanningLatencyInt + ((float)received_info->uiScanningLatencyFrac / 255.0f);
        printf("  - Selected Item: %d\n", received_info->selectedItem);
        printf("  - Number of Items: %d\n", received_info->numberOfItems);
        printf("  - Item Control type : %d\n", received_info->itemControlType);
        printf("  - Latency: %.2f seconds\n", reconstructed_latency);
    } else {
        printf("Received Output Report with unhandled ID: %u\n", reportID);
    }
}
```

#### Appendix

The following section provides an example HID descriptor for a BCI hardware device, and defines example structures for the input and output reports.

##### Example Bci Hid Descriptor and Report Structure

This header declares the protocol you integrate into the firmware for any BCI hardware device that needs to send and receive BCI HID messages.

```c
typedef struct {
    UInt8 reportId;
    UInt8 signalQuality[2]; // 2 8-bit fields for signal quality: 0-255
} BCIInputSignalReport;

typedef struct {
    UInt8 reportId;
    UInt8 buttons[4]; //  4 8-bit fields for 32 buttons (0 = button up, 1 = button down)
} BCIInputButtonReport;

typedef struct {
    UInt8 reportId;
    UInt8 itemIndex;
} BCIInputItemSelection;

typedef struct {
    UInt8 reportId;
    SInt8 position[3]; // 3 8-bit fields for x, y, z positioning: -127-127
} BCIInputPointerReport;


static char BCIDescriptor[] = {

    0x05, 0x60,                               // Usage Page (Brain Control Interface)
    0x09, 0x01,                               // Usage 1 (BCI Application)
    0xA1, 0x01,                               // Collection (Application)
    
    // Signal quality (Decorator)
    //   Use to show selection during item scanning.
    //   When item scanning is off, it can show feedback in a small area.
    //   Decorators: 0 = button number ID, 1 = neural activity strength
    
    0x05, 0x60,                               //   Usage Page (Brain Control Interface)
    0x09, 0x02,                               //   Usage 2 (Signal Quality)
    0x85, 0x01,                               //   ReportID................ (1)
    0xA1, 0x02,                               //   Collection (Logical)
    0x09, 0x02,                               //     Usage 2 (0x2)
    0x15, 0x00,                               //     Logical Minimum......... (0)
    0x26, 0xFF, 0x00,                         //     Logical Maximum......... (255)
    0x75, 0x08,                               //     Report Size............. (8)
    0x95, 0x02,                               //     Report Count............ (2)
    0x81, 0x06,                               //     Input...................(Data, Variable, Relative)
    0xC0,                                     //   End Collection
    
    // BCI Buttons
    //   By default, button 0 = select, button 1 = next, button 2 = previous, button 3 = menu
    0x05, 0x09,                               //   Usage Page (Button)
    0x09, 0x01,                               //   Usage 1 (0x1)
    0x85, 0x02,                               //   ReportID................ (2)
    0xA1, 0x00,                               //   Collection (Physical)
    0x19, 0x01,                               //     Usage Minimum........... (1)
    0x29, 0x20,                               //     Usage Maximum........... (32)
    0x15, 0x00,                               //     Logical Minimum......... (0)
    0x25, 0x01,                               //     Logical Maximum......... (1)
    0x75, 0x01,                               //     Report Size............. (1)
    0x95, 0x20,                               //     Report Count............ (32)
    0x81, 0x02,                               //     Input...................(Data, Variable, Absolute)
    0xC0,                                     //   End Collection
    
    // Pointer: You can have as many of these as needed.
    //  When received, it can move the head tracker.
    //  If the device is in gliding cursor mode, it can move the gliding cursor absolutely.
    0x05, 0x01,                               //   Usage Page (Generic Desktop)
    0x09, 0x01,                               //   Usage (Pointer)
    0x85, 0x03,                               //   ReportID................ (3)
    0xA1, 0x00,                               //   Collection (Physical)
    0x09, 0x30,                               //     Usage (X)
    0x09, 0x31,                               //     Usage (Y)
    0x09, 0x32,                               //     Usage (Z)
    0x15, 0x81,                               //     Logical Minimum......... (-127)
    0x25, 0x7F,                               //     Logical Maximum......... (127)
    0x75, 0x08,                               //     Report Size............. (8)
    0x95, 0x03,                               //     Report Count............ (3)
    0x81, 0x06,                               //     Input...................(Data, Variable, Relative)
    0xC0,                                     //   End Collection

    // Item selection
    0x05, 0x60,                               //   Usage Page (Brain Control Interface)
    0x09, 0x04,                               //   Usage 4 (BCI - Item Selection)
    0x85, 0x04,                               //   ReportID................ (4)
    0xA1, 0x02,                               //   Collection (Logical)
    0x09, 0x04,                               //     Usage 4 (0x4)
    0x15, 0x00,                               //     Logical Minimum......... (0)
    0x26, 0xFF, 0x00,                         //     Logical Maximum......... (255)
    0x75, 0x08,                               //     Report Size............. (8)
    0x95, 0x01,                               //     Report Count............ (1)
    0x81, 0x06,                               //     Input...................(Data, Variable, Relative)
    0xC0,
    
    // Output - Selected Item (typically random per ring)/Number of Items/Ring ID/Item Control Type
    //   This is output each time the scanner moves focus to an item.
    //   When on keyboard (for privacy), only send UI scanning latency. Other fields are zero-set.
    // 1st byte: Selected item.
    // 2nd byte: Number of items.
    // 3rd byte: The seed for this era to distinguish from others.
    // 4th byte: Item control type (discrete item = 0, continuous = 1 (for example, scrollbars) ).
    // 5-6th byte: UI scanning latency. The two reports join the integer and fractional parts of a float.
    //    The host computing device interprets the fractional part as x/255, where x is the 6th byte's value.
    //    The time between handling packet responses in iOS for when "Move next" commands are received from the BCI device.
    0x05, 0x60,                               //   Usage Page (Brain Control Interface)
    0xA1, 0x02,                               //   Collection (Logical)
    0x85, 0x04,                               //     ReportID................ (4)
    0x09, 0x03,                               //     Usage 3 (BCI - Number of item)
    0x15, 0x00,                               //     Logical Minimum......... (0)
    0x26, 0xFF, 0x00,                         //     Logical Maximum......... (255)
    0x75, 0x08,                               //     Report Size............. (8)
    0x95, 0x06,                               //     Report Count............ (6)
    0x91, 0x03,                               //     Output..................(Constant)
    0xC0,                                     //   End Collection

    0xC0,                                     // End Collection
};
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/brain-computer-interface-hid-reference-for-connecting-to-apple-platforms)*