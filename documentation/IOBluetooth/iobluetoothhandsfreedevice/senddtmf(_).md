# sendDTMF(_:)

**Framework**: IOBluetooth  
**Kind**: method  
**Role**: Instance Method

Sends the tone associated with a phone key to the hands-free Bluetooth device.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func sendDTMF(_ character: String!)
```

```objc
- (void) sendDTMF:(NSString *) character;
```

## Parameters

- `character`: The phone keypad character for the tone. The character must be one of the following:

  - `0-9`
  - `#`
  - `*`
  - `A-D`

## See Also

### Sending Messages and Commands
- [func sendSMS(String!, message: String!)](./sendsms%28_,message%29.md)
  Sends a text message to a phone number.
- [func send(atCommand: String!)](./send%28atcommand%29.md)
  Sends an AT command to the Bluetooth audio gateway.
- [func send(atCommand: String!, timeout: Float, selector: Selector!, target: Any!)](./send%28atcommand,timeout,selector,target%29.md)
  Send an AT command to the Bluetooth audio gateway and performs a selector on completion or timeout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevice/senddtmf(_:))*