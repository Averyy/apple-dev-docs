# setSearchAttributes(_:)

**Framework**: IOBluetooth UI  
**Kind**: method  
**Role**: Instance Method

Sets the search attributes that control the panel’s search/inquiry behavior.

**Availability**:
- macOS 10.2+

## Declaration

```swift
func setSearchAttributes(_ searchAttributes: UnsafePointer<IOBluetoothDeviceSearchAttributes>!)
```

```objc
- (void) setSearchAttributes:(const IOBluetoothDeviceSearchAttributes *) searchAttributes;
```

## Discussion

The device search attributes control the inquiry behavior of the panel. They allow only devices that match the specified attributes (i.e. class of device) to be displayed to the user. Note that this only covers attributes returned in an inquiry result and not actual SDP services on the device.

NOTE: This method is only available in macOS 10.2.4 (Bluetooth v1.1) or later.

## Parameters

- `searchAttributes`: Attributes to control the panel’s inquiry behavior.

## See Also

### Instance Methods
- [func addAllowedUUID(IOBluetoothSDPUUID!)](./addalloweduuid%28_%29.md)
  Adds a UUID to the list of UUIDs that are used to validate the user’s selection.
- [func addAllowedUUIDArray([Any]!)](./addalloweduuidarray%28_%29.md)
  Adds an array of UUIDs to the list of UUIDs that are used to validate the user’s selection.
- [func beginSheetModal(for: NSWindow!, modalDelegate: Any!, didEnd: Selector!, contextInfo: UnsafeMutableRawPointer!) -> IOReturn](./beginsheetmodal%28for,modaldelegate,didend,contextinfo%29.md)
  Runs the service browser panel as a sheet on the target window.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetoothui/iobluetoothservicebrowsercontroller/setsearchattributes(_:))*