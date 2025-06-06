# handsFree(_:hangup:)

**Framework**: IOBluetooth  
**Kind**: method

Tells the delegate the connected Bluetooth hands-free phone or headset is sending a hang-up signal.

**Availability**:
- macOS 10.7+

## Declaration

```swift
optional func handsFree(_ device: IOBluetoothHandsFreeAudioGateway!, hangup: NSNumber!)
```

## Parameters

- `device`: The remote hands-free Bluetooth device that’s sending a hang-up signal.
- `hangup`: A number that indicates whether the device is sending a hang-up signal. This value is always set to 1.

## See Also

- [func handsFree(IOBluetoothHandsFreeAudioGateway!, redial: NSNumber!)](iobluetoothhandsfreeaudiogatewaydelegate/handsfree(_:redial:).md)
  Tells the delegate the connected Bluetooth hands-free phone or headset is redialing the last phone number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreeaudiogatewaydelegate/handsfree(_:hangup:))*