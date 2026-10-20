# handsFree(_:unhandledResultCode:)

**Framework**: IOBluetooth  
**Kind**: method  
**Role**: Instance Method

Tells the delegate the phone sent an unknown code.

**Availability**:
- macOS 10.7+

## Declaration

```swift
optional func handsFree(_ device: IOBluetoothHandsFreeDevice!, unhandledResultCode resultCode: String!)
```

```objc
- (void) handsFree:(IOBluetoothHandsFreeDevice *) device unhandledResultCode:(NSString *) resultCode;
```

## Parameters

- `device`: The connected Bluetooth hands-free phone or headset.
- `resultCode`: A string containing the result code. The `“/r/n”` strings are stripped from the beginning and end.

## See Also

### Receiving Other Information
- [func handsFree(IOBluetoothHandsFreeDevice!, subscriberNumber: String!)](./handsfree%28_,subscribernumber%29.md)
  Tells the delegate the subscriber number of a call.
- [func handsFree(IOBluetoothHandsFreeDevice!, ringAttempt: NSNumber!)](./handsfree%28_,ringattempt%29.md)
  Tells the delegate the phone is ringing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevicedelegate/handsfree(_:unhandledresultcode:))*