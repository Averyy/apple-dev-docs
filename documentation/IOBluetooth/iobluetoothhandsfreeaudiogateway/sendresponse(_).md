# sendResponse(_:)

**Framework**: IOBluetooth  
**Kind**: method  
**Role**: Instance Method

Sends data followed by a success message to a connected Bluetooth hands-free phone or headset.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func sendResponse(_ response: String!)
```

```objc
- (void) sendResponse:(NSString *) response;
```

## Discussion

Calling this method has the same result as calling `sendResponse(response: response, withOK: true)`.

## Parameters

- `response`: A string containing the data.

## See Also

### Sending and Receiving Commands
- [func sendResponse(String!, withOK: Bool)](./sendresponse%28_,withok%29.md)
  Sends data followed by an optional success message to a connected Bluetooth hands-free phone or headset.
- [func sendOKResponse()](./sendokresponse%28%29.md)
  Sends a success message to a connected Bluetooth hands-free phone or headset.
- [func process(atCommand: String!)](./process%28atcommand%29.md)
  Processes a command from a connected Bluetooth hands-free phone or headset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreeaudiogateway/sendresponse(_:))*