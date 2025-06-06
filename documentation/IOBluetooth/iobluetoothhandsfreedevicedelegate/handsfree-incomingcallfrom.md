# handsFree(_:incomingCallFrom:)

**Framework**: IOBluetooth  
**Kind**: method

Tells the delegate there’s an incoming call on the connected Bluetooth hands-free phone or headset.

**Availability**:
- macOS 10.7+

## Declaration

```swift
optional func handsFree(_ device: IOBluetoothHandsFreeDevice!, incomingCallFrom number: String!)
```

## Parameters

- `device`: The connected Bluetooth hands-free phone or headset.
- `number`: The phone number of the caller.

## See Also

- [func handsFree(IOBluetoothHandsFreeDevice!, currentCall: [AnyHashable : Any]!)](iobluetoothhandsfreedevicedelegate/handsfree(_:currentcall:).md)
  Sends the delegate information about the current call.
- [Current Call Information Constants](current-call-information-constants.md)
  Get information about a phone call on a hands-free Bluetooth device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevicedelegate/handsfree(_:incomingcallfrom:))*