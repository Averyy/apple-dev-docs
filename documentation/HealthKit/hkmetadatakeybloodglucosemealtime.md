# HKMetadataKeyBloodGlucoseMealTime

**Framework**: HealthKit  
**Kind**: var

A key that indicates the relative timing of a blood glucose reading to a meal.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
let HKMetadataKeyBloodGlucoseMealTime: String
```

#### Discussion

Set this key on a [`bloodGlucose`](hkquantitytypeidentifier/bloodglucose.md) sample. Set it’s value to an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object containing a [`HKBloodGlucoseMealTime`](hkbloodglucosemealtime.md) value.Medical professionals can use the relative meal time to help determine the acceptable range for a blood glucose reading. If your app requires more precise timing or additional information about the meal’s composition, create  samples to record those details (for example, a [`dietaryCarbohydrates`](hkquantitytypeidentifier/dietarycarbohydrates.md) sample with the exact meal time).

## Topics

### Valid Values
- [enum HKBloodGlucoseMealTime](hkbloodglucosemealtime.md)
  Constants indicating the timing of a blood glucose sample relative to a meal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkmetadatakeybloodglucosemealtime)*