# predicates

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

An array of sample predicates that define the type of data that the query returns.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 13.0+
- visionOS
- watchOS 8.5+

## Declaration

```swift
var predicates: [HKSamplePredicate<Sample>] { get set }
```

#### Discussion

To query for multiple types of data, provide a sample predicate for each type. If your [`HKSamplePredicate`](../hksamplepredicate.md) instances return different [`HKSample`](../hksample.md) subclasses, use [`sample(type:predicate:)`](../hksamplepredicate/sample%28type,predicate%29.md) to create the sample predicates.

## See Also

### Accessing Query Properties
- [var limit: Int?](./limit.md)
  The maximum number of samples that the query returns.
- [var sortDescriptors: [SortDescriptor<Sample>]](./sortdescriptors.md)
  An array that specifies the order of the results that the query returns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hksamplequerydescriptor/predicates)*