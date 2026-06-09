# IndexPath.Index

**Framework**: Foundation  
**Kind**: typealias

A type that points to a particular node in an index path, similar to an array index.

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
typealias Index = Array<Int>.Index
```

## See Also

- [var startIndex: IndexPath.Index](indexpath/startindex.md)
  The index of the first node in the index path.
- [var endIndex: IndexPath.Index](indexpath/endindex.md)
  One past the index of the last node in the index path.
- [func index(after: IndexPath.Index) -> IndexPath.Index](indexpath/index(after:).md)
  Returns the index that follows the given index.
- [func index(before: IndexPath.Index) -> IndexPath.Index](indexpath/index(before:).md)
  Returns the index that precedes the given index.
- [IndexPath.Indices](indexpath/indices.md)
  A type that represents a group of nodes in an index path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/indexpath/index)*