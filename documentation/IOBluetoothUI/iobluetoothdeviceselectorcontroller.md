# IOBluetoothDeviceSelectorController

**Framework**: IOBluetooth UI  
**Kind**: class  
**Role**: Class

A NSWindowController subclass to display a window to initiate pairing to other bluetooth devices.

**Availability**:
- macOS 10.2+

## Declaration

```swift
class IOBluetoothDeviceSelectorController
```

```objc
@interface IOBluetoothDeviceSelectorController : NSWindowController
```

#### Overview

Implementation of a window controller to return a NSArray of selected bluetooth devices. This class will handle connecting to the Bluetooth Daemon for the purposes of searches, and displaying the results. This controller will return a NSArray of IOBluetoothDevice objects to the user.

## Topics

### Instance Methods
- [func addAllowedUUID(IOBluetoothSDPUUID!)](./iobluetoothdeviceselectorcontroller/addalloweduuid%28_%29.md)
  Adds a UUID to the list of UUIDs that are used to validate the user’s selection.
- [func addAllowedUUIDArray([Any]!)](./iobluetoothdeviceselectorcontroller/addalloweduuidarray%28_%29.md)
  Adds an array of UUIDs to the list of UUIDs that are used to validate the user’s selection.
- [func beginSheetModal(for: NSWindow!, modalDelegate: Any!, didEnd: Selector!, contextInfo: UnsafeMutableRawPointer!) -> IOReturn](./iobluetoothdeviceselectorcontroller/beginsheetmodal%28for,modaldelegate,didend,contextinfo%29.md)
  Runs the device selector panel as a sheet on the target window.
- [func clearAllowedUUIDs()](./iobluetoothdeviceselectorcontroller/clearalloweduuids%28%29.md)
  Resets the controller back to the default state where it will accept any device the user selects.
- [func getCancel() -> String!](./iobluetoothdeviceselectorcontroller/getcancel%28%29.md)
  Returns the title of the default/cancel button in the device selector panel.
- [func getDescriptionText() -> String!](./iobluetoothdeviceselectorcontroller/getdescriptiontext%28%29.md)
  Returns the description text that appears in the device selector panel.
- [func getHeader() -> String!](./iobluetoothdeviceselectorcontroller/getheader%28%29.md)
  Returns the header text that appears in the device selector panel.
- [func getOptions() -> IOBluetoothServiceBrowserControllerOptions](./iobluetoothdeviceselectorcontroller/getoptions%28%29.md)
  Returns the option bits that control the panel’s behavior.
- [func getPrompt() -> String!](./iobluetoothdeviceselectorcontroller/getprompt%28%29.md)
  Returns the title of the default/select button in the device selector panel.
- [func getResults() -> [Any]!](./iobluetoothdeviceselectorcontroller/getresults%28%29.md)
  Returns the result of the user’s selection.
- [func getSearchAttributes() -> UnsafePointer<IOBluetoothDeviceSearchAttributes>!](./iobluetoothdeviceselectorcontroller/getsearchattributes%28%29.md)
  Returns the search attributes that control the panel’s search/inquiry behavior.
- [func getTitle() -> String!](./iobluetoothdeviceselectorcontroller/gettitle%28%29.md)
  Returns the title of the device selector panel.
- [func runModal() -> Int32](./iobluetoothdeviceselectorcontroller/runmodal%28%29.md)
  Runs the device selector panel in a modal session to allow the user to select a Bluetooth device.
- [func setCancel(String!)](./iobluetoothdeviceselectorcontroller/setcancel%28_%29.md)
  Sets the title of the default/cancel button in the device selector panel.
- [func setDescriptionText(String!)](./iobluetoothdeviceselectorcontroller/setdescriptiontext%28_%29.md)
  Sets the description text that appears in the device selector panel.
- [func setHeader(String!)](./iobluetoothdeviceselectorcontroller/setheader%28_%29.md)
  Sets the header text that appears in the device selector panel.
- [func setOptions(IOBluetoothServiceBrowserControllerOptions)](./iobluetoothdeviceselectorcontroller/setoptions%28_%29.md)
  Sets the option bits that control the panel’s behavior.
- [func setPrompt(String!)](./iobluetoothdeviceselectorcontroller/setprompt%28_%29.md)
  Sets the title of the default/select button in the device selector panel.
- [func setSearchAttributes(UnsafePointer<IOBluetoothDeviceSearchAttributes>!)](./iobluetoothdeviceselectorcontroller/setsearchattributes%28_%29.md)
  Sets the search attributes that control the panel’s search/inquiry behavior.
- [func setTitle(String!)](./iobluetoothdeviceselectorcontroller/settitle%28_%29.md)
  Sets the title of the panel when not run as a sheet.
### Type Methods
- [class func deviceSelector() -> IOBluetoothDeviceSelectorController!](./iobluetoothdeviceselectorcontroller/deviceselector%28%29.md)

## Relationships

### Inherits From
- [NSWindowController](../AppKit/nswindowcontroller.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSeguePerforming](../AppKit/nssegueperforming.md)
- [NSStandardKeyBindingResponding](../AppKit/nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](../AppKit/nstouchbarprovider.md)
- [NSUserActivityRestoring](../AppKit/nsuseractivityrestoring.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Classes
- [class IOBluetoothAccessibilityIgnoredImageCell](./iobluetoothaccessibilityignoredimagecell.md)
- [class IOBluetoothAccessibilityIgnoredTextFieldCell](./iobluetoothaccessibilityignoredtextfieldcell.md)
- [class IOBluetoothDeviceSelectorControllerRef](./iobluetoothdeviceselectorcontrollerref.md)
- [class IOBluetoothObjectPushUIController](./iobluetoothobjectpushuicontroller.md)
  An NSWindowController subclass that supports the creation of an IOBluetoothObjectPushUIController object.
- [class IOBluetoothPairingController](./iobluetoothpairingcontroller.md)
  A NSWindowController subclass to display a window to initiate pairing to other bluetooth devices.
- [class IOBluetoothPairingControllerRef](./iobluetoothpairingcontrollerref.md)
- [class IOBluetoothPasskeyDisplay](./iobluetoothpasskeydisplay.md)
- [class IOBluetoothServiceBrowserController](./iobluetoothservicebrowsercontroller.md)
  A NSWindowController subclass to display a window to search for and perform SDP queries on bluetooth devices within range.
- [class IOBluetoothServiceBrowserControllerRef](./iobluetoothservicebrowsercontrollerref.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetoothui/iobluetoothdeviceselectorcontroller)*