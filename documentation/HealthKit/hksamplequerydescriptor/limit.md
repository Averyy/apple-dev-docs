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

If the `limit` is `nil`, the system returns all matching samples in the HealthKit store.

## See Also

- [var predicates: [HKSamplePredicate<Sample>]](hksamplequerydescriptor/predicates.md)
  An array of sample predicates that define the type of data that the query returns.
- [var sortDescriptors: [SortDescriptor<Sample>]](hksamplequerydescriptor/sortdescriptors.md)
  An array that specifies the order of the results that the query returns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hksamplequerydescriptor/limit)*