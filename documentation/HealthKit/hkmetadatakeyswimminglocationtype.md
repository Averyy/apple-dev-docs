# HKMetadataKeySwimmingLocationType

**Framework**: HealthKit  
**Kind**: var

A key that indicates the location for a swimming workout.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
let HKMetadataKeySwimmingLocationType: String
```

#### Discussion

Set this key on a workout object that represents swimming. Set its value to an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object that contains a valid value from the [`HKWorkoutSwimmingLocationType`](hkworkoutswimminglocationtype.md) enumeration.

## Topics

### Valid Swimming Locations
- [enum HKWorkoutSwimmingLocationType](hkworkoutswimminglocationtype.md)
  The possible locations for swimming.

## See Also

- [let HKMetadataKeySwimmingStrokeStyle: String](hkmetadatakeyswimmingstrokestyle.md)
  A key that indicates the predominant stroke style for a lap of swimming.
- [let HKMetadataKeyLapLength: String](hkmetadatakeylaplength.md)
  A key that indicates the length of a lap during a workout.
- [let HKMetadataKeySWOLFScore: String](hkmetadatakeyswolfscore.md)
- [let HKMetadataKeyWaterSalinity: String](hkmetadatakeywatersalinity.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkmetadatakeyswimminglocationtype)*