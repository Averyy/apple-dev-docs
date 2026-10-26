# cameraTemperature

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

The camera module is operating at an elevated temperature.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
static var cameraTemperature: AVCaptureDevice.SystemPressureState.Factors { get }
```

```c
AVCaptureSystemPressureFactorCameraTemperature
```

## See Also

### System pressure factors
- [static var systemTemperature: AVCaptureDevice.SystemPressureState.Factors](./systemtemperature.md)
  The entire system is under elevated thermal load.
- [static var peakPower: AVCaptureDevice.SystemPressureState.Factors](./peakpower.md)
  The system’s peak power requirements exceed the battery’s current capacity.
- [static var depthModuleTemperature: AVCaptureDevice.SystemPressureState.Factors](./depthmoduletemperature.md)
  The module capturing depth information is operating at an elevated temperature.
- [AVCaptureSystemPressureFactorNone](../../../avcapturesystempressurefactors/avcapturesystempressurefactornone.md)
  System pressure is currently nominal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/systempressurestate-swift.class/factors-swift.struct/cameratemperature)*