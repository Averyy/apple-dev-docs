# includeSample

**Framework**: HealthKit  
**Kind**: property

A Boolean value that determines whether the query should return the series sample.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var includeSample: Bool { get set }
```

#### Discussion

By default, a quantity series sample only returns the individual quantity objects that make up the series—not the [`HKQuantitySample`](hkquantitysample.md) object that represents the entire series. Set this parameter to [`true`](https://developer.apple.com/documentation/Foundation/NSExpression/true) to have the query also return the quantity sample object for the series.

> **Note**:  This may introduce a performance cost for the query.

## See Also

- [init(quantityType: HKQuantityType, predicate: NSPredicate?, quantityHandler: (HKQuantitySeriesSampleQuery, HKQuantity?, DateInterval?, HKQuantitySample?, Bool, (any Error)?) -> Void)](hkquantityseriessamplequery/init(quantitytype:predicate:quantityhandler:).md)
  Creates a new query for a series of the specified quantity type.
- [var orderByQuantitySampleStartDate: Bool](hkquantityseriessamplequery/orderbyquantitysamplestartdate.md)
  A Boolean value that determines whether the query groups the results based on the quantity sample’s start date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquantityseriessamplequery/includesample)*