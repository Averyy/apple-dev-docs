---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/carestorefetchedresults"
framework: "CareKit/CareKit"
---

# CareStoreFetchedResults

**Framework**: CareKit/CareKit  
**Kind**: struct  
**Role**: Structure

A batch of results fetched from the store.

## Declaration

```swift
struct CareStoreFetchedResults<Result, Query>
```

## Topics

### Instance Properties
- [var endIndex: Int](./carestorefetchedresults/endindex.md)
- [var query: Query](./carestorefetchedresults/query.md)
  A query that matches data in the store during a fetch request.
- [var startIndex: Int](./carestorefetchedresults/startindex.md)
### Subscripts
- [subscript(Int) -> CareStoreFetchedResult<Result>](./carestorefetchedresults/subscript%28_%29.md)
### Type Aliases
- [CareStoreFetchedResults.Element](./carestorefetchedresults/element.md)
- [CareStoreFetchedResults.Index](./carestorefetchedresults/index.md)
- [CareStoreFetchedResults.Indices](./carestorefetchedresults/indices.md)
- [CareStoreFetchedResults.Iterator](./carestorefetchedresults/iterator.md)
- [CareStoreFetchedResults.SubSequence](./carestorefetchedresults/subsequence.md)
### Default Implementations
- [BidirectionalCollection Implementations](./carestorefetchedresults/bidirectionalcollection-implementations.md)
- [Collection Implementations](./carestorefetchedresults/collection-implementations.md)
- [RandomAccessCollection Implementations](./carestorefetchedresults/randomaccesscollection-implementations.md)
- [Sequence Implementations](./carestorefetchedresults/sequence-implementations.md)

## Relationships

### Conforms To
- Swift.BidirectionalCollection
- Swift.Collection
- Swift.RandomAccessCollection
- Swift.Sequence

## See Also

### Displaying synchronized care data in SwiftUI
- [struct CareStoreFetchRequest](./carestorefetchrequest.md)
  A property wrapper useful for streaming data from a CareKit store.
- [struct CareStoreFetchedResult](./carestorefetchedresult.md)
  A result fetched from the store.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/carestorefetchedresults)*