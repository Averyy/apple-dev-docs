# limit

**Framework**: HealthKit  
**Kind**: property

The maximum number of samples that the query returns.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 13.0+
- visionOS ?+
- watchOS 8.5+

## Declaration

```swift
var limit: Int?
```

#### Discussion

If the limit is `nil`, the system returns all matching samples in the HealthKit store.

## See Also

- [var predicates: [HKSamplePredicate<Sample>]](hkanchoredobjectquerydescriptor/predicates.md)
  A predicate that limits the results that the query returns.
- [var anchor: HKQueryAnchor?](hkanchoredobjectquerydescriptor/anchor.md)
  An anchor that a previous anchored object query returned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkanchoredobjectquerydescriptor/limit)*