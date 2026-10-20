# sendSMS(_:message:)

**Framework**: IOBluetooth  
**Kind**: method  
**Role**: Instance Method

Sends a text message to a phone number.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func sendSMS(_ aNumber: String!, message aMessage: String!)
```

```objc
- (void) sendSMS:(NSString *) aNumber message:(NSString *) aMessage;
```

## Parameters

- `aNumber`: The phone number to send the message to.
- `aMessage`: A string containing a message. The message must be no longer than 160 characters.

## See Also

### Sending Messages and Commands
- [func sendDTMF(String!)](./senddtmf%28_%29.md)
  Sends the tone associated with a phone key to the hands-free Bluetooth device.
- [func send(atCommand: String!)](./send%28atcommand%29.md)
  Sends an AT command to the Bluetooth audio gateway.
- [func send(atCommand: String!, timeout: Float, selector: Selector!, target: Any!)](./send%28atcommand,timeout,selector,target%29.md)
  Send an AT command to the Bluetooth audio gateway and performs a selector on completion or timeout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevice/sendsms(_:message:))*