# handsFree(_:ringAttempt:)

**Framework**: IOBluetooth  
**Kind**: method

Tells the delegate the phone is ringing.

**Availability**:
- macOS 10.7+

## Declaration

```swift
optional func handsFree(_ device: IOBluetoothHandsFreeDevice!, ringAttempt: NSNumber!)
```

## Parameters

- `device`: The connected Bluetooth hands-free phone or headset.
- `ringAttempt`: The number of ring alerts received for the call.

## See Also

- [func handsFree(IOBluetoothHandsFreeDevice!, subscriberNumber: String!)](iobluetoothhandsfreedevicedelegate/handsfree(_:subscribernumber:).md)
  Tells the delegate the subscriber number of a call.
- [func handsFree(IOBluetoothHandsFreeDevice!, unhandledResultCode: String!)](iobluetoothhandsfreedevicedelegate/handsfree(_:unhandledresultcode:).md)
  Tells the delegate the phone sent an unknown code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevicedelegate/handsfree(_:ringattempt:))*