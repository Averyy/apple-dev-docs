# isTransferInProgress()

**Framework**: IOBluetooth UI  
**Kind**: method

Gets state of the transfer

**Availability**:
- macOS 10.2+

## Declaration

```swift
@MainActor
func isTransferInProgress() -> Bool
```

#### Return Value

The state of the transfer

## See Also

- [func beginSheetModal(for: NSWindow!, modalDelegate: Any!, didEnd: Selector!, contextInfo: UnsafeMutableRawPointer!) -> IOReturn](iobluetoothobjectpushuicontroller/beginsheetmodal(for:modaldelegate:didend:contextinfo:).md)
  Runs the transfer UI as a sheet on the target window.
- [func getDevice() -> IOBluetoothDevice!](iobluetoothobjectpushuicontroller/getdevice.md)
  Gets the object representing the remote target device in the transfer.
- [func getTitle() -> String!](iobluetoothobjectpushuicontroller/gettitle.md)
  Returns the title of the transfer panel.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetoothui/iobluetoothobjectpushuicontroller/istransferinprogress())*