# IOBluetoothObjectPushUIController

**Framework**: IOBluetooth UI  
**Kind**: class

An NSWindowController subclass that supports the creation of an IOBluetoothObjectPushUIController object.

**Availability**:
- macOS 10.2+

## Declaration

```swift
@MainActor
class IOBluetoothObjectPushUIController
```

## Topics

### Initializers
- [init!(objectPushWith: IOBluetoothDevice!, withFiles: [Any]!, delegate: Any!)](iobluetoothobjectpushuicontroller/init(objectpushwith:withfiles:delegate:).md)
  Creates and returns a new IOBluetoothObjectPush object
### Instance Methods
- [func beginSheetModal(for: NSWindow!, modalDelegate: Any!, didEnd: Selector!, contextInfo: UnsafeMutableRawPointer!) -> IOReturn](iobluetoothobjectpushuicontroller/beginsheetmodal(for:modaldelegate:didend:contextinfo:).md)
  Runs the transfer UI as a sheet on the target window.
- [func getDevice() -> IOBluetoothDevice!](iobluetoothobjectpushuicontroller/getdevice.md)
  Gets the object representing the remote target device in the transfer.
- [func getTitle() -> String!](iobluetoothobjectpushuicontroller/gettitle.md)
  Returns the title of the transfer panel.
- [func isTransferInProgress() -> Bool](iobluetoothobjectpushuicontroller/istransferinprogress.md)
  Gets state of the transfer
- [func runModal()](iobluetoothobjectpushuicontroller/runmodal.md)
  Runs the transfer UI panel in a modal session
- [func runPanel()](iobluetoothobjectpushuicontroller/runpanel.md)
  Runs the transfer UI as a panel with no modal session
- [func setIconImage(NSImage!)](iobluetoothobjectpushuicontroller/seticonimage(_:).md)
  Manually sets the icon used in the panel.
- [func setTitle(String!)](iobluetoothobjectpushuicontroller/settitle(_:).md)
  Sets the title of the panel when not run as a sheet.
- [func stop()](iobluetoothobjectpushuicontroller/stop.md)
  Stops the transfer UI

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
- [class IOBluetoothDeviceSelectorController](iobluetoothdeviceselectorcontroller.md)
  A NSWindowController subclass to display a window to initiate pairing to other bluetooth devices.
- [class IOBluetoothDeviceSelectorControllerRef](iobluetoothdeviceselectorcontrollerref.md)
- [class IOBluetoothPairingController](iobluetoothpairingcontroller.md)
  A NSWindowController subclass to display a window to initiate pairing to other bluetooth devices.
- [class IOBluetoothPairingControllerRef](iobluetoothpairingcontrollerref.md)
- [class IOBluetoothPasskeyDisplay](iobluetoothpasskeydisplay.md)
- [class IOBluetoothServiceBrowserController](iobluetoothservicebrowsercontroller.md)
  A NSWindowController subclass to display a window to search for and perform SDP queries on bluetooth devices within range.
- [class IOBluetoothServiceBrowserControllerRef](iobluetoothservicebrowsercontrollerref.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetoothui/iobluetoothobjectpushuicontroller)*