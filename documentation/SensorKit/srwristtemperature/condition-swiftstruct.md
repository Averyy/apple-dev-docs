# SRWristTemperature.Condition

**Framework**: SensorKit  
**Kind**: struct

The user activities with the watch that can impact the temperature measurement.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
struct Condition
```

## Topics

### Conditions
- [static var offWrist: SRWristTemperature.Condition](srwristtemperature/condition-swift.struct/offwrist.md)
  The watch being off the wrist impacts the accuracy.
- [static var onCharger: SRWristTemperature.Condition](srwristtemperature/condition-swift.struct/oncharger.md)
  The watch being on the charger impacts the accuracy.
- [static var inMotion: SRWristTemperature.Condition](srwristtemperature/condition-swift.struct/inmotion.md)
  The watch being in motion impacts the accuracy.
### Creating conditions
- [init(rawValue: UInt)](srwristtemperature/condition-swift.struct/init(rawvalue:).md)
  Creates and returns a new structure with the specified value.

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

- [var condition: SRWristTemperature.Condition](srwristtemperature/condition-swift.property.md)
  The condition of the measurement that impacts its accuracy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srwristtemperature/condition-swift.struct)*