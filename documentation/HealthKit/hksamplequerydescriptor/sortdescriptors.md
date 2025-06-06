# sortDescriptors

**Framework**: HealthKit  
**Kind**: property

An array that specifies the order of the results that the query returns.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 13.0+
- visionOS ?+
- watchOS 8.5+

## Declaration

```swift
var sortDescriptors: [SortDescriptor<Sample>]
```

#### Discussion

The system applies the sort descriptors in order. The later descriptors sort any items that the earlier sort descriptors considered equal. If you don’t need the results in a specific order, pass an empty array.

## See Also

- [var limit: Int?](hksamplequerydescriptor/limit.md)
  The maximum number of samples that the query returns.
- [var predicates: [HKSamplePredicate<Sample>]](hksamplequerydescriptor/predicates.md)
  An array of sample predicates that define the type of data that the query returns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hksamplequerydescriptor/sortdescriptors)*