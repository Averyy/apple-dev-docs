# handsFree(_:batteryCharge:)

**Framework**: IOBluetooth  
**Kind**: method  
**Role**: Instance Method

Tells the delegate the battery level indicator of the connected Bluetooth hands-free phone or headset has changed.

**Availability**:
- macOS 10.7+

## Declaration

```swift
optional func handsFree(_ device: IOBluetoothHandsFreeDevice!, batteryCharge: NSNumber!)
```

```objc
- (void) handsFree:(IOBluetoothHandsFreeDevice *) device batteryCharge:(NSNumber *) batteryCharge;
```

## Parameters

- `device`: The connected Bluetooth hands-free phone or headset.
- `batteryCharge`: The new value of the battery level indicator. For possible values, see [`IOBluetoothHandsFreeIndicatorBattChg`](../iobluetoothhandsfreeindicatorbattchg.md).

## See Also

### Receiving Status Indicator Changes
- [func handsFree(IOBluetoothHandsFreeDevice!, callSetupMode: NSNumber!)](./handsfree%28_,callsetupmode%29.md)
  Tells the delegate the call setup indicator of the connected Bluetooth hands-free phone or headset has changed.
- [func handsFree(IOBluetoothHandsFreeDevice!, isCallActive: NSNumber!)](./handsfree%28_,iscallactive%29.md)
  Tells the delegate the active call indicator of the connected Bluetooth hands-free phone or headset has changed.
- [func handsFree(IOBluetoothHandsFreeDevice!, isServiceAvailable: NSNumber!)](./handsfree%28_,isserviceavailable%29.md)
  Tells the delegate the service level indicator of the connected Bluetooth hands-free phone or headset has changed.
- [func handsFree(IOBluetoothHandsFreeDevice!, signalStrength: NSNumber!)](./handsfree%28_,signalstrength%29.md)
  Tells the delegate the call setup signal strength indicator of the connected Bluetooth hands-free phone or headset has changed.
- [func handsFree(IOBluetoothHandsFreeDevice!, callHoldState: NSNumber!)](./handsfree%28_,callholdstate%29.md)
  Tells the delegate the call held indicator of the connected Bluetooth hands-free phone or headset has changed.
- [func handsFree(IOBluetoothHandsFreeDevice!, isRoaming: NSNumber!)](./handsfree%28_,isroaming%29.md)
  Tells the delegate the roaming indicator of the connected Bluetooth hands-free phone or headset has changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevicedelegate/handsfree(_:batterycharge:))*