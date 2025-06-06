# sendSMS(_:message:)

**Framework**: IOBluetooth  
**Kind**: method

Sends a text message to a phone number.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func sendSMS(_ aNumber: String!, message aMessage: String!)
```

## Parameters

- `aNumber`: The phone number to send the message to.
- `aMessage`: A string containing a message. The message must be no longer than 160 characters.

## See Also

- [func sendDTMF(String!)](iobluetoothhandsfreedevice/senddtmf(_:).md)
  Sends the tone associated with a phone key to the hands-free Bluetooth device.
- [func send(atCommand: String!)](iobluetoothhandsfreedevice/send(atcommand:).md)
  Sends an AT command to the Bluetooth audio gateway.
- [func send(atCommand: String!, timeout: Float, selector: Selector!, target: Any!)](iobluetoothhandsfreedevice/send(atcommand:timeout:selector:target:).md)
  Send an AT command to the Bluetooth audio gateway and performs a selector on completion or timeout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevice/sendsms(_:message:))*