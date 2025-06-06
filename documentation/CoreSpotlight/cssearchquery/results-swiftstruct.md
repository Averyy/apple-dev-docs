# CSSearchQuery.Results

**Framework**: Core Spotlight  
**Kind**: struct

An asynchronous sequence that contains the results that match the query string.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
struct Results
```

#### Discussion

A `CSSearchQuery/Results-swift.struct` structure contains the results of a query. Fetch this structure from the [`results`](cssearchquery/results-swift.property.md) property of your query object to execute the query automatically and begin the delivery of the results. Use each instance of the structure to get the details for a single result.

For more information about how to use this structure, see the [`results`](cssearchquery/results-swift.property.md) property.

## Topics

### Structures
- [CSSearchQuery.Results.Item](cssearchquery/results-swift.struct/item.md)
- [CSSearchQuery.Results.Iterator](cssearchquery/results-swift.struct/iterator.md)

## Relationships

### Conforms To
- [AsyncSequence](../Swift/AsyncSequence.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var results: CSSearchQuery.Results](cssearchquery/results-swift.property.md)
  The results that match the current query string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchquery/results-swift.struct)*