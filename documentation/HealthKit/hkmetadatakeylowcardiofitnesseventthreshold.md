# HKMetadataKeyLowCardioFitnessEventThreshold

**Framework**: HealthKit  
**Kind**: var

The VO2 max threshold used to categorize low-level cardio fitness events.

**Availability**:
- iOS 14.3+
- iPadOS 14.3+
- Mac Catalyst 14.3+
- macOS 13.0+
- visionOS 1.0+
- watchOS 7.2+

## Declaration

```swift
let HKMetadataKeyLowCardioFitnessEventThreshold: String
```

#### Discussion

The system sets this key on [`lowCardioFitnessEvent`](hkcategorytypeidentifier/lowcardiofitnessevent.md) samples. It contains the threshold value for the user’s VO2 max measurements. The threshold value varies depending on certain parameters and physical characteristics, such as the user’s age.

A low-cardio fitness event indicates a period of time when the user’s VO2 max measurements consistently fall below the defined value. The system triggers this event approximately once every four months.

The value of this key is an [`HKQuantity`](hkquantity.md) object with a unit of `ml/(kg*min)`. For more information on working with complex units, see [`unitMultiplied(by:)`](hkunit/unitmultiplied(by:).md), [`unitDivided(by:)`](hkunit/unitdivided(by:).md), and [`init(from:)`](hkunit/init(from:)-9qont.md).

## See Also

- [let HKMetadataKeyVO2MaxValue: String](hkmetadatakeyvo2maxvalue.md)
  The maximum oxygen consumption rate during exercise of increasing intensity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkmetadatakeylowcardiofitnesseventthreshold)*