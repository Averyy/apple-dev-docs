# objects

**Framework**: HealthKit  
**Kind**: property

The set of sample objects that make up the correlation.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var objects: Set<HKSample> { get }
```

#### Discussion

This property contains the quantity and category samples that are grouped into this correlation. Blood pressure correlations always include two quantity samples that represent the systolic and diastolic values. In contrast, food correlations can contain a wide range of dietary information about the food, including information about the fat, protein, carbohydrates, energy, and vitamins consumed.

## See Also

- [var correlationType: HKCorrelationType](hkcorrelation/correlationtype.md)
  The type for this correlation.
- [func objects(for: HKObjectType) -> Set<HKSample>](hkcorrelation/objects(for:).md)
  Returns a set containing all the objects of the specified type in the correlation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkcorrelation/objects)*