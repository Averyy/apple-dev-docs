# handsFree(_:currentCall:)

**Framework**: IOBluetooth  
**Kind**: method

Sends the delegate information about the current call.

**Availability**:
- macOS 10.7+

## Declaration

```swift
optional func handsFree(_ device: IOBluetoothHandsFreeDevice!, currentCall: [AnyHashable : Any]!)
```

## Parameters

- `device`: The connected Bluetooth hands-free phone or headset.
- `currentCall`: A dictionary with the incoming SMS message. For dictionary keys, see  .

## See Also

- [func handsFree(IOBluetoothHandsFreeDevice!, incomingCallFrom: String!)](iobluetoothhandsfreedevicedelegate/handsfree(_:incomingcallfrom:).md)
  Tells the delegate there’s an incoming call on the connected Bluetooth hands-free phone or headset.
- [Current Call Information Constants](current-call-information-constants.md)
  Get information about a phone call on a hands-free Bluetooth device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevicedelegate/handsfree(_:currentcall:))*