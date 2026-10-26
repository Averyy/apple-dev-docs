# AVCaptureDevice.SystemPressureState.Factors

**Framework**: AVFoundation  
**Kind**: struct  
**Role**: Structure

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

```c
enum AVCaptureSystemPressureFactors : NSUInteger;
```

## Topics

### System pressure factors
- [static var systemTemperature: AVCaptureDevice.SystemPressureState.Factors](./factors-swift.struct/systemtemperature.md)
  The entire system is under elevated thermal load.
- [static var peakPower: AVCaptureDevice.SystemPressureState.Factors](./factors-swift.struct/peakpower.md)
  The system’s peak power requirements exceed the battery’s current capacity.
- [static var depthModuleTemperature: AVCaptureDevice.SystemPressureState.Factors](./factors-swift.struct/depthmoduletemperature.md)
  The module capturing depth information is operating at an elevated temperature.
- [static var cameraTemperature: AVCaptureDevice.SystemPressureState.Factors](./factors-swift.struct/cameratemperature.md)
  The camera module is operating at an elevated temperature.
- [AVCaptureSystemPressureFactorNone](../../avcapturesystempressurefactors/avcapturesystempressurefactornone.md)
  System pressure is currently nominal.
### Initializers
- [init(rawValue: UInt)](./factors-swift.struct/init%28rawvalue%29.md)
  Creates a system pressure factor from its raw string value.
### Type Properties
- [static var batteryStress: AVCaptureDevice.SystemPressureState.Factors](./factors-swift.struct/batterystress.md)
  Indicates that under the current battery conditions, the device will shut down within 30 seconds if system load is not reduced.

## Relationships

### Conforms To
- [BitwiseCopyable](../../../Swift/bitwisecopyable.md)
- [Equatable](../../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../../Swift/optionset.md)
- [RawRepresentable](../../../Swift/rawrepresentable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)
- [SetAlgebra](../../../Swift/setalgebra.md)

## See Also

### Contributing factors
- [var factors: AVCaptureDevice.SystemPressureState.Factors](./factors-swift.property.md)
  The set of underlying causes for the system pressure level.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/systempressurestate-swift.class/factors-swift.struct)*