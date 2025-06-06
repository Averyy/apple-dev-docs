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

- [func addAllowedUUID(IOBluetoothSDPUUID!)](iobluetoothpairingcontroller/addalloweduuid(_:).md)
  Adds a UUID to the list of UUIDs that are used to validate the user’s selection.
- [func addAllowedUUIDArray([Any]!)](iobluetoothpairingcontroller/addalloweduuidarray(_:).md)
  Adds an array of UUIDs to the list of UUIDs that are used to validate the user’s selection.
- [func clearAllowedUUIDs()](iobluetoothpairingcontroller/clearalloweduuids.md)
  Resets the controller back to the default state where it will accept any device the user selects.
- [func getDescriptionText() -> String!](iobluetoothpairingcontroller/getdescriptiontext.md)
  Returns the description text that appears in the device selector panel.
- [func getOptions() -> IOBluetoothServiceBrowserControllerOptions](iobluetoothpairingcontroller/getoptions.md)
  Returns the option bits that control the panel’s behavior.
- [func getResults() -> [Any]!](iobluetoothpairingcontroller/getresults.md)
  Returns an NSArray of the devices that were paired.
- [func getSearchAttributes() -> UnsafePointer<IOBluetoothDeviceSearchAttributes>!](iobluetoothpairingcontroller/getsearchattributes.md)
  Returns the search attributes that control the panel’s search/inquiry behavior.
- [func getTitle() -> String!](iobluetoothpairingcontroller/gettitle.md)
  Returns the title of the device selector panel.
- [func runModal() -> Int32](iobluetoothpairingcontroller/runmodal.md)
  Runs the pairing panel in a modal session to allow the user to select a Bluetooth device.
- [func setDescriptionText(String!)](iobluetoothpairingcontroller/setdescriptiontext(_:).md)
  Sets the description text that appears in the device selector panel.
- [func setOptions(IOBluetoothServiceBrowserControllerOptions)](iobluetoothpairingcontroller/setoptions(_:).md)
  Sets the option bits that control the panel’s behavior.
- [func setPrompt(String!)](iobluetoothpairingcontroller/setprompt(_:).md)
  Sets the title of the default/select button in the device selector panel.
- [func setSearchAttributes(UnsafePointer<IOBluetoothDeviceSearchAttributes>!)](iobluetoothpairingcontroller/setsearchattributes(_:).md)
  Sets the search attributes that control the panel’s search/inquiry behavior.
- [func setTitle(String!)](iobluetoothpairingcontroller/settitle(_:).md)
  Sets the title of the panel when not run as a sheet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetoothui/iobluetoothpairingcontroller/getprompt())*