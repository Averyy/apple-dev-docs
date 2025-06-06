# handsFree(_:callHoldState:)

**Framework**: IOBluetooth  
**Kind**: method

Tells the delegate the call held indicator of the connected Bluetooth hands-free phone or headset has changed.

**Availability**:
- macOS 10.7+

## Declaration

```swift
optional func handsFree(_ device: IOBluetoothHandsFreeDevice!, callHoldState: NSNumber!)
```

## Parameters

- `device`: The connected Bluetooth hands-free phone or headset.
- `callHoldState`: The new value of the call hold indicator. For possible values, see  .

## See Also

- [func handsFree(IOBluetoothHandsFreeDevice!, callSetupMode: NSNumber!)](iobluetoothhandsfreedevicedelegate/handsfree(_:callsetupmode:).md)
  Tells the delegate the call setup indicator of the connected Bluetooth hands-free phone or headset has changed.
- [func handsFree(IOBluetoothHandsFreeDevice!, isCallActive: NSNumber!)](iobluetoothhandsfreedevicedelegate/handsfree(_:iscallactive:).md)
  Tells the delegate the active call indicator of the connected Bluetooth hands-free phone or headset has changed.
- [func handsFree(IOBluetoothHandsFreeDevice!, isServiceAvailable: NSNumber!)](iobluetoothhandsfreedevicedelegate/handsfree(_:isserviceavailable:).md)
  Tells the delegate the service level indicator of the connected Bluetooth hands-free phone or headset has changed.
- [func handsFree(IOBluetoothHandsFreeDevice!, signalStrength: NSNumber!)](iobluetoothhandsfreedevicedelegate/handsfree(_:signalstrength:).md)
  Tells the delegate the call setup signal strength indicator of the connected Bluetooth hands-free phone or headset has changed.
- [func handsFree(IOBluetoothHandsFreeDevice!, isRoaming: NSNumber!)](iobluetoothhandsfreedevicedelegate/handsfree(_:isroaming:).md)
  Tells the delegate the roaming indicator of the connected Bluetooth hands-free phone or headset has changed.
- [func handsFree(IOBluetoothHandsFreeDevice!, batteryCharge: NSNumber!)](iobluetoothhandsfreedevicedelegate/handsfree(_:batterycharge:).md)
  Tells the delegate the battery level indicator of the connected Bluetooth hands-free phone or headset has changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevicedelegate/handsfree(_:callholdstate:))*