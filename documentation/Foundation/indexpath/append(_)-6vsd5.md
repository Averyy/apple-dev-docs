# append(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Appends an array of elements to this index path as additional nodes.

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
mutating func append(_ other: Array<IndexPath.Element>)
```

## See Also

### Selecting Nodes
- [func append(IndexPath)](./append%28_%29-6dxrh.md)
  Appends the nodes of another index path to this one.
- [func append(IndexPath.Element)](./append%28_%29-7qv6f.md)
  Appends a single element to this index path as a new node.
- [func appending(IndexPath.Element) -> IndexPath](./appending%28_%29-93eco.md)
  Returns a new index path containing the elements of this one plus the given element.
- [func appending(IndexPath) -> IndexPath](./appending%28_%29-53tcl.md)
  Returns a new index path containing the elements of this one plus those of another index path.
- [func appending(Array<IndexPath.Element>) -> IndexPath](./appending%28_%29-174v0.md)
  Returns a new index path containing the elements of this one plus an array of additional elements.
- [func compare(IndexPath) -> ComparisonResult](./compare%28_%29.md)
  Compares this index path to another in depth-first traversal order.
- [func dropLast() -> IndexPath](./droplast%28%29.md)
  Return a new index path containing all but the last element.
- [func index(after: IndexPath.Index) -> IndexPath.Index](./index%28after%29.md)
  Returns the index that follows the given index.
- [func index(before: IndexPath.Index) -> IndexPath.Index](./index%28before%29.md)
  Returns the index that precedes the given index.
- [func makeIterator() -> IndexingIterator<IndexPath>](./makeiterator%28%29.md)
  Returns an iterator over the nodes of the index path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/indexpath/append(_:)-6vsd5)*