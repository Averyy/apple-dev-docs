# init(type:predicate:samplePredicates:completion:)

**Framework**: HealthKit  
**Kind**: init

Instantiates and returns a correlation query.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(type correlationType: HKCorrelationType, predicate: NSPredicate?, samplePredicates: [HKSampleType : NSPredicate]?, completion: @escaping (HKCorrelationQuery, [HKCorrelation]?, (any Error)?) -> Void)
```

#### Return Value

A newly initialized correlation object.

#### Discussion

After instantiating the query, run it by calling the [`HKHealthStore`](hkhealthstore.md) class’s [`execute(_:)`](hkhealthstore/execute(_:).md) method. Queries run on a background thread. As soon as the query is complete, the results handler is executed on the background thread. You typically dispatch these results to the main thread to update the user interface.

## Parameters

- `correlationType`: The type of correlation to search for.
- `predicate`: A predicate that limits the results returned by the query. This predicate is compared with the correlation objects. Pass   to receive all the correlations of the specified type.
- `samplePredicates`: Three things must be true if this query is going to match a correlation:
- `completion`: A block that is called when the query finishes executing. This block takes the following parameters:


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkcorrelationquery/init(type:predicate:samplepredicates:completion:))*