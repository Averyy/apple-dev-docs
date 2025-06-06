# depthModuleTemperature

**Framework**: AVFoundation  
**Kind**: property

The module capturing depth information is operating at an elevated temperature.

**Availability**:
- iOS 11.1+
- iPadOS 11.1+
- Mac Catalyst 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
static var depthModuleTemperature: AVCaptureDevice.SystemPressureState.Factors { get }
```

#### Discussion

As system pressure increases, depth quality may become degraded. To reduce system pressure from this factor, reduce depth capture frame rate.

This factor applies only to [`builtInTrueDepthCamera`](avcapturedevice/devicetype-swift.struct/builtintruedepthcamera.md) devices.

## See Also

- [static var systemTemperature: AVCaptureDevice.SystemPressureState.Factors](avcapturedevice/systempressurestate-swift.class/factors-swift.struct/systemtemperature.md)
  The entire system is under elevated thermal load.
- [static var peakPower: AVCaptureDevice.SystemPressureState.Factors](avcapturedevice/systempressurestate-swift.class/factors-swift.struct/peakpower.md)
  The system’s peak power requirements exceed the battery’s current capacity.
- [static var cameraTemperature: AVCaptureDevice.SystemPressureState.Factors](avcapturedevice/systempressurestate-swift.class/factors-swift.struct/cameratemperature.md)
  The camera module is operating at an elevated temperature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/systempressurestate-swift.class/factors-swift.struct/depthmoduletemperature)*