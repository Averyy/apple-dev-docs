# runModal()

**Framework**: IOBluetooth UI  
**Kind**: method  
**Role**: Instance Method

Runs the device selector panel in a modal session to allow the user to select a Bluetooth device.

**Availability**:
- macOS 10.2+

## Declaration

```swift
func runModal() -> Int32
```

```objc
- (int) runModal;
```

#### Return Value

Returns kIOBluetoothUISuccess if a successful, validated device selection was made by the user. Returns kIOBluetoothUIUserCanceledErr if the user cancelled the panel. These return values are the same as NSRunStoppedResponse and NSRunAbortedResponse respectively. They are the standard values used in a modal session.

#### Discussion

The controller will use the panel attributes to filter what devices the user sees. The allowed UUIDs will be used to validate the selection the user makes. Only when a selection has been validated (or the panel cancelled), will this method return.

NOTE: This method is only available in macOS 10.2.4 (Bluetooth v1.1) or later.

## See Also

### Instance Methods
- [func addAllowedUUID(IOBluetoothSDPUUID!)](./addalloweduuid%28_%29.md)
  Adds a UUID to the list of UUIDs that are used to validate the user’s selection.
- [func addAllowedUUIDArray([Any]!)](./addalloweduuidarray%28_%29.md)
  Adds an array of UUIDs to the list of UUIDs that are used to validate the user’s selection.
- [func beginSheetModal(for: NSWindow!, modalDelegate: Any!, didEnd: Selector!, contextInfo: UnsafeMutableRawPointer!) -> IOReturn](./beginsheetmodal%28for,modaldelegate,didend,contextinfo%29.md)
  Runs the device selector panel as a sheet on the target window.
- [func clearAllowedUUIDs()](./clearalloweduuids%28%29.md)
  Resets the controller back to the default state where it will accept any device the user selects.
- [func getCancel() -> String!](./getcancel%28%29.md)
  Returns the title of the default/cancel button in the device selector panel.
- [func getDescriptionText() -> String!](./getdescriptiontext%28%29.md)
  Returns the description text that appears in the device selector panel.
- [func getHeader() -> String!](./getheader%28%29.md)
  Returns the header text that appears in the device selector panel.
- [func getOptions() -> IOBluetoothServiceBrowserControllerOptions](./getoptions%28%29.md)
  Returns the option bits that control the panel’s behavior.
- [func getPrompt() -> String!](./getprompt%28%29.md)
  Returns the title of the default/select button in the device selector panel.
- [func getResults() -> [Any]!](./getresults%28%29.md)
  Returns the result of the user’s selection.
- [func getSearchAttributes() -> UnsafePointer<IOBluetoothDeviceSearchAttributes>!](./getsearchattributes%28%29.md)
  Returns the search attributes that control the panel’s search/inquiry behavior.
- [func getTitle() -> String!](./gettitle%28%29.md)
  Returns the title of the device selector panel.
- [func setCancel(String!)](./setcancel%28_%29.md)
  Sets the title of the default/cancel button in the device selector panel.
- [func setDescriptionText(String!)](./setdescriptiontext%28_%29.md)
  Sets the description text that appears in the device selector panel.
- [func setHeader(String!)](./setheader%28_%29.md)
  Sets the header text that appears in the device selector panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetoothui/iobluetoothdeviceselectorcontroller/runmodal())*