# HKMetadataKeySwimmingStrokeStyle

**Framework**: HealthKit  
**Kind**: var

A key that indicates the predominant stroke style for a lap of swimming.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
let HKMetadataKeySwimmingStrokeStyle: String
```

#### Discussion

Set this key on workout lap events. Set its value to an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object that contains a valid value from the  [`HKSwimmingStrokeStyle`](hkswimmingstrokestyle.md) enumeration.

## Topics

### Valid Stroke Styles
- [enum HKSwimmingStrokeStyle](hkswimmingstrokestyle.md)
  The style of stroke while swimming.

## See Also

- [let HKMetadataKeySwimmingLocationType: String](hkmetadatakeyswimminglocationtype.md)
  A key that indicates the location for a swimming workout.
- [let HKMetadataKeyLapLength: String](hkmetadatakeylaplength.md)
  A key that indicates the length of a lap during a workout.
- [let HKMetadataKeySWOLFScore: String](hkmetadatakeyswolfscore.md)
- [let HKMetadataKeyWaterSalinity: String](hkmetadatakeywatersalinity.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkmetadatakeyswimmingstrokestyle)*