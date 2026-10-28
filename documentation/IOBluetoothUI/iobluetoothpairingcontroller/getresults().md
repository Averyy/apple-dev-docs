# getResults()

**Framework**: IOBluetooth UI  
**Kind**: method  
**Role**: Instance Method

Returns an NSArray of the devices that were paired.

**Availability**:
- macOS 10.2+

## Declaration

```swift
func getResults() -> [Any]!
```

```objc
- (NSArray *) getResults;
```

## Return Value

Returns an NSArray of IOBluetoothDevice objects of devices that were paired. If the user cancelled the panel, nil will be returned.

## Discussion

There will only be results if the panel has been run, the user has successfully made a selection, that selection has been validated and the selected device paired. If kIOBluetoothUISuccess was returned for the session, there should be valid results. Currently only a single device is allowed to be selected, so the results array will only contain one object. However in the future multiple selection may be supported.

NOTE: This method is only available in macOS 10.2.4 (Bluetooth v1.1) or later.

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

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetoothui/iobluetoothpairingcontroller/getresults())*