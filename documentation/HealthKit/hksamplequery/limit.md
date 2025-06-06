# limit

**Framework**: HealthKit  
**Kind**: property

The maximum number of samples that this query returns.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var limit: Int { get }
```

#### Discussion

This property’s value sets the maximum number of samples that the query returns upon completion.

If you are specifically interested in retrieving only new samples (samples added since the last query), consider using an [`HKAnchoredObjectQuery`](hkanchoredobjectquery.md) query instead.

## See Also

- [var sortDescriptors: [NSSortDescriptor]?](hksamplequery/sortdescriptors.md)
  The sort descriptors that specify the order of the results returned by this query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hksamplequery/limit)*