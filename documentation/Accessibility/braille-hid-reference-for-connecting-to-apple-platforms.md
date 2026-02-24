# Braille HID reference for connecting to Apple platforms

**Framework**: Accessibility

An overview of the human interface device (HID) descriptor for interfacing between braille devices and Apple devices.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 12.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 7.2+

#### Overview

This document provides a reference for manufacturers of third-party braille devices who want to build in firmware support for interfacing with Apple devices, such as iPhone and Mac.

People who are blind or have low vision can access text and sometimes images using a refreshable braille display, which dynamically raises and lowers tactile dots on a surface. Many braille displays also have various input controls, such as buttons, keys, and switches, that people can use to navigate a user interface and type braille cells. There are also braille devices that only have input controls and no display.

This document uses the term *braille devices* to refer to either braille devices with input controls, braille displays, or devices that support both.

People can use some braille devices as a standalone device, but this document describes devices that are also designed for people to connect to a general-purpose electronic computing device such as a computer, phone, tablet, or watch. When a braille device is connected, the computing device controls what’s displayed through tactile dots, and interprets the input buttons.

#### Hid Descriptor Background

The USB-IF human interface device (HID) standard for braille devices describes specifications that allow braille devices to connect to computing platforms such as macOS and iOS. For more information about this USB-IF HID standard, visit [`http://www.usb.org/`](https://developer.apple.comhttp://www.usb.org/).

Apple platforms support the HID protocol for braille devices over Bluetooth and USB transport. For iPhones and iPads, USB support is available only for models with USB-C connectors.

#### Hid Descriptor

To make a braille device compatible with the HID standard for braille devices, the device needs to expose a *HID descriptor* that describes the characteristics of the display. This HID descriptor includes a device report that typically specifies the number of braille cells, various buttons, braille or Perkins keys, and router keys. These specifications are available in the Braille Usage Page (Code 0x41). The device report sets the parameters for how the braille device sends data (button presses or other controls) and how it receives data (braille cell updates).

For processing input events such as button presses, the input report mirrors the structure of the input elements of the device report. Most of the input events are button presses, so make sure to send a down and up event. The down event has a non-zero value for that control. The up event has a value of zero for that control in the input report.

##### Braille Cells

The following code shows an example device report for a braille display that has 20 8-dot braille cells:

```c
static char BrailleDevice[] = {
    0x05, 0x41,        // Usage Page (Braille)
    0x09, 0x01,        // Usage (Braille Display)
    0xA1, 0x01,        // Collection (Application)
    
    0x05, 0x41,        //   Usage Page (Braille)
    0x09, 0x02,        //   Usage (Braille Row)
    
    0xA1, 0x02,        //   Collection (Logical)
    0x09, 0x04,        //     Usage (8-Dot Braille Cell)
    0x15, 0x00,        //     Logical Minimum (0)
    0x26, 0xFF, 0x00,  //     Logical Maximum (255)
    0x75, 8,           //     Report Size (8)
    0x95, 20,          //     Report Count (20) - This means it's a 20-cell braille display.
    0x91, 0x03,        //     Output (Const,Var,Abs,No Wrap,Linear,Preferred State,No Null Position,Non-volatile)
    
    0xC0,              //   End Collection
    0xC0               // End Collection
};
```

The type of braille cell is also set in the usage for the braille row:

```c
6-dot braille cell = 0x03
8-dot braille cell = 0x04
```

When the braille device receives an update for the braille cells, the cells are in accordance with [`ISO/TR 11548‐1`](https://developer.apple.comhttp://www.unicode.org/versions/Unicode5.2.0/ch15.pdf).

The following code shows an example byte buffer for an update that spells out “hello” in Unified English Braille (UEB) that the braille device might receive. In decimal, this is:

```c
{ 19, 17, 7, 7, 21, 0 }
```

The braille device can interpret the first character (`19`) as a bit field for braille pattern dots: 1, 2, 5 (h in UEB).

```c
{ 0001 0011 }
```

##### Router Buttons

Many braille cells have a router button above each cell that helps people move cursor positions. The following code shows an example of the bytes you set in your device report for 20 router buttons:

```c
    0x09, 0xFA,        //     Usage (Router Set 1)
    0xA1, 0x02,        //     Collection (Logical)
    0x0A, 0x00, 0x01,  //       Usage (Router Key)
    0x15, 0x00,        //       Logical Minimum (0)
    0x25, 0x01,        //       Logical Maximum (1)
    0x75, 1,           //       Report Size (1)
    0x95, 20,          //       Report Count (20)
    0x81, 0x02,        //       Input (Data,Var,Abs,No Wrap,Linear,Preferred State,No Null Position)
    0xC0,              //     End Collection
```

When a person presses a router button, the braille device needs to generate an input report to send to the computing device. In this example, the braille device only has router buttons as input, so the input report only accounts for the 20 bits of router buttons:

```c
typedef struct {
    UInt8 routerButtons : 20;    
} BrailleInputReport;
```

For example, if a person presses the third router button, here’s the corresponding input report:

```c
BrailleInputReport report;
bzero(&report, sizeof(report));
report.routerButtons = 1 << 3;
```

##### Braille Keys

If a braille display allows for input, many have six or eight Perkins-style braille keys that are available for inputting braille patterns.

- If there are six braille keys, traditionally they’re arranged from left to right as 3, 2, 1, spacing and then 4, 5, 6.
- If there are eight braille keys, traditionally they’re arranged from left to right as 7, 3, 2, 1, spacing and then 4, 5, 6, 8.

The following code shows an example of a 20-cell braille display with router buttons and eight Perkins keys:

```c
static char BrailleDevice[] = {
    0x05, 0x41,        // Usage Page (Braille)
    0x09, 0x01,        // Usage (Braille Display)
    0xA1, 0x01,        // Collection (Application)
    
    // 8 Perkins Braille Keys
    0x1A, 0x01, 0x02,  //   Usage Minimum (Braille Keyboard Dot 1)
    0x2A, 0x08, 0x02,  //   Usage Maximum (Braille Keyboard Dot 8)
    0x75, 0x01,        //   Report Size (1)
    0x95, 0x08,        //   Report Count (8)
    0x15, 0x00,        //   Logical Minimum (0)
    0x25, 0x01,        //   Logical Maximum (1)
    0x81, 0x02,        //   Input (Data,Var,Abs,No Wrap,Linear,Preferred State,No Null Position)
    
    // Braille Cells
    0x05, 0x41,        //   Usage Page (Braille)
    0x09, 0x02,        //   Usage (Braille Row)
    0xA1, 0x02,        //   Collection (Logical)
    0x09, 0x04,        //     Usage (8-Dot Braille Cell)
    0x15, 0x00,        //     Logical Minimum (0)
    0x26, 0xFF, 0x00,  //     Logical Maximum (255)
    0x75, 8,           //     Report Size (8)
    0x95, 20,          //     Report Count (20) - 20-cell braille display.
    0x91, 0x03,        //     Output (Const,Var,Abs,No Wrap,Linear,Preferred State,No Null Position,Non-volatile)

    // Router Buttons    
    0x09, 0xFA,        //     Usage (Router Set 1)
    0xA1, 0x02,        //     Collection (Logical)
    0x0A, 0x00, 0x01,  //       Usage (Router Key)
    0x15, 0x00,        //       Logical Minimum (0)
    0x25, 0x01,        //       Logical Maximum (1)
    0x75, 1,           //       Report Size (1)
    0x95, 20,          //       Report Count (20)
    0x81, 0x02,        //       Input (Data,Var,Abs,No Wrap,Linear,Preferred State,No Null Position)
    0xC0,              //     End Collection

    0xC0,              //   End Collection
    0xC0               // End Collection
};
```

For this device, the input report structure is:

```c
typedef struct {
    UInt8 brailleKeys : 8;
    UInt8 routerButtons : 20;    
} BrailleInputReport;
```

For example, if a person presses braille keys 1, 2, 5 (h - chord in UEB), the input report is:

```c
BrailleInputReport report;
bzero(&report, sizeof(report));
report.brailleKeys = (1 << 0) | (1 << 1) | (1 << 4);
```

##### Buttons

Braille displays often have buttons that let people control the computing device to perform commands such as navigation, panning, enter, space, and more. The HID standard for braille devices categorizes these as follows:

- **`Braille Face/Left/Right/Top/Joystick/Dpad Controls`**: A collection of controls located on various sides of a braille display that are either buttons, joysticks, or directional pads.

The following code shows an example of an addition that you can make to the device report that specifies three braille left controls. For other categories of controls, see [`Appendix`](braille-hid-reference-for-connecting-to-apple-platforms#Appendix.md).

```c
...
    0x0A, 0x0D, 0x02,  //   Usage (Braille Left Controls)
    0xA1, 0x02,        //   Collection (Logical)
    0x05, 0x09,        //     Usage Page (Button)
    0x19, 0x01,        //     Usage Minimum (Button 1)
    0x29, 0x03,        //     Usage Maximum (Button 3)
    0x75, 0x01,        //     Report Size (1)
    0x95, 0x03,        //     Report Count (3)
    0x15, 0x00,        //     Logical Minimum (0)
    0x25, 0x01,        //     Logical Maximum (1)
    0x81, 0x02,        //     Input (Data,Var,Abs,No Wrap,Linear,Preferred State,No Null Position)
    0xC0,              //   End Collection
...
```

After making this addition, the input report structure is:

```c
typedef struct {
    UInt8 brailleKeys : 8;
    UInt8 routerButtons : 20;    
    UInt8 brailleLeftButtons : 3;    
} BrailleInputReport;
```

##### Braille Pan Controls

Braille panning allows a person to move the focus of the braille cells either to the right or the left to bring the rest of a line of text into view. Traditionally, there are pan-left and pan-right controls.

The following code shows an example of a device report that has braille pan-left buttons:

```c
    0x0A, 0x0D, 0x02,  //   Usage (Braille Left Controls)
    0xA1, 0x02,        //   Collection (Logical)
    0x05, 0x41,        //     Usage Page (Braille)
    0x0A, 0x1A, 0x02,  //     Usage (Pan Left)
    0x75, 0x01,        //     Report Size (1)
    0x95, 0x01,        //     Report Count (1)
    0x15, 0x00,        //     Logical Minimum (0)
    0x25, 0x01,        //     Logical Maximum (1)
    0x81, 0x02,        //     Input (Data,Var,Abs,No Wrap,Linear,Preferred State,No Null Position)
    0xC0,              //   End Collection
```

##### Screen Reader Identification

You can determine which screen reader is connected to the braille device by using the screen reader identifier. To receive this value, include the screen reader identification feature in your device report:

```c
    0x05, 0x41,        //   Usage Page (Braille)
    0x09, 0x07,        //   Usage (Screen Reader Identifier)
    0x95, 0x01,        //   Report Count (1)
    0x75, 0x80,        //   Report Size (128)
    0xB1, 0x02,        //   FEATURE (Data,Var,Abs)
```

When the computing device detects this, it sends a report back when your device connects. Apple returns the following identifiers for VoiceOver depending on platform:

**iOS, iPadOS, tvOS, visionOS, watchOS**:

```c
{ 0xd2, 0x11, 0xec, 0x73, 0xae, 0x43, 0x4b, 0x2b, 0xa6, 0x91, 0x5f, 0x66, 0x20, 0xb4, 0xdb, 0xf6 }
```

**macOS**:

```c
{ 0xbc, 0x4b, 0x74, 0xea, 0xb7, 0x87, 0x4a, 0x6d, 0xb5, 0x72, 0x4e, 0x2d, 0x74, 0x6a, 0x9a, 0xfd }
```

##### Apple Screen Reader Controls

The HID standard for braille devices allows the device to issue platform-specific commands to the screen reader. For example, Magic Tap is a command that’s available in iOS, but not macOS. If a button press controls Magic Tap in iOS, you can change that when detecting the macOS VoiceOver version.

To define these, indicate in the device report that you have screen reader controls available:

```c
    0x05, 0x41,        //   Usage Page (Braille)
    0x09, 0x06,        //   Usage (Screen Reader Controls)
    0xA1, 0x02,        //     Collection (Logical)
    0x05, 0x09,        //     Usage Page (Button)
    0x19, 0x01,        //     Usage Minimum (Button 1)
    0x29, 0x08,        //     Usage Maximum (Button 8)
    0x75, 0x01,        //     Report Size (1)
    0x95, 0x08,        //     Report Count (8)
    0x15, 0x00,        //     Logical Minimum (0)
    0x25, 0x01,        //     Logical Maximum (1)
    0x81, 0x02,        //     Input (Data,Var,Abs,No Wrap,Linear,Preferred State,No Null Position)
    0xC0,              //   End Collection
```

Then, that button can generate a specific value that corresponds to commands for the relevant screen reader version.

For available commands, see [`Braille screen reader controls`](braille-hid-reference-for-connecting-to-apple-platforms#Braille-screen-reader-controls.md).

##### Composite Displays

You can also combine braille displays with other HID devices, such as keyboards. In this case, make sure the device report includes both a braille usage page that describes braille behavior, and a keyboard usage page that describes the keyboard. The system handles keyboard events, but the screen reader handles the braille page events.

#### Appendix

The following sections provide a reference for HID values related to braille devices.

##### Hid Usage and Usage Pages for Braille Devices

```c
enum
{
    kHIDPage_Braille = 0x41
};

enum
{
    kHIDUsage_BrailleDisplay = 0x01,
    kHIDUsage_BrailleRow = 0x02,
    kHIDUsage_6DotBrailleCell = 0x03,
    kHIDUsage_8DotBrailleCell = 0x04,
    kHIDUsage_NumberOfBrailleCells = 0x05,
    kHIDUsage_screen readerControl = 0x06,
    kHIDUsage_screen readerIdentifier = 0x07,
    
    // 08-F9 Reserved
    
    kHIDUsage_RotorSet1 = 0xFA,
    kHIDUsage_RotorSet2 = 0xFB,
    kHIDUsage_RotorSet3 = 0xFC,
    
    kHIDUsage_RouterButton = 0x100,    
    
    kHIDUsage_BrailleButtons = 0x200,
    kHIDUsage_BrailleButton_Dot1  = 0x201,
    kHIDUsage_BrailleButton_Dot2  = 0x202,
    kHIDUsage_BrailleButton_Dot3  = 0x203,
    kHIDUsage_BrailleButton_Dot4  = 0x204,
    kHIDUsage_BrailleButton_Dot5  = 0x205,
    kHIDUsage_BrailleButton_Dot6  = 0x206,
    kHIDUsage_BrailleButton_Dot7  = 0x207,
    kHIDUsage_BrailleButton_Dot8  = 0x208,
    kHIDUsage_BrailleButton_Space = 0x209,
    kHIDUsage_BrailleButton_Left_Space = 0x20A,
    kHIDUsage_BrailleButton_Right_Space = 0x20B,
    kHIDUsage_BrailleFaceControls = 0x20C,
    kHIDUsage_BrailleLeftControls = 0x20D,
    kHIDUsage_BrailleRightControls = 0x20E,
    kHIDUsage_BrailleTopControls = 0x20F,
    kHIDUsage_BrailleJoystickCenter = 0x210,
    kHIDUsage_BrailleJoystickUp = 0x211,
    kHIDUsage_BrailleJoystickDown = 0x212,
    kHIDUsage_BrailleJoystickLeft = 0x213,
    kHIDUsage_BrailleJoystickRight = 0x214,
    kHIDUsage_BrailleDPadCenter = 0x215,
    kHIDUsage_BrailleDPadUp = 0x216,
    kHIDUsage_BrailleDPadDown = 0x217,
    kHIDUsage_BrailleDPadLeft = 0x218,
    kHIDUsage_BrailleDPadRight = 0x219,
    kHIDUsage_BraillePanLeft = 0x21A,
    kHIDUsage_BraillePanRight = 0x21B,
    kHIDUsage_BrailleRockerUp = 0x21C,
    kHIDUsage_BrailleRockerDown = 0x21D,
    kHIDUsage_BrailleRockerPress = 0x21E,

}
```

##### Braille Screen Reader Controls

**iOS, iPadOS, tvOS, visionOS, watchOS**:

```c
enum {
    kHIDUsage_BrailleNextInputMode = 0x001,
    kHIDUsage_BrailleNextOutputMode = 0x002,
    kHIDUsage_BraillePanLeft = 0x003,
    kHIDUsage_BraillePanRight = 0x004,
    kHIDUsage_BrailleDelete = 0x005,
    kHIDUsage_BrailleForwardDelete = 0x006,
    kHIDUsage_BrailleReturn = 0x007,
    kHIDUsage_BrailleEscape = 0x008,
    kHIDUsage_BrailleToggleContracted = 0x009,
    kHIDUsage_BrailleToggleEightDot = 0x00A,
    kHIDUsage_BrailleMoveToStatusBar = 0x011,
    kHIDUsage_BrailleMoveToFirstItem = 0x012,
    kHIDUsage_BrailleMoveToLastItem = 0x013,
    kHIDUsage_BraillePreviousItem = 0x014,
    kHIDUsage_BrailleNextItem = 0x015,
    kHIDUsage_BrailleReadFromTop = 0x016,
    kHIDUsage_BrailleReadAll = 0x017,
    kHIDUsage_BrailleScrollLeft = 0x018,
    kHIDUsage_BrailleScrollRight = 0x019,
    kHIDUsage_BrailleScrollUp = 0x01A,
    kHIDUsage_BrailleScrollDown = 0x01B,
    kHIDUsage_RotorRight = 0x021,
    kHIDUsage_RotorLeft = 0x022,
    kHIDUsage_RotorUp = 0x023,
    kHIDUsage_RotorDown = 0x024,
    kHIDUsage_BrailleTap = 0x025,
    kHIDUsage_BrailleStartStopSpeech = 0x026,
    kHIDUsage_BrailleMagicTap = 0x027,
    kHIDUsage_BrailleMoveToDesktop = 0x031,
    kHIDUsage_BrailleMoveToDock = 0x032,
    kHIDUsage_BrailleMoveToMenuBar = 0x033,
    kHIDUsage_BrailleInteract = 0x034,
    kHIDUsage_BrailleStopInteract = 0x035,
    kHIDUsage_NextHeading = 0x049,
    kHIDUsage_PreviousHeading = 0x04A,
    kHIDUsage_NextGraphic = 0x04B,
    kHIDUsage_PreviousGraphic = 0x04C,
    kHIDUsage_NextTable = 0x04D,
    kHIDUsage_PreviousTable = 0x04E,
    kHIDUsage_NextList = 0x04F,
    kHIDUsage_PreviousList = 0x050,
    kHIDUsage_NextControl = 0x051,
    kHIDUsage_PreviousControl = 0x052,
    kHIDUsage_NextBlockquote = 0x053,
    kHIDUsage_PreviousBlockquote = 0x054,
    kHIDUsage_NextSameBlockquote = 0x055,
    kHIDUsage_PreviousSameBlockquote = 0x056,
    kHIDUsage_NextLink = 0x057,
    kHIDUsage_PreviousLink = 0x058,
    kHIDUsage_NextVisitedLink = 0x059,
    kHIDUsage_PreviousVisitedLink = 0x05A,
    kHIDUsage_NextSameHeading = 0x05B,
    kHIDUsage_PreviousSameHeading = 0x05C,
    kHIDUsage_NextBoldText = 0x05D,
    kHIDUsage_PreviousBoldText = 0x05E,
    kHIDUsage_NextItalicText = 0x05F,
    kHIDUsage_PreviousItalicText = 0x060,
    kHIDUsage_NextUnderlineText = 0x061,
    kHIDUsage_PreviousUnderlineText = 0x062,
    kHIDUsage_NextMisspelledWord = 0x063,
    kHIDUsage_PreviousMisspelledWord = 0x064,
    kHIDUsage_NextPlainText = 0x065,
    kHIDUsage_PreviousPlainText = 0x066,
    kHIDUsage_NextColorChange = 0x067,
    kHIDUsage_PreviousColorChange = 0x068,
    kHIDUsage_NextFontChange = 0x069,
    kHIDUsage_PreviousFontChange = 0x06A,
    kHIDUsage_NextStyleChange = 0x06B,
    kHIDUsage_PreviousStyleChange = 0x06C,
    kHIDUsage_NextSameElement = 0x06D,
    kHIDUsage_PreviousSameElement = 0x06E,
    kHIDUsage_NextDifferentElement = 0x06F,
    kHIDUsage_PreviousDifferentElement = 0x070,
};
```

**macOS**:

```c
enum {
    kHIDUsage_BrailleNextInputMode = 0x001,
    kHIDUsage_BrailleNextOutputMode = 0x002,
    kHIDUsage_BraillePanLeft = 0x003,
    kHIDUsage_BraillePanRight = 0x004,
    kHIDUsage_BrailleDelete = 0x005,
    kHIDUsage_BrailleForwardDelete = 0x006,
    kHIDUsage_BrailleReturn = 0x007,
    kHIDUsage_BrailleEscape = 0x008,
    kHIDUsage_BrailleToggleContracted = 0x009,
    kHIDUsage_BrailleToggleEightDot = 0x00A,
    kHIDUsage_BrailleMoveToFirstItem = 0x012,
    kHIDUsage_BrailleMoveToLastItem = 0x013,
    kHIDUsage_BrailleReadFromTop = 0x016,
    kHIDUsage_BrailleReadAll = 0x017,
    kHIDUsage_BrailleScrollLeft = 0x018,
    kHIDUsage_BrailleScrollRight = 0x019,
    kHIDUsage_BrailleScrollUp = 0x01A,
    kHIDUsage_BrailleScrollDown = 0x01B,
    kHIDUsage_RotorRight = 0x021,
    kHIDUsage_RotorLeft = 0x022,
    kHIDUsage_RotorUp = 0x023,
    kHIDUsage_RotorDown = 0x024,
    kHIDUsage_BrailleTap = 0x025,
    kHIDUsage_BrailleStartStopSpeech = 0x026,
    kHIDUsage_BrailleMoveToDesktop = 0x031,
    kHIDUsage_BrailleMoveToDock = 0x032,
    kHIDUsage_BrailleMoveToMenuBar = 0x033,
    kHIDUsage_BrailleInteract = 0x034,
    kHIDUsage_BrailleStopInteract = 0x035,

    kHIDUsage_BrailleMoveUp = 0x041,
    kHIDUsage_BrailleMoveDown = 0x042,
    kHIDUsage_BrailleMoveLeft = 0x043,
    kHIDUsage_BrailleMoveRight = 0x044,
    kHIDUsage_BrailleWrapUp = 0x045,
    kHIDUsage_BrailleWrapDown = 0x046,
    kHIDUsage_BrailleWrapLeft = 0x047,
    kHIDUsage_BrailleWrapRight = 0x048,

    kHIDUsage_NextHeading = 0x049,
    kHIDUsage_PreviousHeading = 0x04A,
    kHIDUsage_NextGraphic = 0x04B,
    kHIDUsage_PreviousGraphic = 0x04C,
    kHIDUsage_NextTable = 0x04D,
    kHIDUsage_PreviousTable = 0x04E,
    kHIDUsage_NextList = 0x04F,
    kHIDUsage_PreviousList = 0x050,
    kHIDUsage_NextControl = 0x051,
    kHIDUsage_PreviousControl = 0x052,
    kHIDUsage_NextBlockquote = 0x053,
    kHIDUsage_PreviousBlockquote = 0x054,
    kHIDUsage_NextSameBlockquote = 0x055,
    kHIDUsage_PreviousSameBlockquote = 0x056,
    kHIDUsage_NextLink = 0x057,
    kHIDUsage_PreviousLink = 0x058,
    kHIDUsage_NextVisitedLink = 0x059,
    kHIDUsage_PreviousVisitedLink = 0x05A,
    kHIDUsage_NextSameHeading = 0x05B,
    kHIDUsage_PreviousSameHeading = 0x05C,
    kHIDUsage_NextBoldText = 0x05D,
    kHIDUsage_PreviousBoldText = 0x05E,
    kHIDUsage_NextItalicText = 0x05F,
    kHIDUsage_PreviousItalicText = 0x060,
    kHIDUsage_NextUnderlineText = 0x061,
    kHIDUsage_PreviousUnderlineText = 0x062,
    kHIDUsage_NextMisspelledWord = 0x063,
    kHIDUsage_PreviousMisspelledWord = 0x064,
    kHIDUsage_NextPlainText = 0x065,
    kHIDUsage_PreviousPlainText = 0x066,
    kHIDUsage_NextColorChange = 0x067,
    kHIDUsage_PreviousColorChange = 0x068,
    kHIDUsage_NextFontChange = 0x069,
    kHIDUsage_PreviousFontChange = 0x06A,
    kHIDUsage_NextStyleChange = 0x06B,
    kHIDUsage_PreviousStyleChange = 0x06C,
    kHIDUsage_NextSameElement = 0x06D,
    kHIDUsage_PreviousSameElement = 0x06E,
    kHIDUsage_NextDifferentElement = 0x06F,
};
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/braille-hid-reference-for-connecting-to-apple-platforms)*