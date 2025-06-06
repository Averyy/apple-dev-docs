# addAllowedUUIDArray(_:)

**Framework**: IOBluetooth UI  
**Kind**: method

Adds an array of UUIDs to the list of UUIDs that are used to validate the user’s selection.

**Availability**:
- macOS 10.2+

## Declaration

```swift
@MainActor
func addAllowedUUIDArray(_ allowedUUIDArray: [Any]!)
```

#### Discussion

The user’s device selection gets validated against the UUIDs passed to -addAllowedUUID: addAllowedUUIDArray:. Each call to those methods essentially adds a filter that the selected device gets validated with. If any of the filters match, the device is considered valid. If they all fail, the device is not valid and the user is presented with an error code that the device does not support the required services. The UUID passed to -addAllowedUUID: is the only UUID that must be present in the device’s SDP service records. Alternatively, all of the UUIDs in the UUID array passed to -addAllowedUUIDArray must be present.

NOTE: This method is only available in macOS 10.2.4 (Bluetooth v1.1) or later.

## Parameters

- `allowedUUIDArray`: An NSArray of UUIDs that all must be present in a device for it to be selectable.

## See Also

- [func addAllowedUUID(IOBluetoothSDPUUID!)](iobluetoothdeviceselectorcontroller/addalloweduuid(_:).md)
  Adds a UUID to the list of UUIDs that are used to validate the user’s selection.
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
- [func getResults() -> [Any]!](iobluetoothdeviceselectorcontroller/getresults.md)
  Returns the result of the user’s selection.
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

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetoothui/iobluetoothdeviceselectorcontroller/addalloweduuidarray(_:))*