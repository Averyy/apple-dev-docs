# handsFree(_:signalStrength:)

**Framework**: IOBluetooth  
**Kind**: method  
**Role**: Instance Method

Tells the delegate the call setup signal strength indicator of the connected Bluetooth hands-free phone or headset has changed.

**Availability**:
- macOS 10.7+

## Declaration

```swift
optional func handsFree(_ device: IOBluetoothHandsFreeDevice!, signalStrength: NSNumber!)
```

```objc
- (void) handsFree:(IOBluetoothHandsFreeDevice *) device signalStrength:(NSNumber *) signalStrength;
```

## Parameters

- `device`: The connected Bluetooth hands-free phone or headset.
- `signalStrength`: The new value of the signal strength indicator. For possible values, see [`IOBluetoothHandsFreeIndicatorSignal`](../iobluetoothhandsfreeindicatorsignal.md).

## See Also

### Receiving Status Indicator Changes
- [func handsFree(IOBluetoothHandsFreeDevice!, callSetupMode: NSNumber!)](./handsfree%28_,callsetupmode%29.md)
  Tells the delegate the call setup indicator of the connected Bluetooth hands-free phone or headset has changed.
- [func handsFree(IOBluetoothHandsFreeDevice!, isCallActive: NSNumber!)](./handsfree%28_,iscallactive%29.md)
  Tells the delegate the active call indicator of the connected Bluetooth hands-free phone or headset has changed.
- [func handsFree(IOBluetoothHandsFreeDevice!, isServiceAvailable: NSNumber!)](./handsfree%28_,isserviceavailable%29.md)
  Tells the delegate the service level indicator of the connected Bluetooth hands-free phone or headset has changed.
- [func handsFree(IOBluetoothHandsFreeDevice!, callHoldState: NSNumber!)](./handsfree%28_,callholdstate%29.md)
  Tells the delegate the call held indicator of the connected Bluetooth hands-free phone or headset has changed.
- [func handsFree(IOBluetoothHandsFreeDevice!, isRoaming: NSNumber!)](./handsfree%28_,isroaming%29.md)
  Tells the delegate the roaming indicator of the connected Bluetooth hands-free phone or headset has changed.
- [func handsFree(IOBluetoothHandsFreeDevice!, batteryCharge: NSNumber!)](./handsfree%28_,batterycharge%29.md)
  Tells the delegate the battery level indicator of the connected Bluetooth hands-free phone or headset has changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevicedelegate/handsfree(_:signalstrength:))*