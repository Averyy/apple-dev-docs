# anchor

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

An anchor that a previous anchored object query returned.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 13.0+
- visionOS
- watchOS 8.5+

## Declaration

```swift
var anchor: HKQueryAnchor?
```

## Discussion

The anchor object corresponds to the last object that the previous query returned. The current query returns only samples and deleted objects newer than the anchor. Pass `nil` to receive all the matching samples and recently deleted objects currently in the HealthKit store.

## See Also

### Accessing Query Properties
- [var predicates: [HKSamplePredicate<Sample>]](./predicates.md)
  A predicate that limits the results that the query returns.
- [var limit: Int?](./limit.md)
  The maximum number of samples that the query returns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkanchoredobjectquerydescriptor/anchor)*