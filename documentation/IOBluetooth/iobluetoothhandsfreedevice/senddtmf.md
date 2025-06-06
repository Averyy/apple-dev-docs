# sendDTMF(_:)

**Framework**: IOBluetooth  
**Kind**: method

Sends the tone associated with a phone key to the hands-free Bluetooth device.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func sendDTMF(_ character: String!)
```

## Parameters

- `character`: The phone keypad character for the tone. The character must be one of the following:

## See Also

- [func sendSMS(String!, message: String!)](iobluetoothhandsfreedevice/sendsms(_:message:).md)
  Sends a text message to a phone number.
- [func send(atCommand: String!)](iobluetoothhandsfreedevice/send(atcommand:).md)
  Sends an AT command to the Bluetooth audio gateway.
- [func send(atCommand: String!, timeout: Float, selector: Selector!, target: Any!)](iobluetoothhandsfreedevice/send(atcommand:timeout:selector:target:).md)
  Send an AT command to the Bluetooth audio gateway and performs a selector on completion or timeout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevice/senddtmf(_:))*