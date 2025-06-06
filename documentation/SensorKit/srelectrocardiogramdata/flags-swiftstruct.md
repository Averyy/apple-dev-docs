# SRElectrocardiogramData.Flags

**Framework**: SensorKit  
**Kind**: struct

Sensor context or events that occur during a sample ECG data reading.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
struct Flags
```

## Topics

### Getting context or events
- [static var crownTouched: SRElectrocardiogramData.Flags](srelectrocardiogramdata/flags-swift.struct/crowntouched.md)
  The system records the ECG data when the person touches the crown.
- [static var signalInvalid: SRElectrocardiogramData.Flags](srelectrocardiogramdata/flags-swift.struct/signalinvalid.md)
  An invalid sensor signal occurs in the ECG data.
### Initializing flags
- [init(rawValue: UInt)](srelectrocardiogramdata/flags-swift.struct/init(rawvalue:).md)
  Initializes an ECG flags structure.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [var flags: SRElectrocardiogramData.Flags](srelectrocardiogramdata/flags-swift.property.md)
- [var value: Measurement<UnitElectricPotentialDifference>](srelectrocardiogramdata/value.md)
  The electrocardiogram data in microvolts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srelectrocardiogramdata/flags-swift.struct)*