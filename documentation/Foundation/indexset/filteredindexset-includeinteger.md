# filteredIndexSet(includeInteger:)

**Framework**: Foundation  
**Kind**: method

Returns an IndexSet filtered according to the result of `includeInteger`.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func filteredIndexSet(includeInteger: (IndexSet.Element) throws -> Bool) rethrows -> IndexSet
```

## Parameters

- `includeInteger`: The predicate which decides if an integer will be included in the result or not.

## See Also

- [func filteredIndexSet(in: Range<IndexSet.Element>, includeInteger: (IndexSet.Element) throws -> Bool) rethrows -> IndexSet](indexset/filteredindexset(in:includeinteger:)-6cdvc.md)
  Returns an IndexSet filtered according to the result of `includeInteger`.
- [func filteredIndexSet(in: ClosedRange<IndexSet.Element>, includeInteger: (IndexSet.Element) throws -> Bool) rethrows -> IndexSet](indexset/filteredindexset(in:includeinteger:)-9dn86.md)
  Returns an IndexSet filtered according to the result of `includeInteger`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/indexset/filteredindexset(includeinteger:))*