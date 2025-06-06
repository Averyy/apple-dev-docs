# init(predicates:anchor:limit:)

**Framework**: HealthKit  
**Kind**: init

Creates an anchored object query descriptor.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 13.0+
- visionOS ?+
- watchOS 8.5+

## Declaration

```swift
init(predicates: [HKSamplePredicate<Sample>], anchor: HKQueryAnchor?, limit: Int? = nil)
```

#### Discussion

The system sets the descriptor’s `HKAnchoredObjectQueryDescriptor/Output` type based on the `predicates` parameter.

## Parameters

- `predicates`: An array of sample predicates that define the type of data that the query returns. To query for multiple types of data, provide a sample predicate for each type.
- `anchor`: An anchor that a previous anchored object query returned. The anchor object corresponds to the last object that the previous query returned. The current query returns only samples and deleted objects newer than the anchor. Pass   to receive all the matching samples and recently deleted objects currently in the HealthKit store.
- `limit`: An optional value that specifies the maximum number of samples that the query returns. If you don’t specify the limit, the system returns all matching samples in the HealthKit store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkanchoredobjectquerydescriptor/init(predicates:anchor:limit:))*