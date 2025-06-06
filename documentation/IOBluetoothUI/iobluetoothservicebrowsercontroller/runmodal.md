# runModal()

**Framework**: IOBluetooth UI  
**Kind**: method

Runs the service browser panel in a modal session to allow the user to select a service on a Bluetooth device.

**Availability**:
- macOS 10.2+

## Declaration

```swift
@MainActor
func runModal() -> Int32
```

#### Return Value

Returns kIOBluetoothUISuccess if a successful, validated service selection was made by the user. Returns kIOBluetoothUIUserCanceledErr if the user cancelled the panel. These return values are the same as NSRunStoppedResponse and NSRunAbortedResponse respectively. They are the standard values used in a modal session.

#### Discussion

The controller will use the panel attributes to filter what devices the user sees. The allowed UUIDs will be used to validate the selection the user makes. The user will only be able to select services that match the allowed UUIDs. Only when a selection has been validated (or the panel cancelled), will this method return.

NOTE: This method is only available in macOS 10.2.4 (Bluetooth v1.1) or later.

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
- [func getPrompt() -> String!](iobluetoothservicebrowsercontroller/getprompt.md)
  Returns the title of the default/select button in the device selector panel.
- [func getRef() -> Unmanaged<IOBluetoothServiceBrowserControllerRef>!](iobluetoothservicebrowsercontroller/getref.md)
  Returns an IOBluetoothServiceBrowserControllerRef representation of the target IOBluetoothServiceBrowserController object.
- [func getResults() -> [Any]!](iobluetoothservicebrowsercontroller/getresults.md)
  Returns the result of the user’s selection.
- [func getSearchAttributes() -> UnsafePointer<IOBluetoothDeviceSearchAttributes>!](iobluetoothservicebrowsercontroller/getsearchattributes.md)
  Returns the search attributes that control the panel’s search/inquiry behavior.
- [func getTitle() -> String!](iobluetoothservicebrowsercontroller/gettitle.md)
  Returns the title of the device selector panel.
- [func setDescriptionText(String!)](iobluetoothservicebrowsercontroller/setdescriptiontext(_:).md)
  Sets the description text that appears in the device selector panel.
- [func setOptions(IOBluetoothServiceBrowserControllerOptions)](iobluetoothservicebrowsercontroller/setoptions(_:).md)
  Modify the options for the window controller.
- [func setPrompt(String!)](iobluetoothservicebrowsercontroller/setprompt(_:).md)
  Sets the title of the default/select button in the device selector panel.
- [func setSearchAttributes(UnsafePointer<IOBluetoothDeviceSearchAttributes>!)](iobluetoothservicebrowsercontroller/setsearchattributes(_:).md)
  Sets the search attributes that control the panel’s search/inquiry behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetoothui/iobluetoothservicebrowsercontroller/runmodal())*