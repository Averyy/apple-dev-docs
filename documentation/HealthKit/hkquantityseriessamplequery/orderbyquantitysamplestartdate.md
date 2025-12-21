# orderByQuantitySampleStartDate

**Framework**: HealthKit  
**Kind**: property

A Boolean value that determines whether the query groups the results based on the quantity sample’s start date.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var orderByQuantitySampleStartDate: Bool { get set }
```

#### Discussion

By default the query returns all the quantities in ascending order based on their start date. If you set this property to [`true`](https://developer.apple.com/documentation/Swift/true), HealthKit first sorts the matching [`HKQuantitySample`](hkquantitysample.md) objects by their [`startDate`](hksample/startdate.md) parameter. Then, for each sample, it returns all the quantity objects in ascending order. If the sample objects overlap, then the quantities may not appear in ascending order when switching from one sample to the next.

## See Also

- [init(quantityType: HKQuantityType, predicate: NSPredicate?, quantityHandler: (HKQuantitySeriesSampleQuery, HKQuantity?, DateInterval?, HKQuantitySample?, Bool, (any Error)?) -> Void)](hkquantityseriessamplequery/init(quantitytype:predicate:quantityhandler:).md)
  Creates a new query for a series of the specified quantity type.
- [var includeSample: Bool](hkquantityseriessamplequery/includesample.md)
  A Boolean value that determines whether the query should return the series sample.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquantityseriessamplequery/orderbyquantitysamplestartdate)*