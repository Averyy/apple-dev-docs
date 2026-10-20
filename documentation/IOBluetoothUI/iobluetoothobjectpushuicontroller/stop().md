# stop()

**Framework**: IOBluetooth UI  
**Kind**: method  
**Role**: Instance Method

Stops the transfer UI

**Availability**:
- macOS 10.2+

## Declaration

```swift
func stop()
```

```objc
- (void) stop;
```

#### Discussion

Returns immediately. The object will callback over the delegate method (above) when the transfer is completed, or will release itself if no delegate is set.

## See Also

### Instance Methods
- [func beginSheetModal(for: NSWindow!, modalDelegate: Any!, didEnd: Selector!, contextInfo: UnsafeMutableRawPointer!) -> IOReturn](./beginsheetmodal%28for,modaldelegate,didend,contextinfo%29.md)
  Runs the transfer UI as a sheet on the target window.
- [func getDevice() -> IOBluetoothDevice!](./getdevice%28%29.md)
  Gets the object representing the remote target device in the transfer.
- [func getTitle() -> String!](./gettitle%28%29.md)
  Returns the title of the transfer panel.
- [func isTransferInProgress() -> Bool](./istransferinprogress%28%29.md)
  Gets state of the transfer
- [func runModal()](./runmodal%28%29.md)
  Runs the transfer UI panel in a modal session
- [func runPanel()](./runpanel%28%29.md)
  Runs the transfer UI as a panel with no modal session
- [func setIconImage(NSImage!)](./seticonimage%28_%29.md)
  Manually sets the icon used in the panel.
- [func setTitle(String!)](./settitle%28_%29.md)
  Sets the title of the panel when not run as a sheet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetoothui/iobluetoothobjectpushuicontroller/stop())*