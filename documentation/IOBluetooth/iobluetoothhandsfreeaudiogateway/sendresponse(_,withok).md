# sendResponse(_:withOK:)

**Framework**: IOBluetooth  
**Kind**: method  
**Role**: Instance Method

Sends data followed by an optional success message to a connected Bluetooth hands-free phone or headset.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func sendResponse(_ response: String!, withOK: Bool)
```

```objc
- (void) sendResponse:(NSString *) response withOK:(BOOL) withOK;
```

## Parameters

- `response`: A string containing the data.
- `withOK`: If `true`, send an `OK` message after sending the response.

## See Also

### Sending and Receiving Commands
- [func sendResponse(String!)](./sendresponse%28_%29.md)
  Sends data followed by a success message to a connected Bluetooth hands-free phone or headset.
- [func sendOKResponse()](./sendokresponse%28%29.md)
  Sends a success message to a connected Bluetooth hands-free phone or headset.
- [func process(atCommand: String!)](./process%28atcommand%29.md)
  Processes a command from a connected Bluetooth hands-free phone or headset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreeaudiogateway/sendresponse(_:withok:))*