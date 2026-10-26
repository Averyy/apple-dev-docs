# SRWristTemperature.Condition

**Framework**: SensorKit  
**Kind**: struct  
**Role**: Structure

The user activities with the watch that can impact the temperature measurement.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
struct Condition
```

```c
enum SRWristTemperatureCondition : NSUInteger;
```

## Topics

### Conditions
- [static var offWrist: SRWristTemperature.Condition](./condition-swift.struct/offwrist.md)
  The watch being off the wrist impacts the accuracy.
- [static var onCharger: SRWristTemperature.Condition](./condition-swift.struct/oncharger.md)
  The watch being on the charger impacts the accuracy.
- [static var inMotion: SRWristTemperature.Condition](./condition-swift.struct/inmotion.md)
  The watch being in motion impacts the accuracy.
### Creating conditions
- [init(rawValue: UInt)](./condition-swift.struct/init%28rawvalue%29.md)
  Creates and returns a new structure with the specified value.
### Enumeration Cases
- [SRWristTemperatureConditionNone](../srwristtemperaturecondition/srwristtemperatureconditionnone.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Determining the accuracy
- [var condition: SRWristTemperature.Condition](./condition-swift.property.md)
  The condition of the measurement that impacts its accuracy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srwristtemperature/condition-swift.struct)*