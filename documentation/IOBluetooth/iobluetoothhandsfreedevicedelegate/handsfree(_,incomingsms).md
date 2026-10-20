# handsFree(_:incomingSMS:)

**Framework**: IOBluetooth  
**Kind**: method  
**Role**: Instance Method

Tells the delegate there’s an incoming text message.

**Availability**:
- macOS 10.7+

## Declaration

```swift
optional func handsFree(_ device: IOBluetoothHandsFreeDevice!, incomingSMS sms: [AnyHashable : Any]!)
```

```objc
- (void) handsFree:(IOBluetoothHandsFreeDevice *) device incomingSMS:(NSDictionary *) sms;
```

## Parameters

- `device`: The connected Bluetooth hands-free phone or headset.
- `sms`: A dictionary containing the incoming SMS message. For dictionary keys, see [SMS Dictionary Key Constants](../sms-dictionary-key-constants.md).

## See Also

### Receiving SMS Information
- [SMS Dictionary Key Constants](../sms-dictionary-key-constants.md)
  Read the parts of an SMS message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevicedelegate/handsfree(_:incomingsms:))*