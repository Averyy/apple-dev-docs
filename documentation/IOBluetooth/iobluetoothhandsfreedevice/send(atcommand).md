# send(atCommand:)

**Framework**: IOBluetooth  
**Kind**: method

Sends an AT command to the Bluetooth audio gateway.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func send(atCommand: String!)
```

## Parameters

- `atCommand`: A string containing the AT command.

## See Also

- [func sendSMS(String!, message: String!)](iobluetoothhandsfreedevice/sendsms(_:message:).md)
  Sends a text message to a phone number.
- [func sendDTMF(String!)](iobluetoothhandsfreedevice/senddtmf(_:).md)
  Sends the tone associated with a phone key to the hands-free Bluetooth device.
- [func send(atCommand: String!, timeout: Float, selector: Selector!, target: Any!)](iobluetoothhandsfreedevice/send(atcommand:timeout:selector:target:).md)
  Send an AT command to the Bluetooth audio gateway and performs a selector on completion or timeout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevice/send(atcommand:))*