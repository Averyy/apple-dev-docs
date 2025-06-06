# food

**Framework**: HealthKit  
**Kind**: property

Food correlation types combine any number of nutritional samples into a single food object.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static let food: HKCorrelationTypeIdentifier
```

#### Discussion

When creating food samples, specify the type of food using the [`HKMetadataKeyFoodType`](hkmetadatakeyfoodtype.md) metadata key.

## See Also

- [struct HKCorrelationTypeIdentifier](hkcorrelationtypeidentifier.md)
  The identifiers that create correlation type objects.
- [class HKCorrelationType](hkcorrelationtype.md)
  A type that identifies samples that group multiple subsamples.
- [class HKCorrelation](hkcorrelation.md)
  A sample that groups multiple related samples into a single entry.
- [let HKMetadataKeyFoodType: String](hkmetadatakeyfoodtype.md)
  The type of food that the HealthKit object represents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkcorrelationtypeidentifier/food)*