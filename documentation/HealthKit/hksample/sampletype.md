# sampleType

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

The sample type.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
@NSCopying
var sampleType: HKSampleType { get }
```

```objc
@property (copy, readonly) HKSampleType * sampleType;
```

#### Discussion

This property contains a concrete sample type that corresponds with this sample’s concrete class. For example, if the sample is an [`HKQuantitySample`](../hkquantitysample.md) instance, it returns an [`HKQuantityType`](../hkquantitytype.md) object.

## See Also

### Related Documentation
- [var quantityType: HKQuantityType](../hkquantitysample/quantitytype.md)
  The quantity type for this sample.
- [var correlationType: HKCorrelationType](../hkcorrelation/correlationtype.md)
  The type for this correlation.
- [var categoryType: HKCategoryType](../hkcategorysample/categorytype.md)
  The category type for this sample.
### Accessing the Sample’s Data
- [var startDate: Date](./startdate.md)
  The sample’s start date.
- [var endDate: Date](./enddate.md)
  The sample’s end date.
- [var hasUndeterminedDuration: Bool](./hasundeterminedduration.md)
  Indicates whether the sample has an unknown duration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hksample/sampletype)*