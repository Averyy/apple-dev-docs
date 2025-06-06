# HKMetadataKeyLapLength

**Framework**: HealthKit  
**Kind**: var

A key that indicates the length of a lap during a workout.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
let HKMetadataKeyLapLength: String
```

#### Discussion

Set this key on  a workout, workout segment, or a quantity sample that represents distance. Set its value to an [`HKQuantity`](hkquantity.md) object that uses length units (described in [`HKUnit`](hkunit.md)).

## See Also

- [let HKMetadataKeySwimmingLocationType: String](hkmetadatakeyswimminglocationtype.md)
  A key that indicates the location for a swimming workout.
- [let HKMetadataKeySwimmingStrokeStyle: String](hkmetadatakeyswimmingstrokestyle.md)
  A key that indicates the predominant stroke style for a lap of swimming.
- [let HKMetadataKeySWOLFScore: String](hkmetadatakeyswolfscore.md)
- [let HKMetadataKeyWaterSalinity: String](hkmetadatakeywatersalinity.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkmetadatakeylaplength)*