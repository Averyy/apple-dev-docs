# HKMetadataKeyFoodType

**Framework**: HealthKit  
**Kind**: var

The type of food that the HealthKit object represents.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let HKMetadataKeyFoodType: String
```

#### Discussion

This key takes a string value. Food objects are usually [`food`](hkcorrelationtypeidentifier/food.md) samples containing any number of `Nutrition Identifiers` samples.

## See Also

- [static let food: HKCorrelationTypeIdentifier](hkcorrelationtypeidentifier/food.md)
  Food correlation types combine any number of nutritional samples into a single food object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkmetadatakeyfoodtype)*