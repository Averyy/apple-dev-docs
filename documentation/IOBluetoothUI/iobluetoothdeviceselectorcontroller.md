# IOBluetoothDeviceSelectorController

**Framework**: IOBluetooth UI  
**Kind**: class

A NSWindowController subclass to display a window to initiate pairing to other bluetooth devices.

**Availability**:
- macOS 10.2+

## Declaration

```swift
@MainActor
class IOBluetoothDeviceSelectorController
```

#### Overview

Implementation of a window controller to return a NSArray of selected bluetooth devices. This class will handle connecting to the Bluetooth Daemon for the purposes of searches, and displaying the results. This controller will return a NSArray of IOBluetoothDevice objects to the user.

## Topics

### Instance Methods
- [func addAllowedUUID(IOBluetoothSDPUUID!)](iobluetoothdeviceselectorcontroller/addalloweduuid(_:).md)
  Adds a UUID to the list of UUIDs that are used to validate the user’s selection.
- [func addAllowedUUIDArray([Any]!)](iobluetoothdeviceselectorcontroller/addalloweduuidarray(_:).md)
  Adds an array of UUIDs to the list of UUIDs that are used to validate the user’s selection.
- [func beginSheetModal(for: NSWindow!, modalDelegate: Any!, didEnd: Selector!, contextInfo: UnsafeMutableRawPointer!) -> IOReturn](iobluetoothdeviceselectorcontroller/beginsheetmodal(for:modaldelegate:didend:contextinfo:).md)
  Runs the device selector panel as a sheet on the target window.
- [func clearAllowedUUIDs()](iobluetoothdeviceselectorcontroller/clearalloweduuids.md)
  Resets the controller back to the default state where it will accept any device the user selects.
- [func getCancel() -> String!](iobluetoothdeviceselectorcontroller/getcancel.md)
  Returns the title of the default/cancel button in the device selector panel.
- [func getDescriptionText() -> String!](iobluetoothdeviceselectorcontroller/getdescriptiontext.md)
  Returns the description text that appears in the device selector panel.
- [func getHeader() -> String!](iobluetoothdeviceselectorcontroller/getheader.md)
  Returns the header text that appears in the device selector panel.
- [func getOptions() -> IOBluetoothServiceBrowserControllerOptions](iobluetoothdeviceselectorcontroller/getoptions.md)
  Returns the option bits that control the panel’s behavior.
- [func getPrompt() -> String!](iobluetoothdeviceselectorcontroller/getprompt.md)
  Returns the title of the default/select button in the device selector panel.
- [func getResults() -> [Any]!](iobluetoothdeviceselectorcontroller/getresults.md)
  Returns the result of the user’s selection.
- [func getSearchAttributes() -> UnsafePointer<IOBluetoothDeviceSearchAttributes>!](iobluetoothdeviceselectorcontroller/getsearchattributes.md)
  Returns the search attributes that control the panel’s search/inquiry behavior.
- [func getTitle() -> String!](iobluetoothdeviceselectorcontroller/gettitle.md)
  Returns the title of the device selector panel.
- [func runModal() -> Int32](iobluetoothdeviceselectorcontroller/runmodal.md)
  Runs the device selector panel in a modal session to allow the user to select a Bluetooth device.
- [func setCancel(String!)](iobluetoothdeviceselectorcontroller/setcancel(_:).md)
  Sets the title of the default/cancel button in the device selector panel.
- [func setDescriptionText(String!)](iobluetoothdeviceselectorcontroller/setdescriptiontext(_:).md)
  Sets the description text that appears in the device selector panel.
- [func setHeader(String!)](iobluetoothdeviceselectorcontroller/setheader(_:).md)
  Sets the header text that appears in the device selector panel.
- [func setOptions(IOBluetoothServiceBrowserControllerOptions)](iobluetoothdeviceselectorcontroller/setoptions(_:).md)
  Sets the option bits that control the panel’s behavior.
- [func setPrompt(String!)](iobluetoothdeviceselectorcontroller/setprompt(_:).md)
  Sets the title of the default/select button in the device selector panel.
- [func setSearchAttributes(UnsafePointer<IOBluetoothDeviceSearchAttributes>!)](iobluetoothdeviceselectorcontroller/setsearchattributes(_:).md)
  Sets the search attributes that control the panel’s search/inquiry behavior.
- [func setTitle(String!)](iobluetoothdeviceselectorcontroller/settitle(_:).md)
  Sets the title of the panel when not run as a sheet.
### Type Methods
- [class func deviceSelector() -> IOBluetoothDeviceSelectorController!](iobluetoothdeviceselectorcontroller/deviceselector.md)

## Relationships

### Inherits From
- [NSWindowController](../AppKit/NSWindowController.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSeguePerforming](../AppKit/NSSeguePerforming.md)
- [NSStandardKeyBindingResponding](../AppKit/NSStandardKeyBindingResponding.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [NSUserActivityRestoring](../AppKit/NSUserActivityRestoring.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class IOBluetoothAccessibilityIgnoredImageCell](iobluetoothaccessibilityignoredimagecell.md)
- [class IOBluetoothAccessibilityIgnoredTextFieldCell](iobluetoothaccessibilityignoredtextfieldcell.md)
- [class IOBluetoothDeviceSelectorControllerRef](iobluetoothdeviceselectorcontrollerref.md)
- [class IOBluetoothObjectPushUIController](iobluetoothobjectpushuicontroller.md)
  An NSWindowController subclass that supports the creation of an IOBluetoothObjectPushUIController object.
- [class IOBluetoothPairingController](iobluetoothpairingcontroller.md)
  A NSWindowController subclass to display a window to initiate pairing to other bluetooth devices.
- [class IOBluetoothPairingControllerRef](iobluetoothpairingcontrollerref.md)
- [class IOBluetoothPasskeyDisplay](iobluetoothpasskeydisplay.md)
- [class IOBluetoothServiceBrowserController](iobluetoothservicebrowsercontroller.md)
  A NSWindowController subclass to display a window to search for and perform SDP queries on bluetooth devices within range.
- [class IOBluetoothServiceBrowserControllerRef](iobluetoothservicebrowsercontrollerref.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetoothui/iobluetoothdeviceselectorcontroller)*