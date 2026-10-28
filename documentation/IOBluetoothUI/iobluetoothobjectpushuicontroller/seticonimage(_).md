# setIconImage(_:)

**Framework**: IOBluetooth UI  
**Kind**: method  
**Role**: Instance Method

Manually sets the icon used in the panel.

**Availability**:
- macOS 10.2+

## Declaration

```swift
func setIconImage(_ image: NSImage!)
```

```objc
- (void) setIconImage:(NSImage *) image;
```

## Discussion

The panel icon should be set to the icon of the calling application. If not set, the panel will try to load up the correct icon for the target device, and will default to the icon of the running application on fail.

## Parameters

- `image`: Image to use as the icon.

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
- [func setTitle(String!)](./settitle%28_%29.md)
  Sets the title of the panel when not run as a sheet.
- [func stop()](./stop%28%29.md)
  Stops the transfer UI


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetoothui/iobluetoothobjectpushuicontroller/seticonimage(_:))*