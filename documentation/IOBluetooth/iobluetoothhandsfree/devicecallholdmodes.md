# deviceCallHoldModes

**Framework**: IOBluetooth  
**Kind**: property  
**Role**: Instance Property

Return the device’s supported call hold modes.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var deviceCallHoldModes: UInt32 { get }
```

```objc
@property (readonly) uint32_t deviceCallHoldModes;
```

## Return Value

The SMS services supported

## Discussion

Returns the device’s supported call hold modes bitmap. The values are described in “IOBluetoothHandsFreeCallHoldModes.”


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfree/devicecallholdmodes)*