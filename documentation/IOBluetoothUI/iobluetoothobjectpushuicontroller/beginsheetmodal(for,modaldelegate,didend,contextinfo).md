# beginSheetModal(for:modalDelegate:didEnd:contextInfo:)

**Framework**: IOBluetooth UI  
**Kind**: method  
**Role**: Instance Method

Runs the transfer UI as a sheet on the target window.

**Availability**:
- macOS 10.2+

## Declaration

```swift
func beginSheetModal(for sheetWindow: NSWindow!, modalDelegate: Any!, didEnd didEndSelector: Selector!, contextInfo: UnsafeMutableRawPointer!) -> IOReturn
```

```objc
- (IOReturn) beginSheetModalForWindow:(NSWindow *) sheetWindow modalDelegate:(id) modalDelegate didEndSelector:(SEL) didEndSelector contextInfo:(void *) contextInfo;
```

#### Return Value

Returns kIOReturnSuccess if the sheet modal session was started.

#### Discussion

This function works the same way as -[NSApplication beginSheet:modalForWindow:modalDelegate:didEndSelector:contextInfo:]. The didEndSelector has a similar prototype as in NSApplication except that the first argument is the IOBluetoothDeviceSelectorController object instead of the window:

-(void)sheetDidEnd:(IOBluetoothDeviceSelectorController *)controller returnCode:(int)returnCode contextInfo:(void *)contextInfo. The returnCode parameter will either be kIOBluetoothUISuccess or kIOBluetoothUIUserCancelledErr as described in -runModal.

## Parameters

- `sheetWindow`: NSWindow to attach the device selector panel to as a sheet.
- `modalDelegate`: Delegate object that gets sent the didEndSelector when the sheet modal session is finished.
- `didEndSelector`: Selector sent to the modalDelegate when the sheet modal session is finished.
- `contextInfo`: User-definied value passed to the modalDelegate in the didEndSelector.

## See Also

### Instance Methods
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
- [func stop()](./stop%28%29.md)
  Stops the transfer UI


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetoothui/iobluetoothobjectpushuicontroller/beginsheetmodal(for:modaldelegate:didend:contextinfo:))*