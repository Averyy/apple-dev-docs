# runModal()

**Framework**: IOBluetooth UI  
**Kind**: method

Runs the transfer UI panel in a modal session

**Availability**:
- macOS 10.2+

## Declaration

```swift
@MainActor
func runModal()
```

#### Discussion

Returns when the modal session has ended. This object will call back over the delegate method (above) when the transfer is complete. Users should release the object then. If no delegate is set the object will release itself.

## See Also

- [func beginSheetModal(for: NSWindow!, modalDelegate: Any!, didEnd: Selector!, contextInfo: UnsafeMutableRawPointer!) -> IOReturn](iobluetoothobjectpushuicontroller/beginsheetmodal(for:modaldelegate:didend:contextinfo:).md)
  Runs the transfer UI as a sheet on the target window.
- [func getDevice() -> IOBluetoothDevice!](iobluetoothobjectpushuicontroller/getdevice.md)
  Gets the object representing the remote target device in the transfer.
- [func getTitle() -> String!](iobluetoothobjectpushuicontroller/gettitle.md)
  Returns the title of the transfer panel.
- [func isTransferInProgress() -> Bool](iobluetoothobjectpushuicontroller/istransferinprogress.md)
  Gets state of the transfer
- [func runPanel()](iobluetoothobjectpushuicontroller/runpanel.md)
  Runs the transfer UI as a panel with no modal session
- [func setIconImage(NSImage!)](iobluetoothobjectpushuicontroller/seticonimage(_:).md)
  Manually sets the icon used in the panel.
- [func setTitle(String!)](iobluetoothobjectpushuicontroller/settitle(_:).md)
  Sets the title of the panel when not run as a sheet.
- [func stop()](iobluetoothobjectpushuicontroller/stop.md)
  Stops the transfer UI


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetoothui/iobluetoothobjectpushuicontroller/runmodal())*