# handsFree(_:subscriberNumber:)

**Framework**: IOBluetooth  
**Kind**: method  
**Role**: Instance Method

Tells the delegate the subscriber number of a call.

**Availability**:
- macOS 10.7+

## Declaration

```swift
optional func handsFree(_ device: IOBluetoothHandsFreeDevice!, subscriberNumber: String!)
```

```objc
- (void) handsFree:(IOBluetoothHandsFreeDevice *) device subscriberNumber:(NSString *) subscriberNumber;
```

#### Discussion

If multiple subscriber numbers are on the gateway, this function is called once for each subscriber number.

## Parameters

- `device`: The connected Bluetooth hands-free phone or headset.
- `subscriberNumber`: The subscriber number.

## See Also

### Receiving Other Information
- [func handsFree(IOBluetoothHandsFreeDevice!, ringAttempt: NSNumber!)](./handsfree%28_,ringattempt%29.md)
  Tells the delegate the phone is ringing.
- [func handsFree(IOBluetoothHandsFreeDevice!, unhandledResultCode: String!)](./handsfree%28_,unhandledresultcode%29.md)
  Tells the delegate the phone sent an unknown code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevicedelegate/handsfree(_:subscribernumber:))*