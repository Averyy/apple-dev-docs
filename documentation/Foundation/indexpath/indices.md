# IndexPath.Indices

**Framework**: Foundation  
**Kind**: typealias  
**Role**: Type Alias

A type that represents a group of nodes in an index path.

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
typealias Indices = DefaultIndices<IndexPath>
```

## See Also

### Manipulating Indexes
- [IndexPath.Index](./index.md)
  A type that points to a particular node in an index path, similar to an array index.
- [var startIndex: IndexPath.Index](./startindex.md)
  The index of the first node in the index path.
- [var endIndex: IndexPath.Index](./endindex.md)
  One past the index of the last node in the index path.
- [func index(after: IndexPath.Index) -> IndexPath.Index](./index%28after%29.md)
  Returns the index that follows the given index.
- [func index(before: IndexPath.Index) -> IndexPath.Index](./index%28before%29.md)
  Returns the index that precedes the given index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/indexpath/indices)*