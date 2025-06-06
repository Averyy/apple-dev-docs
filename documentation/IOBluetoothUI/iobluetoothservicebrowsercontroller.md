# IOBluetoothServiceBrowserController

**Framework**: IOBluetooth UI  
**Kind**: class

A NSWindowController subclass to display a window to search for and perform SDP queries on bluetooth devices within range.

**Availability**:
- macOS 10.2+

## Declaration

```swift
@MainActor
class IOBluetoothServiceBrowserController
```

#### Overview

This NSWindowController subclass will bring up a generic Bluetooth search and SDP browsing window allowing the user to find devices within range, perform SDP queries on a particular device, and select a SDP service to connect to. The client application can provide NSArrays of valid service UUIDs to allow, and an NSArray of valid device types to allow. The device type filter is not yet implemented.

## Topics

### Initializers
- [init!(IOBluetoothServiceBrowserControllerOptions)](iobluetoothservicebrowsercontroller/init(_:).md)
  Allocator work Bluetooth Service Browser window controller.
### Instance Methods
- [func addAllowedUUID(IOBluetoothSDPUUID!)](iobluetoothservicebrowsercontroller/addalloweduuid(_:).md)
  Adds a UUID to the list of UUIDs that are used to validate the user’s selection.
- [func addAllowedUUIDArray([Any]!)](iobluetoothservicebrowsercontroller/addalloweduuidarray(_:).md)
  Adds an array of UUIDs to the list of UUIDs that are used to validate the user’s selection.
- [func beginSheetModal(for: NSWindow!, modalDelegate: Any!, didEnd: Selector!, contextInfo: UnsafeMutableRawPointer!) -> IOReturn](iobluetoothservicebrowsercontroller/beginsheetmodal(for:modaldelegate:didend:contextinfo:).md)
  Runs the service browser panel as a sheet on the target window.
- [func clearAllowedUUIDs()](iobluetoothservicebrowsercontroller/clearalloweduuids.md)
  Resets the controller back to the default state where it will accept any device the user selects.
- [func getDescriptionText() -> String!](iobluetoothservicebrowsercontroller/getdescriptiontext.md)
  Returns the description text that appears in the device selector panel.
- [func getOptions() -> IOBluetoothServiceBrowserControllerOptions](iobluetoothservicebrowsercontroller/getoptions.md)
  Returns the option bits that control the panel’s behavior.
- [func getPrompt() -> String!](iobluetoothservicebrowsercontroller/getprompt.md)
  Returns the title of the default/select button in the device selector panel.
- [func getRef() -> Unmanaged<IOBluetoothServiceBrowserControllerRef>!](iobluetoothservicebrowsercontroller/getref.md)
  Returns an IOBluetoothServiceBrowserControllerRef representation of the target IOBluetoothServiceBrowserController object.
- [func getResults() -> [Any]!](iobluetoothservicebrowsercontroller/getresults.md)
  Returns the result of the user’s selection.
- [func getSearchAttributes() -> UnsafePointer<IOBluetoothDeviceSearchAttributes>!](iobluetoothservicebrowsercontroller/getsearchattributes.md)
  Returns the search attributes that control the panel’s search/inquiry behavior.
- [func getTitle() -> String!](iobluetoothservicebrowsercontroller/gettitle.md)
  Returns the title of the device selector panel.
- [func runModal() -> Int32](iobluetoothservicebrowsercontroller/runmodal.md)
  Runs the service browser panel in a modal session to allow the user to select a service on a Bluetooth device.
- [func setDescriptionText(String!)](iobluetoothservicebrowsercontroller/setdescriptiontext(_:).md)
  Sets the description text that appears in the device selector panel.
- [func setOptions(IOBluetoothServiceBrowserControllerOptions)](iobluetoothservicebrowsercontroller/setoptions(_:).md)
  Modify the options for the window controller.
- [func setPrompt(String!)](iobluetoothservicebrowsercontroller/setprompt(_:).md)
  Sets the title of the default/select button in the device selector panel.
- [func setSearchAttributes(UnsafePointer<IOBluetoothDeviceSearchAttributes>!)](iobluetoothservicebrowsercontroller/setsearchattributes(_:).md)
  Sets the search attributes that control the panel’s search/inquiry behavior.
- [func setTitle(String!)](iobluetoothservicebrowsercontroller/settitle(_:).md)
  Sets the title of the panel when not run as a sheet.
### Type Methods
- [class func withServiceBrowserControllerRef(IOBluetoothServiceBrowserControllerRef!) -> IOBluetoothServiceBrowserController!](iobluetoothservicebrowsercontroller/withservicebrowsercontrollerref(_:).md)
  Method call to convert an IOBluetoothServiceBrowserControllerRef into an IOBluetoothServiceBrowserController *.

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

## See Also

- [class IOBluetoothAccessibilityIgnoredImageCell](iobluetoothaccessibilityignoredimagecell.md)
- [class IOBluetoothAccessibilityIgnoredTextFieldCell](iobluetoothaccessibilityignoredtextfieldcell.md)
- [class IOBluetoothDeviceSelectorController](iobluetoothdeviceselectorcontroller.md)
  A NSWindowController subclass to display a window to initiate pairing to other bluetooth devices.
- [class IOBluetoothDeviceSelectorControllerRef](iobluetoothdeviceselectorcontrollerref.md)
- [class IOBluetoothObjectPushUIController](iobluetoothobjectpushuicontroller.md)
  An NSWindowController subclass that supports the creation of an IOBluetoothObjectPushUIController object.
- [class IOBluetoothPairingController](iobluetoothpairingcontroller.md)
  A NSWindowController subclass to display a window to initiate pairing to other bluetooth devices.
- [class IOBluetoothPairingControllerRef](iobluetoothpairingcontrollerref.md)
- [class IOBluetoothPasskeyDisplay](iobluetoothpasskeydisplay.md)
- [class IOBluetoothServiceBrowserControllerRef](iobluetoothservicebrowsercontrollerref.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetoothui/iobluetoothservicebrowsercontroller)*