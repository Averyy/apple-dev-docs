# send(atCommand:)

**Framework**: IOBluetooth  
**Kind**: method  
**Role**: Instance Method

Sends an AT command to the Bluetooth audio gateway.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func send(atCommand: String!)
```

```objc
- (void) sendATCommand:(NSString *) atCommand;
```

## Parameters

- `atCommand`: A string containing the AT command.

## See Also

### Sending Messages and Commands
- [func sendSMS(String!, message: String!)](./sendsms%28_,message%29.md)
  Sends a text message to a phone number.
- [func sendDTMF(String!)](./senddtmf%28_%29.md)
  Sends the tone associated with a phone key to the hands-free Bluetooth device.
- [func send(atCommand: String!, timeout: Float, selector: Selector!, target: Any!)](./send%28atcommand,timeout,selector,target%29.md)
  Send an AT command to the Bluetooth audio gateway and performs a selector on completion or timeout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevice/send(atcommand:))*