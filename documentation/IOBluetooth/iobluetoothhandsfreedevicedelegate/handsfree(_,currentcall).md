# handsFree(_:currentCall:)

**Framework**: IOBluetooth  
**Kind**: method  
**Role**: Instance Method

Sends the delegate information about the current call.

**Availability**:
- macOS 10.7+

## Declaration

```swift
optional func handsFree(_ device: IOBluetoothHandsFreeDevice!, currentCall: [AnyHashable : Any]!)
```

```objc
- (void) handsFree:(IOBluetoothHandsFreeDevice *) device currentCall:(NSDictionary *) currentCall;
```

## Parameters

- `device`: The connected Bluetooth hands-free phone or headset.
- `currentCall`: A dictionary with the incoming SMS message. For dictionary keys, see [Current Call Information Constants](../current-call-information-constants.md).

## See Also

### Receiving Call Status
- [func handsFree(IOBluetoothHandsFreeDevice!, incomingCallFrom: String!)](./handsfree%28_,incomingcallfrom%29.md)
  Tells the delegate there’s an incoming call on the connected Bluetooth hands-free phone or headset.
- [Current Call Information Constants](../current-call-information-constants.md)
  Get information about a phone call on a hands-free Bluetooth device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevicedelegate/handsfree(_:currentcall:))*