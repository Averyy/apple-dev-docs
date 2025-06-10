# HKMetadataKeyVO2MaxValue

**Framework**: HealthKit  
**Kind**: var

The maximum oxygen consumption rate during exercise of increasing intensity.

**Availability**:
- iOS 14.3+
- iPadOS 14.3+
- Mac Catalyst 14.3+
- macOS 13.0+
- visionOS 1.0+
- watchOS 7.2+

## Declaration

```swift
let HKMetadataKeyVO2MaxValue: String
```

#### Discussion

The system sets this key on [`lowCardioFitnessEvent`](hkcategorytypeidentifier/lowcardiofitnessevent.md) samples. It contains the value of the VO2 max measurement that triggered the event. The value of this key is an [`HKQuantity`](hkquantity.md) object with a unit of `ml/(kg*min)`. For more information on working with complex units, see [`unitMultiplied(by:)`](hkunit/unitmultiplied(by:).md), [`unitDivided(by:)`](hkunit/unitdivided(by:).md), and [`init(from:)`](hkunit/init(from:)-9qont.md).

## See Also

- [let HKMetadataKeyLowCardioFitnessEventThreshold: String](hkmetadatakeylowcardiofitnesseventthreshold.md)
  The VO2 max threshold used to categorize low-level cardio fitness events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkmetadatakeyvo2maxvalue)*