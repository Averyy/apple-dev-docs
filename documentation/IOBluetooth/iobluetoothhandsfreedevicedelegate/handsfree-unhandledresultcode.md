# handsFree(_:unhandledResultCode:)

**Framework**: IOBluetooth  
**Kind**: method

Tells the delegate the phone sent an unknown code.

**Availability**:
- macOS 10.7+

## Declaration

```swift
optional func handsFree(_ device: IOBluetoothHandsFreeDevice!, unhandledResultCode resultCode: String!)
```

## Parameters

- `device`: The connected Bluetooth hands-free phone or headset.
- `resultCode`: A string containing the result code. The   strings are stripped from the beginning and end.

## See Also

- [func handsFree(IOBluetoothHandsFreeDevice!, subscriberNumber: String!)](iobluetoothhandsfreedevicedelegate/handsfree(_:subscribernumber:).md)
  Tells the delegate the subscriber number of a call.
- [func handsFree(IOBluetoothHandsFreeDevice!, ringAttempt: NSNumber!)](iobluetoothhandsfreedevicedelegate/handsfree(_:ringattempt:).md)
  Tells the delegate the phone is ringing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevicedelegate/handsfree(_:unhandledresultcode:))*