# process(atCommand:)

**Framework**: IOBluetooth  
**Kind**: method

Processes a command from a connected Bluetooth hands-free phone or headset.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func process(atCommand: String!)
```

## Parameters

- `atCommand`: A string containing the AT command sent from the hands-free Bluetooth device.

## See Also

- [func sendResponse(String!)](iobluetoothhandsfreeaudiogateway/sendresponse(_:).md)
  Sends data followed by a success message to a connected Bluetooth hands-free phone or headset.
- [func sendResponse(String!, withOK: Bool)](iobluetoothhandsfreeaudiogateway/sendresponse(_:withok:).md)
  Sends data followed by an optional success message to a connected Bluetooth hands-free phone or headset.
- [func sendOKResponse()](iobluetoothhandsfreeaudiogateway/sendokresponse.md)
  Sends a success message to a connected Bluetooth hands-free phone or headset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreeaudiogateway/process(atcommand:))*