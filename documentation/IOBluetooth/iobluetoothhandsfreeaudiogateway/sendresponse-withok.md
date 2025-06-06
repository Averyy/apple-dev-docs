# sendResponse(_:withOK:)

**Framework**: IOBluetooth  
**Kind**: method

Sends data followed by an optional success message to a connected Bluetooth hands-free phone or headset.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func sendResponse(_ response: String!, withOK: Bool)
```

## Parameters

- `response`: A string containing the data.
- `withOK`: If  , send an   message after sending the response.

## See Also

- [func sendResponse(String!)](iobluetoothhandsfreeaudiogateway/sendresponse(_:).md)
  Sends data followed by a success message to a connected Bluetooth hands-free phone or headset.
- [func sendOKResponse()](iobluetoothhandsfreeaudiogateway/sendokresponse.md)
  Sends a success message to a connected Bluetooth hands-free phone or headset.
- [func process(atCommand: String!)](iobluetoothhandsfreeaudiogateway/process(atcommand:).md)
  Processes a command from a connected Bluetooth hands-free phone or headset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreeaudiogateway/sendresponse(_:withok:))*