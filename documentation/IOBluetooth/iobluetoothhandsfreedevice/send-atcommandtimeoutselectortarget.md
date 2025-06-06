# send(atCommand:timeout:selector:target:)

**Framework**: IOBluetooth  
**Kind**: method

Send an AT command to the Bluetooth audio gateway and performs a selector on completion or timeout.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func send(atCommand: String!, timeout: Float, selector: Selector!, target: Any!)
```

## Parameters

- `atCommand`: A string containing the AT command.
- `timeout`: The number of seconds until the message times out.
- `selector`: The function to call on completion or timeout.
- `target`: The target object for the completion call.

## See Also

- [func sendSMS(String!, message: String!)](iobluetoothhandsfreedevice/sendsms(_:message:).md)
  Sends a text message to a phone number.
- [func sendDTMF(String!)](iobluetoothhandsfreedevice/senddtmf(_:).md)
  Sends the tone associated with a phone key to the hands-free Bluetooth device.
- [func send(atCommand: String!)](iobluetoothhandsfreedevice/send(atcommand:).md)
  Sends an AT command to the Bluetooth audio gateway.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevice/send(atcommand:timeout:selector:target:))*