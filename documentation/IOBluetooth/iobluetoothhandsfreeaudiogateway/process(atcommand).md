# process(atCommand:)

**Framework**: IOBluetooth  
**Kind**: method  
**Role**: Instance Method

Processes a command from a connected Bluetooth hands-free phone or headset.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func process(atCommand: String!)
```

```objc
- (void) processATCommand:(NSString *) atCommand;
```

## Parameters

- `atCommand`: A string containing the AT command sent from the hands-free Bluetooth device.

## See Also

### Sending and Receiving Commands
- [func sendResponse(String!)](./sendresponse%28_%29.md)
  Sends data followed by a success message to a connected Bluetooth hands-free phone or headset.
- [func sendResponse(String!, withOK: Bool)](./sendresponse%28_,withok%29.md)
  Sends data followed by an optional success message to a connected Bluetooth hands-free phone or headset.
- [func sendOKResponse()](./sendokresponse%28%29.md)
  Sends a success message to a connected Bluetooth hands-free phone or headset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreeaudiogateway/process(atcommand:))*