# HKObjectQueryNoLimit

**Framework**: HealthKit  
**Kind**: var  
**Role**: Global Variable

A value indicating that the query returns all the matching samples in the HealthKit store.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS
- watchOS

## Declaration

```swift
var HKObjectQueryNoLimit: Int { get }
```

```c
static const NSUInteger HKObjectQueryNoLimit;
```

## See Also

### Creating Anchored Object Queries
- [Executing Anchored Object Queries](./executing-anchored-object-queries.md)
  Create and run an anchored object query.
- [init(type: HKSampleType, predicate: NSPredicate?, anchor: HKQueryAnchor?, limit: Int, resultsHandler: (HKAnchoredObjectQuery, [HKSample]?, [HKDeletedObject]?, HKQueryAnchor?, (any Error)?) -> Void)](./hkanchoredobjectquery/init%28type,predicate,anchor,limit,resultshandler%29.md)
  Initializes a new anchored object query.
- [init(queryDescriptors: [HKQueryDescriptor], anchor: HKQueryAnchor?, limit: Int, resultsHandler: (HKAnchoredObjectQuery, [HKSample]?, [HKDeletedObject]?, HKQueryAnchor?, (any Error)?) -> Void)](./hkanchoredobjectquery/init%28querydescriptors,anchor,limit,resultshandler%29.md)
  Creates an anchored object query that matches any of the query descriptors you provided.
- [init(type: HKSampleType, predicate: NSPredicate?, anchor: Int, limit: Int, completionHandler: (HKAnchoredObjectQuery, [HKSample]?, Int, (any Error)?) -> Void)](./hkanchoredobjectquery/init%28type,predicate,anchor,limit,completionhandler%29.md)
  Initializes a new anchored object query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkobjectquerynolimit)*