# init(quantityType:predicate:quantityHandler:)

**Framework**: HealthKit  
**Kind**: init

Creates a new query for a series of the specified quantity type.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
init(quantityType: HKQuantityType, predicate: NSPredicate?, quantityHandler: @escaping (HKQuantitySeriesSampleQuery, HKQuantity?, DateInterval?, HKQuantitySample?, Bool, (any Error)?) -> Void)
```

#### Discussion

HealthKit returns quantities in ascending order, based on their start date.

## Parameters

- `quantityType`: The quantity type.
- `predicate`: A predicate used to filter the results. To query for all the quantity objects for a specific  , see  .
- `quantityHandler`: A handler called by the query with the results. The query calls the block multiple times until either the   parameter is  , or you call the HealthKit store’s   method. The handler takes the following arguments:

## See Also

- [var includeSample: Bool](hkquantityseriessamplequery/includesample.md)
  A Boolean value that determines whether the query should return the series sample.
- [var orderByQuantitySampleStartDate: Bool](hkquantityseriessamplequery/orderbyquantitysamplestartdate.md)
  A Boolean value that determines whether the query groups the results based on the quantity sample’s start date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquantityseriessamplequery/init(quantitytype:predicate:quantityhandler:))*