# handsFree(_:redial:)

**Framework**: IOBluetooth  
**Kind**: method  
**Role**: Instance Method

Tells the delegate the connected Bluetooth hands-free phone or headset is redialing the last phone number.

**Availability**:
- macOS 10.7+

## Declaration

```swift
optional func handsFree(_ device: IOBluetoothHandsFreeAudioGateway!, redial: NSNumber!)
```

```objc
- (void) handsFree:(IOBluetoothHandsFreeAudioGateway *) device redial:(NSNumber *) redial;
```

## Parameters

- `device`: The audio gateway for the remote hands-free Bluetooth device.
- `redial`: A number that indicates whether the device is attempting to redial. This value is always set to 1.

## See Also

### Receiving Status Change Information
- [func handsFree(IOBluetoothHandsFreeAudioGateway!, hangup: NSNumber!)](./handsfree%28_,hangup%29.md)
  Tells the delegate the connected Bluetooth hands-free phone or headset is sending a hang-up signal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreeaudiogatewaydelegate/handsfree(_:redial:))*