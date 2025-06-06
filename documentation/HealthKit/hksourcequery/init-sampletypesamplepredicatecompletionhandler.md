# init(sampleType:samplePredicate:completionHandler:)

**Framework**: HealthKit  
**Kind**: init

Instantiates and returns a source query.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
init(sampleType: HKSampleType, samplePredicate objectPredicate: NSPredicate?, completionHandler: @escaping (HKSourceQuery, Set<HKSource>?, (any Error)?) -> Void)
```

## Mentions

- [Executing Source Queries](executing-source-queries.md)

#### Return Value

A newly initialized sample query object.

#### Discussion

After instantiating the query, call the [`HKHealthStore`](hkhealthstore.md) class’s [`execute(_:)`](hkhealthstore/execute(_:).md) method to run this query. Queries run on an anonymous background queue. As soon as the query is complete, the results handler is executed on the same background queue (but not necessarily on the same thread).

## Parameters

- `sampleType`: The type of sample to search for. This query supports all sample types. Specifically, you can pass any concrete subclass of the   class (the  ,  ,  ,  and   classes).
- `objectPredicate`: A predicate that limits the samples matched by the query. Pass   if you want to receive the sources for all the samples of the specified type.
- `completionHandler`: A block that is called when the query finishes executing. This block takes the following parameters:

## See Also

- [Executing Source Queries](executing-source-queries.md)
  Create and run source queries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hksourcequery/init(sampletype:samplepredicate:completionhandler:))*