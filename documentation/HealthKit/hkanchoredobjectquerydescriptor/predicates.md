# predicates

**Framework**: HealthKit  
**Kind**: property

A predicate that limits the results that the query returns.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 13.0+
- visionOS ?+
- watchOS 8.5+

## Declaration

```swift
var predicates: [HKSamplePredicate<Sample>] { get set }
```

## See Also

- [var anchor: HKQueryAnchor?](hkanchoredobjectquerydescriptor/anchor.md)
  An anchor that a previous anchored object query returned.
- [var limit: Int?](hkanchoredobjectquerydescriptor/limit.md)
  The maximum number of samples that the query returns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkanchoredobjectquerydescriptor/predicates)*