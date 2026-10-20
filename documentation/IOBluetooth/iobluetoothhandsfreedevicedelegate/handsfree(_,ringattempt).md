# handsFree(_:ringAttempt:)

**Framework**: IOBluetooth  
**Kind**: method  
**Role**: Instance Method

Tells the delegate the phone is ringing.

**Availability**:
- macOS 10.7+

## Declaration

```swift
optional func handsFree(_ device: IOBluetoothHandsFreeDevice!, ringAttempt: NSNumber!)
```

```objc
- (void) handsFree:(IOBluetoothHandsFreeDevice *) device ringAttempt:(NSNumber *) ringAttempt;
```

## Parameters

- `device`: The connected Bluetooth hands-free phone or headset.
- `ringAttempt`: The number of ring alerts received for the call.

## See Also

### Receiving Other Information
- [func handsFree(IOBluetoothHandsFreeDevice!, subscriberNumber: String!)](./handsfree%28_,subscribernumber%29.md)
  Tells the delegate the subscriber number of a call.
- [func handsFree(IOBluetoothHandsFreeDevice!, unhandledResultCode: String!)](./handsfree%28_,unhandledresultcode%29.md)
  Tells the delegate the phone sent an unknown code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevicedelegate/handsfree(_:ringattempt:))*