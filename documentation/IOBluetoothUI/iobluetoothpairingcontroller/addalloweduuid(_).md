# addAllowedUUID(_:)

**Framework**: IOBluetooth UI  
**Kind**: method  
**Role**: Instance Method

Adds a UUID to the list of UUIDs that are used to validate the user’s selection.

**Availability**:
- macOS 10.2+

## Declaration

```swift
func addAllowedUUID(_ allowedUUID: IOBluetoothSDPUUID!)
```

```objc
- (void) addAllowedUUID:(IOBluetoothSDPUUID *) allowedUUID;
```

## Discussion

The user’s device selection gets validated against the UUIDs passed to -addAllowedUUID: addAllowedUUIDArray:. Each call to those methods essentially adds a filter that the selected device gets validated with. If any of the filters match, the device is considered valid. If they all fail, the device is not valid and the user is presented with an error code that the device does not support the required services. The UUID passed to -addAllowedUUID: is the only UUID that must be present in the device’s SDP service records. Alternatively, all of the UUIDs in the UUID array passed to -addAllowedUUIDArray must be present.

NOTE: This method is only available in macOS 10.2.4 (Bluetooth v1.1) or later.

## Parameters

- `allowedUUID`: UUID that a device may contain to be selected

## See Also

### Instance Methods
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
- [func getResults() -> [Any]!](./getresults%28%29.md)
  Returns an NSArray of the devices that were paired.
- [func getSearchAttributes() -> UnsafePointer<IOBluetoothDeviceSearchAttributes>!](./getsearchattributes%28%29.md)
  Returns the search attributes that control the panel’s search/inquiry behavior.
- [func getTitle() -> String!](./gettitle%28%29.md)
  Returns the title of the device selector panel.
- [func runModal() -> Int32](./runmodal%28%29.md)
  Runs the pairing panel in a modal session to allow the user to select a Bluetooth device.
- [func setDescriptionText(String!)](./setdescriptiontext%28_%29.md)
  Sets the description text that appears in the device selector panel.
- [func setOptions(IOBluetoothServiceBrowserControllerOptions)](./setoptions%28_%29.md)
  Sets the option bits that control the panel’s behavior.
- [func setPrompt(String!)](./setprompt%28_%29.md)
  Sets the title of the default/select button in the device selector panel.
- [func setSearchAttributes(UnsafePointer<IOBluetoothDeviceSearchAttributes>!)](./setsearchattributes%28_%29.md)
  Sets the search attributes that control the panel’s search/inquiry behavior.
- [func setTitle(String!)](./settitle%28_%29.md)
  Sets the title of the panel when not run as a sheet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetoothui/iobluetoothpairingcontroller/addalloweduuid(_:))*