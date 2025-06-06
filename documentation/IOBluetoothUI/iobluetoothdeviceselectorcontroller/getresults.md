# getResults()

**Framework**: IOBluetooth UI  
**Kind**: method

Returns the result of the user’s selection.

**Availability**:
- macOS 10.2+

## Declaration

```swift
@MainActor
func getResults() -> [Any]!
```

#### Return Value

Returns an NSArray of IOBluetoothDevice objects corresponding to the user’s selection. If the user cancelled the panel, nil will be returned.

#### Discussion

There will only be results if the panel has been run, the user has successfully made a selection and that selection has been validated. If kIOBluetoothUISuccess was returned for the session, there should be valid results. Currently only a single device is allowed to be selected, so the results array will only contain one object. However in the future multiple selection will be supported.

NOTE: This method is only available in macOS 10.2.4 (Bluetooth v1.1) or later.

## See Also

- [func addAllowedUUID(IOBluetoothSDPUUID!)](iobluetoothdeviceselectorcontroller/addalloweduuid(_:).md)
  Adds a UUID to the list of UUIDs that are used to validate the user’s selection.
- [func addAllowedUUIDArray([Any]!)](iobluetoothdeviceselectorcontroller/addalloweduuidarray(_:).md)
  Adds an array of UUIDs to the list of UUIDs that are used to validate the user’s selection.
- [func beginSheetModal(for: NSWindow!, modalDelegate: Any!, didEnd: Selector!, contextInfo: UnsafeMutableRawPointer!) -> IOReturn](iobluetoothdeviceselectorcontroller/beginsheetmodal(for:modaldelegate:didend:contextinfo:).md)
  Runs the device selector panel as a sheet on the target window.
- [func clearAllowedUUIDs()](iobluetoothdeviceselectorcontroller/clearalloweduuids.md)
  Resets the controller back to the default state where it will accept any device the user selects.
- [func getCancel() -> String!](iobluetoothdeviceselectorcontroller/getcancel.md)
  Returns the title of the default/cancel button in the device selector panel.
- [func getDescriptionText() -> String!](iobluetoothdeviceselectorcontroller/getdescriptiontext.md)
  Returns the description text that appears in the device selector panel.
- [func getHeader() -> String!](iobluetoothdeviceselectorcontroller/getheader.md)
  Returns the header text that appears in the device selector panel.
- [func getOptions() -> IOBluetoothServiceBrowserControllerOptions](iobluetoothdeviceselectorcontroller/getoptions.md)
  Returns the option bits that control the panel’s behavior.
- [func getPrompt() -> String!](iobluetoothdeviceselectorcontroller/getprompt.md)
  Returns the title of the default/select button in the device selector panel.
- [func getSearchAttributes() -> UnsafePointer<IOBluetoothDeviceSearchAttributes>!](iobluetoothdeviceselectorcontroller/getsearchattributes.md)
  Returns the search attributes that control the panel’s search/inquiry behavior.
- [func getTitle() -> String!](iobluetoothdeviceselectorcontroller/gettitle.md)
  Returns the title of the device selector panel.
- [func runModal() -> Int32](iobluetoothdeviceselectorcontroller/runmodal.md)
  Runs the device selector panel in a modal session to allow the user to select a Bluetooth device.
- [func setCancel(String!)](iobluetoothdeviceselectorcontroller/setcancel(_:).md)
  Sets the title of the default/cancel button in the device selector panel.
- [func setDescriptionText(String!)](iobluetoothdeviceselectorcontroller/setdescriptiontext(_:).md)
  Sets the description text that appears in the device selector panel.
- [func setHeader(String!)](iobluetoothdeviceselectorcontroller/setheader(_:).md)
  Sets the header text that appears in the device selector panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetoothui/iobluetoothdeviceselectorcontroller/getresults())*