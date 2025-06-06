# getPrompt()

**Framework**: IOBluetooth UI  
**Kind**: method

Returns the title of the default/select button in the device selector panel.

**Availability**:
- macOS 10.2+

## Declaration

```swift
@MainActor
func getPrompt() -> String!
```

#### Return Value

Returns the default button title of the device selector panel.

## See Also

- [func addAllowedUUID(IOBluetoothSDPUUID!)](iobluetoothservicebrowsercontroller/addalloweduuid(_:).md)
  Adds a UUID to the list of UUIDs that are used to validate the user’s selection.
- [func addAllowedUUIDArray([Any]!)](iobluetoothservicebrowsercontroller/addalloweduuidarray(_:).md)
  Adds an array of UUIDs to the list of UUIDs that are used to validate the user’s selection.
- [func beginSheetModal(for: NSWindow!, modalDelegate: Any!, didEnd: Selector!, contextInfo: UnsafeMutableRawPointer!) -> IOReturn](iobluetoothservicebrowsercontroller/beginsheetmodal(for:modaldelegate:didend:contextinfo:).md)
  Runs the service browser panel as a sheet on the target window.
- [func clearAllowedUUIDs()](iobluetoothservicebrowsercontroller/clearalloweduuids.md)
  Resets the controller back to the default state where it will accept any device the user selects.
- [func getDescriptionText() -> String!](iobluetoothservicebrowsercontroller/getdescriptiontext.md)
  Returns the description text that appears in the device selector panel.
- [func getOptions() -> IOBluetoothServiceBrowserControllerOptions](iobluetoothservicebrowsercontroller/getoptions.md)
  Returns the option bits that control the panel’s behavior.
- [func getRef() -> Unmanaged<IOBluetoothServiceBrowserControllerRef>!](iobluetoothservicebrowsercontroller/getref.md)
  Returns an IOBluetoothServiceBrowserControllerRef representation of the target IOBluetoothServiceBrowserController object.
- [func getResults() -> [Any]!](iobluetoothservicebrowsercontroller/getresults.md)
  Returns the result of the user’s selection.
- [func getSearchAttributes() -> UnsafePointer<IOBluetoothDeviceSearchAttributes>!](iobluetoothservicebrowsercontroller/getsearchattributes.md)
  Returns the search attributes that control the panel’s search/inquiry behavior.
- [func getTitle() -> String!](iobluetoothservicebrowsercontroller/gettitle.md)
  Returns the title of the device selector panel.
- [func runModal() -> Int32](iobluetoothservicebrowsercontroller/runmodal.md)
  Runs the service browser panel in a modal session to allow the user to select a service on a Bluetooth device.
- [func setDescriptionText(String!)](iobluetoothservicebrowsercontroller/setdescriptiontext(_:).md)
  Sets the description text that appears in the device selector panel.
- [func setOptions(IOBluetoothServiceBrowserControllerOptions)](iobluetoothservicebrowsercontroller/setoptions(_:).md)
  Modify the options for the window controller.
- [func setPrompt(String!)](iobluetoothservicebrowsercontroller/setprompt(_:).md)
  Sets the title of the default/select button in the device selector panel.
- [func setSearchAttributes(UnsafePointer<IOBluetoothDeviceSearchAttributes>!)](iobluetoothservicebrowsercontroller/setsearchattributes(_:).md)
  Sets the search attributes that control the panel’s search/inquiry behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetoothui/iobluetoothservicebrowsercontroller/getprompt())*