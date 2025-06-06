# handsFree(_:subscriberNumber:)

**Framework**: IOBluetooth  
**Kind**: method

Tells the delegate the subscriber number of a call.

**Availability**:
- macOS 10.7+

## Declaration

```swift
optional func handsFree(_ device: IOBluetoothHandsFreeDevice!, subscriberNumber: String!)
```

#### Discussion

If multiple subscriber numbers are on the gateway, this function is called once for each subscriber number.

## Parameters

- `device`: The connected Bluetooth hands-free phone or headset.
- `subscriberNumber`: The subscriber number.

## See Also

- [func handsFree(IOBluetoothHandsFreeDevice!, ringAttempt: NSNumber!)](iobluetoothhandsfreedevicedelegate/handsfree(_:ringattempt:).md)
  Tells the delegate the phone is ringing.
- [func handsFree(IOBluetoothHandsFreeDevice!, unhandledResultCode: String!)](iobluetoothhandsfreedevicedelegate/handsfree(_:unhandledresultcode:).md)
  Tells the delegate the phone sent an unknown code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevicedelegate/handsfree(_:subscribernumber:))*