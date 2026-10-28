# beginSheetModal(for:modalDelegate:didEnd:contextInfo:)

**Framework**: IOBluetooth UI  
**Kind**: method  
**Role**: Instance Method

Runs the service browser panel as a sheet on the target window.

**Availability**:
- macOS 10.2+

## Declaration

```swift
func beginSheetModal(for sheetWindow: NSWindow!, modalDelegate: Any!, didEnd didEndSelector: Selector!, contextInfo: UnsafeMutableRawPointer!) -> IOReturn
```

```objc
- (IOReturn) beginSheetModalForWindow:(NSWindow *) sheetWindow modalDelegate:(id) modalDelegate didEndSelector:(SEL) didEndSelector contextInfo:(void *) contextInfo;
```

## Return Value

Returns kIOReturnSuccess if the sheet modal session was started.

## Discussion

This function works the same way as -[NSApplication beginSheet:modalForWindow:modalDelegate:didEndSelector:contextInfo:]. The didEndSelector has a similar prototype as in NSApplication except that the first argument is the IOBluetoothServiceBrowserController object instead of the window: -(void)sheetDidEnd:(IOBluetoothServiceBrowserController *)controller returnCode:(int)returnCode contextInfo:(void *)contextInfo. The returnCode parameter will either be kIOBluetoothUISuccess or kIOBluetoothUIUserCancelledErr as described in -runModal.

NOTE: This method is only available in macOS 10.2.4 (Bluetooth v1.1) or later.

## Parameters

- `sheetWindow`: NSWindow to attach the service browser panel to as a sheet.
- `modalDelegate`: Delegate object that gets sent the didEndSelector when the sheet modal session is finished.
- `didEndSelector`: Selector sent to the modalDelegate when the sheet modal session is finished.
- `contextInfo`: User-definied value passed to the modalDelegate in the didEndSelector.

## See Also

### Instance Methods
- [func addAllowedUUID(IOBluetoothSDPUUID!)](./addalloweduuid%28_%29.md)
  Adds a UUID to the list of UUIDs that are used to validate the user’s selection.
- [func addAllowedUUIDArray([Any]!)](./addalloweduuidarray%28_%29.md)
  Adds an array of UUIDs to the list of UUIDs that are used to validate the user’s selection.
- [func clearAllowedUUIDs()](./clearalloweduuids%28%29.md)
  Resets the controller back to the default state where it will accept any device the user selects.
- [func getDescriptionText() -> String!](./getdescriptiontext%28%29.md)
  Returns the description text that appears in the device selector panel.
- [func getOptions() -> IOBluetoothServiceBrowserControllerOptions](./getoptions%28%29.md)
  Returns the option bits that control the panel’s behavior.
- [func getPrompt() -> String!](./getprompt%28%29.md)
  Returns the title of the default/select button in the device selector panel.
- [func getRef() -> Unmanaged<IOBluetoothServiceBrowserControllerRef>!](./getref%28%29.md)
  Returns an IOBluetoothServiceBrowserControllerRef representation of the target IOBluetoothServiceBrowserController object.
- [func getResults() -> [Any]!](./getresults%28%29.md)
  Returns the result of the user’s selection.
- [func getSearchAttributes() -> UnsafePointer<IOBluetoothDeviceSearchAttributes>!](./getsearchattributes%28%29.md)
  Returns the search attributes that control the panel’s search/inquiry behavior.
- [func getTitle() -> String!](./gettitle%28%29.md)
  Returns the title of the device selector panel.
- [func runModal() -> Int32](./runmodal%28%29.md)
  Runs the service browser panel in a modal session to allow the user to select a service on a Bluetooth device.
- [func setDescriptionText(String!)](./setdescriptiontext%28_%29.md)
  Sets the description text that appears in the device selector panel.
- [func setOptions(IOBluetoothServiceBrowserControllerOptions)](./setoptions%28_%29.md)
  Modify the options for the window controller.
- [func setPrompt(String!)](./setprompt%28_%29.md)
  Sets the title of the default/select button in the device selector panel.
- [func setSearchAttributes(UnsafePointer<IOBluetoothDeviceSearchAttributes>!)](./setsearchattributes%28_%29.md)
  Sets the search attributes that control the panel’s search/inquiry behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetoothui/iobluetoothservicebrowsercontroller/beginsheetmodal(for:modaldelegate:didend:contextinfo:))*