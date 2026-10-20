# send(atCommand:timeout:selector:target:)

**Framework**: IOBluetooth  
**Kind**: method  
**Role**: Instance Method

Send an AT command to the Bluetooth audio gateway and performs a selector on completion or timeout.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func send(atCommand: String!, timeout: Float, selector: Selector!, target: Any!)
```

```objc
- (void) sendATCommand:(NSString *) atCommand timeout:(float) timeout selector:(SEL) selector target:(id) target;
```

## Parameters

- `atCommand`: A string containing the AT command.
- `timeout`: The number of seconds until the message times out.
- `selector`: The function to call on completion or timeout.
- `target`: The target object for the completion call.

## See Also

### Sending Messages and Commands
- [func sendSMS(String!, message: String!)](./sendsms%28_,message%29.md)
  Sends a text message to a phone number.
- [func sendDTMF(String!)](./senddtmf%28_%29.md)
  Sends the tone associated with a phone key to the hands-free Bluetooth device.
- [func send(atCommand: String!)](./send%28atcommand%29.md)
  Sends an AT command to the Bluetooth audio gateway.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevice/send(atcommand:timeout:selector:target:))*