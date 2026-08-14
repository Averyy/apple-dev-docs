# AVCaptureDevice.SystemPressureState.Factors

**Framework**: AVFoundation  
**Kind**: struct

A structure that defines the factors affecting capture system performance.

**Availability**:
- iOS 11.1+
- iPadOS 11.1+
- Mac Catalyst 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
struct Factors
```

## Topics

### System pressure factors
- [static var systemTemperature: AVCaptureDevice.SystemPressureState.Factors](avcapturedevice/systempressurestate-swift.class/factors-swift.struct/systemtemperature.md)
  The entire system is under elevated thermal load.
- [static var peakPower: AVCaptureDevice.SystemPressureState.Factors](avcapturedevice/systempressurestate-swift.class/factors-swift.struct/peakpower.md)
  The system’s peak power requirements exceed the battery’s current capacity.
- [static var depthModuleTemperature: AVCaptureDevice.SystemPressureState.Factors](avcapturedevice/systempressurestate-swift.class/factors-swift.struct/depthmoduletemperature.md)
  The module capturing depth information is operating at an elevated temperature.
- [static var cameraTemperature: AVCaptureDevice.SystemPressureState.Factors](avcapturedevice/systempressurestate-swift.class/factors-swift.struct/cameratemperature.md)
  The camera module is operating at an elevated temperature.
### Initializers
- [init(rawValue: UInt)](avcapturedevice/systempressurestate-swift.class/factors-swift.struct/init(rawvalue:).md)
  Creates a system pressure factor from its raw string value.
### Type Properties
- [static var batteryStress: AVCaptureDevice.SystemPressureState.Factors](avcapturedevice/systempressurestate-swift.class/factors-swift.struct/batterystress.md)
  Indicates that under the current battery conditions, the device will shut down within 30 seconds if system load is not reduced.

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SetAlgebra](../swift/setalgebra.md)

## See Also

- [var factors: AVCaptureDevice.SystemPressureState.Factors](avcapturedevice/systempressurestate-swift.class/factors-swift.property.md)
  The set of underlying causes for the system pressure level.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/systempressurestate-swift.class/factors-swift.struct)*