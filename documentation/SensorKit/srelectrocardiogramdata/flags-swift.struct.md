# SRElectrocardiogramData.Flags

**Framework**: SensorKit  
**Kind**: struct  
**Role**: Structure

Sensor context or events that occur during a sample ECG data reading.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
struct Flags
```

```c
enum SRElectrocardiogramDataFlags : NSUInteger;
```

## Topics

### Getting context or events
- [static var crownTouched: SRElectrocardiogramData.Flags](./flags-swift.struct/crowntouched.md)
  The system records the ECG data when the person touches the crown.
- [static var signalInvalid: SRElectrocardiogramData.Flags](./flags-swift.struct/signalinvalid.md)
  An invalid sensor signal occurs in the ECG data.
### Initializing flags
- [init(rawValue: UInt)](./flags-swift.struct/init%28rawvalue%29.md)
  Initializes an ECG flags structure.
### Enumeration Cases
- [SRElectrocardiogramDataFlagsNone](../srelectrocardiogramdataflags/srelectrocardiogramdataflagsnone.md)
  Flag that indicates no context or events occur.

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

### Getting electrocardiogram details
- [var flags: SRElectrocardiogramData.Flags](./flags-swift.property.md)
- [var value: Measurement<UnitElectricPotentialDifference>](./value.md)
  The electrocardiogram data in microvolts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srelectrocardiogramdata/flags-swift.struct)*