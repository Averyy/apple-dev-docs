# handsFree(_:redial:)

**Framework**: IOBluetooth  
**Kind**: method

Tells the delegate the connected Bluetooth hands-free phone or headset is redialing the last phone number.

**Availability**:
- macOS 10.7+

## Declaration

```swift
optional func handsFree(_ device: IOBluetoothHandsFreeAudioGateway!, redial: NSNumber!)
```

## Parameters

- `device`: The audio gateway for the remote hands-free Bluetooth device.
- `redial`: A number that indicates whether the device is attempting to redial. This value is always set to 1.

## See Also

- [func handsFree(IOBluetoothHandsFreeAudioGateway!, hangup: NSNumber!)](iobluetoothhandsfreeaudiogatewaydelegate/handsfree(_:hangup:).md)
  Tells the delegate the connected Bluetooth hands-free phone or headset is sending a hang-up signal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreeaudiogatewaydelegate/handsfree(_:redial:))*