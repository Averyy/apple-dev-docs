# setOptions(_:)

**Framework**: IOBluetooth UI  
**Kind**: method  
**Role**: Instance Method

Sets the option bits that control the panel’s behavior.

**Availability**:
- macOS 10.2+

## Declaration

```swift
func setOptions(_ options: IOBluetoothServiceBrowserControllerOptions)
```

```objc
- (void) setOptions:(IOBluetoothServiceBrowserControllerOptions) options;
```

## Discussion

The pairing controller options control the behavior of the panel. Currently kIOBluetoothServiceBrowserControllerOptionsAutoStartInquiry is the only supported option. In the future more options will be added to control things like whether the connection to the device is closed when the controller is finished or if multiple selection is allowed.

NOTE: This method is only available in macOS 10.2.4 (Bluetooth v1.1) or later.

## Parameters

- `options`: Options to control the panel’s behavior.

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
- [func setPrompt(String!)](./setprompt%28_%29.md)
  Sets the title of the default/select button in the device selector panel.
- [func setSearchAttributes(UnsafePointer<IOBluetoothDeviceSearchAttributes>!)](./setsearchattributes%28_%29.md)
  Sets the search attributes that control the panel’s search/inquiry behavior.
- [func setTitle(String!)](./settitle%28_%29.md)
  Sets the title of the panel when not run as a sheet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetoothui/iobluetoothpairingcontroller/setoptions(_:))*