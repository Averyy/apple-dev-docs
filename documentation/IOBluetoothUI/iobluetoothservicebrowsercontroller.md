# IOBluetoothServiceBrowserController

**Framework**: IOBluetooth UI  
**Kind**: class  
**Role**: Class

A NSWindowController subclass to display a window to search for and perform SDP queries on bluetooth devices within range.

**Availability**:
- macOS 10.2+

## Declaration

```swift
class IOBluetoothServiceBrowserController
```

```objc
@interface IOBluetoothServiceBrowserController : NSWindowController
```

#### Overview

This NSWindowController subclass will bring up a generic Bluetooth search and SDP browsing window allowing the user to find devices within range, perform SDP queries on a particular device, and select a SDP service to connect to. The client application can provide NSArrays of valid service UUIDs to allow, and an NSArray of valid device types to allow. The device type filter is not yet implemented.

## Topics

### Initializers
- [init!(IOBluetoothServiceBrowserControllerOptions)](./iobluetoothservicebrowsercontroller/init%28_%29.md)
  Allocator work Bluetooth Service Browser window controller.
### Instance Methods
- [func addAllowedUUID(IOBluetoothSDPUUID!)](./iobluetoothservicebrowsercontroller/addalloweduuid%28_%29.md)
  Adds a UUID to the list of UUIDs that are used to validate the user’s selection.
- [func addAllowedUUIDArray([Any]!)](./iobluetoothservicebrowsercontroller/addalloweduuidarray%28_%29.md)
  Adds an array of UUIDs to the list of UUIDs that are used to validate the user’s selection.
- [func beginSheetModal(for: NSWindow!, modalDelegate: Any!, didEnd: Selector!, contextInfo: UnsafeMutableRawPointer!) -> IOReturn](./iobluetoothservicebrowsercontroller/beginsheetmodal%28for,modaldelegate,didend,contextinfo%29.md)
  Runs the service browser panel as a sheet on the target window.
- [func clearAllowedUUIDs()](./iobluetoothservicebrowsercontroller/clearalloweduuids%28%29.md)
  Resets the controller back to the default state where it will accept any device the user selects.
- [func getDescriptionText() -> String!](./iobluetoothservicebrowsercontroller/getdescriptiontext%28%29.md)
  Returns the description text that appears in the device selector panel.
- [func getOptions() -> IOBluetoothServiceBrowserControllerOptions](./iobluetoothservicebrowsercontroller/getoptions%28%29.md)
  Returns the option bits that control the panel’s behavior.
- [func getPrompt() -> String!](./iobluetoothservicebrowsercontroller/getprompt%28%29.md)
  Returns the title of the default/select button in the device selector panel.
- [func getRef() -> Unmanaged<IOBluetoothServiceBrowserControllerRef>!](./iobluetoothservicebrowsercontroller/getref%28%29.md)
  Returns an IOBluetoothServiceBrowserControllerRef representation of the target IOBluetoothServiceBrowserController object.
- [func getResults() -> [Any]!](./iobluetoothservicebrowsercontroller/getresults%28%29.md)
  Returns the result of the user’s selection.
- [func getSearchAttributes() -> UnsafePointer<IOBluetoothDeviceSearchAttributes>!](./iobluetoothservicebrowsercontroller/getsearchattributes%28%29.md)
  Returns the search attributes that control the panel’s search/inquiry behavior.
- [func getTitle() -> String!](./iobluetoothservicebrowsercontroller/gettitle%28%29.md)
  Returns the title of the device selector panel.
- [func runModal() -> Int32](./iobluetoothservicebrowsercontroller/runmodal%28%29.md)
  Runs the service browser panel in a modal session to allow the user to select a service on a Bluetooth device.
- [func setDescriptionText(String!)](./iobluetoothservicebrowsercontroller/setdescriptiontext%28_%29.md)
  Sets the description text that appears in the device selector panel.
- [func setOptions(IOBluetoothServiceBrowserControllerOptions)](./iobluetoothservicebrowsercontroller/setoptions%28_%29.md)
  Modify the options for the window controller.
- [func setPrompt(String!)](./iobluetoothservicebrowsercontroller/setprompt%28_%29.md)
  Sets the title of the default/select button in the device selector panel.
- [func setSearchAttributes(UnsafePointer<IOBluetoothDeviceSearchAttributes>!)](./iobluetoothservicebrowsercontroller/setsearchattributes%28_%29.md)
  Sets the search attributes that control the panel’s search/inquiry behavior.
- [func setTitle(String!)](./iobluetoothservicebrowsercontroller/settitle%28_%29.md)
  Sets the title of the panel when not run as a sheet.
- [- discover:](./iobluetoothservicebrowsercontroller/discover_.md)
  Invoke an already created window controller to display, and run the modal dialog.
- [- discoverAsSheetForWindow:withRecord:](./iobluetoothservicebrowsercontroller/discoverassheetforwindow_withrecord_.md)
  Invoke an already created window controller to display, and run the modal dialog.
- [- discoverWithDeviceAttributes:serviceList:serviceRecord:](./iobluetoothservicebrowsercontroller/discoverwithdeviceattributes_servicelist_servicerecord_.md)
  Invoke an already created window controller to display, and run the modal dialog.
### Type Methods
- [class func withServiceBrowserControllerRef(IOBluetoothServiceBrowserControllerRef!) -> IOBluetoothServiceBrowserController!](./iobluetoothservicebrowsercontroller/withservicebrowsercontrollerref%28_%29.md)
  Method call to convert an IOBluetoothServiceBrowserControllerRef into an IOBluetoothServiceBrowserController *.
- [+ browseDevices:options:](./iobluetoothservicebrowsercontroller/browsedevices_options_.md)
- [+ browseDevicesAsSheetForWindow:options:window:](./iobluetoothservicebrowsercontroller/browsedevicesassheetforwindow_options_window_.md)

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
- [class IOBluetoothDeviceSelectorController](./iobluetoothdeviceselectorcontroller.md)
  A NSWindowController subclass to display a window to initiate pairing to other bluetooth devices.
- [class IOBluetoothDeviceSelectorControllerRef](./iobluetoothdeviceselectorcontrollerref.md)
- [class IOBluetoothObjectPushUIController](./iobluetoothobjectpushuicontroller.md)
  An NSWindowController subclass that supports the creation of an IOBluetoothObjectPushUIController object.
- [class IOBluetoothPairingController](./iobluetoothpairingcontroller.md)
  A NSWindowController subclass to display a window to initiate pairing to other bluetooth devices.
- [class IOBluetoothPairingControllerRef](./iobluetoothpairingcontrollerref.md)
- [class IOBluetoothPasskeyDisplay](./iobluetoothpasskeydisplay.md)
- [class IOBluetoothServiceBrowserControllerRef](./iobluetoothservicebrowsercontrollerref.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetoothui/iobluetoothservicebrowsercontroller)*