# cameraTemperature

**Framework**: AVFoundation  
**Kind**: property

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

## See Also

- [static var systemTemperature: AVCaptureDevice.SystemPressureState.Factors](avcapturedevice/systempressurestate-swift.class/factors-swift.struct/systemtemperature.md)
  The entire system is under elevated thermal load.
- [static var peakPower: AVCaptureDevice.SystemPressureState.Factors](avcapturedevice/systempressurestate-swift.class/factors-swift.struct/peakpower.md)
  The system’s peak power requirements exceed the battery’s current capacity.
- [static var depthModuleTemperature: AVCaptureDevice.SystemPressureState.Factors](avcapturedevice/systempressurestate-swift.class/factors-swift.struct/depthmoduletemperature.md)
  The module capturing depth information is operating at an elevated temperature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/systempressurestate-swift.class/factors-swift.struct/cameratemperature)*