# setIconImage(_:)

**Framework**: IOBluetooth UI  
**Kind**: method

Manually sets the icon used in the panel.

**Availability**:
- macOS 10.2+

## Declaration

```swift
@MainActor
func setIconImage(_ image: NSImage!)
```

#### Discussion

The panel icon should be set to the icon of the calling application. If not set, the panel will try to load up the correct icon for the target device, and will default to the icon of the running application on fail.

## Parameters

- `image`: Image to use as the icon.

## See Also

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
- [func setTitle(String!)](iobluetoothobjectpushuicontroller/settitle(_:).md)
  Sets the title of the panel when not run as a sheet.
- [func stop()](iobluetoothobjectpushuicontroller/stop.md)
  Stops the transfer UI


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetoothui/iobluetoothobjectpushuicontroller/seticonimage(_:))*