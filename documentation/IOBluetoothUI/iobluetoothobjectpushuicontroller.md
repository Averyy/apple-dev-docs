# IOBluetoothObjectPushUIController

**Framework**: IOBluetooth UI  
**Kind**: class  
**Role**: Class

An NSWindowController subclass that supports the creation of an IOBluetoothObjectPushUIController object.

**Availability**:
- macOS 10.2+

## Declaration

```swift
class IOBluetoothObjectPushUIController
```

```objc
@interface IOBluetoothObjectPushUIController : NSWindowController
```

## Topics

### Initializers
- [init!(objectPushWith: IOBluetoothDevice!, withFiles: [Any]!, delegate: Any!)](./iobluetoothobjectpushuicontroller/init%28objectpushwith,withfiles,delegate%29.md)
  Creates and returns a new IOBluetoothObjectPush object
- [init!(objectPushWithBluetoothDevice: IOBluetoothDevice!, withFiles: [Any]!, delegate: Any!)](./iobluetoothobjectpushuicontroller/init%28objectpushwithbluetoothdevice,withfiles,delegate%29.md)
### Instance Methods
- [func beginSheetModal(for: NSWindow!, modalDelegate: Any!, didEnd: Selector!, contextInfo: UnsafeMutableRawPointer!) -> IOReturn](./iobluetoothobjectpushuicontroller/beginsheetmodal%28for,modaldelegate,didend,contextinfo%29.md)
  Runs the transfer UI as a sheet on the target window.
- [func getDevice() -> IOBluetoothDevice!](./iobluetoothobjectpushuicontroller/getdevice%28%29.md)
  Gets the object representing the remote target device in the transfer.
- [func getTitle() -> String!](./iobluetoothobjectpushuicontroller/gettitle%28%29.md)
  Returns the title of the transfer panel.
- [func isTransferInProgress() -> Bool](./iobluetoothobjectpushuicontroller/istransferinprogress%28%29.md)
  Gets state of the transfer
- [func runModal()](./iobluetoothobjectpushuicontroller/runmodal%28%29.md)
  Runs the transfer UI panel in a modal session
- [func runPanel()](./iobluetoothobjectpushuicontroller/runpanel%28%29.md)
  Runs the transfer UI as a panel with no modal session
- [func setIconImage(NSImage!)](./iobluetoothobjectpushuicontroller/seticonimage%28_%29.md)
  Manually sets the icon used in the panel.
- [func setTitle(String!)](./iobluetoothobjectpushuicontroller/settitle%28_%29.md)
  Sets the title of the panel when not run as a sheet.
- [func stop()](./iobluetoothobjectpushuicontroller/stop%28%29.md)
  Stops the transfer UI

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
- [class IOBluetoothPairingController](./iobluetoothpairingcontroller.md)
  A NSWindowController subclass to display a window to initiate pairing to other bluetooth devices.
- [class IOBluetoothPairingControllerRef](./iobluetoothpairingcontrollerref.md)
- [class IOBluetoothPasskeyDisplay](./iobluetoothpasskeydisplay.md)
- [class IOBluetoothServiceBrowserController](./iobluetoothservicebrowsercontroller.md)
  A NSWindowController subclass to display a window to search for and perform SDP queries on bluetooth devices within range.
- [class IOBluetoothServiceBrowserControllerRef](./iobluetoothservicebrowsercontrollerref.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetoothui/iobluetoothobjectpushuicontroller)*