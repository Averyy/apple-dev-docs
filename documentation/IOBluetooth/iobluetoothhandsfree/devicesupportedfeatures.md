# deviceSupportedFeatures

**Framework**: IOBluetooth  
**Kind**: property  
**Role**: Instance Property

Return the device’s supported features.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var deviceSupportedFeatures: UInt32 { get }
```

```objc
@property (readonly) uint32_t deviceSupportedFeatures;
```

## Return Value

The device features bitmap

## Discussion

Returns the device’s supported features bitmap. The values are described in “IOBluetoothHandsFreeDeviceFeatures and IOBluetoothHandsFreeAudioGatewayFeatures.”


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfree/devicesupportedfeatures)*