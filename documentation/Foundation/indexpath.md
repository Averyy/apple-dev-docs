# IndexPath

**Framework**: Foundation  
**Kind**: struct

A list of indexes that together represent the path to a specific location in a tree of nested arrays.

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
struct IndexPath
```

#### Overview

Each index in an index path represents the index into an array of children from one node in the tree to another, deeper, node.

## Topics

### Creating Index Paths
- [init()](indexpath/init.md)
  Creates an empty index path.
- [init(index: IndexPath.Element)](indexpath/init(index:).md)
  Creates an index path with a single element.
- [init(arrayLiteral: IndexPath.Element...)](indexpath/init(arrayliteral:).md)
  Creates an index path from an array literal.
- [init(indexes: Array<IndexPath.Element>)](indexpath/init(indexes:)-7auqk.md)
  Creates an index path from an array of elements.
- [init<ElementSequence>(indexes: ElementSequence)](indexpath/init(indexes:)-55we8.md)
  Creates an index path from a sequence of integers.
- [IndexPath.Element](indexpath/element.md)
  A type that represents one node of an index path.
### Working with Special Node Names
- [var endIndex: IndexPath.Index](indexpath/endindex.md)
  One past the index of the last node in the index path.
- [var item: Int](indexpath/item-8cp0y.md)
  The value of the item element of the index path.
- [var row: Int](indexpath/row.md)
  The value of the row element of the index path.
- [var section: Int](indexpath/section-8h7wo.md)
  The value of the section element of the index path.
- [var startIndex: IndexPath.Index](indexpath/startindex.md)
  The index of the first node in the index path.
### Accessing Nodes
- [subscript(IndexPath.Index) -> IndexPath.Element](indexpath/subscript(_:)-6p6ul.md)
  Accesses one of the index path’s nodes.
- [subscript(Range<IndexPath.Index>) -> IndexPath](indexpath/subscript(_:)-4pgu1.md)
  Accesses a contiguous subrange of the index path’s nodes.
### Adding Nodes
- [static func + (IndexPath, IndexPath) -> IndexPath](indexpath/+(_:_:).md)
  Combines the elements of two index paths into a single index path.
- [static func += (inout IndexPath, IndexPath)](indexpath/+=(_:_:).md)
  Appends the elements of another index path to this index path.
### Selecting Nodes
- [func append(IndexPath)](indexpath/append(_:)-6dxrh.md)
  Appends the nodes of another index path to this one.
- [func append(Array<IndexPath.Element>)](indexpath/append(_:)-6vsd5.md)
  Appends an array of elements to this index path as additional nodes.
- [func append(IndexPath.Element)](indexpath/append(_:)-7qv6f.md)
  Appends a single element to this index path as a new node.
- [func appending(IndexPath.Element) -> IndexPath](indexpath/appending(_:)-93eco.md)
  Returns a new index path containing the elements of this one plus the given element.
- [func appending(IndexPath) -> IndexPath](indexpath/appending(_:)-53tcl.md)
  Returns a new index path containing the elements of this one plus those of another index path.
- [func appending(Array<IndexPath.Element>) -> IndexPath](indexpath/appending(_:)-174v0.md)
  Returns a new index path containing the elements of this one plus an array of additional elements.
- [func compare(IndexPath) -> ComparisonResult](indexpath/compare(_:).md)
  Compares this index path to another in depth-first traversal order.
- [func dropLast() -> IndexPath](indexpath/droplast.md)
  Return a new index path containing all but the last element.
- [func index(after: IndexPath.Index) -> IndexPath.Index](indexpath/index(after:).md)
  Returns the index that follows the given index.
- [func index(before: IndexPath.Index) -> IndexPath.Index](indexpath/index(before:).md)
  Returns the index that precedes the given index.
- [func makeIterator() -> IndexingIterator<IndexPath>](indexpath/makeiterator.md)
  Returns an iterator over the nodes of the index path.
### Excluding Nodes
- [func dropLast() -> IndexPath](indexpath/droplast.md)
  Return a new index path containing all but the last element.
### Iterating over Nodes
- [func makeIterator() -> IndexingIterator<IndexPath>](indexpath/makeiterator.md)
  Returns an iterator over the nodes of the index path.
### Comparing Index Paths
- [func compare(IndexPath) -> ComparisonResult](indexpath/compare(_:).md)
  Compares this index path to another in depth-first traversal order.
### Manipulating Indexes
- [IndexPath.Index](indexpath/index.md)
  A type that points to a particular node in an index path, similar to an array index.
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
### Using Reference Types
- [class NSIndexPath](nsindexpath.md)
  A list of indexes that together represent the path to a specific location in a tree of nested arrays.
### Initializers
- [init(item: Int, section: Int)](indexpath/init(item:section:)-359jo.md)
  Creates an index path that references an item in a particular section.
- [init(item: Int, section: Int)](indexpath/init(item:section:)-rib.md)
  Initialize for use with `NSCollectionView`.
- [init(row: Int, section: Int)](indexpath/init(row:section:).md)
  Creates an index path that references a row in a particular section.
### Instance Properties
- [var item: Int](indexpath/item-6rh8l.md)
  The item of this index path, when used with `NSCollectionView`.
- [var section: Int](indexpath/section-2059m.md)
  The section of this index path, when used with `NSCollectionView`.

## Relationships

### Conforms To
- [BidirectionalCollection](../swift/bidirectionalcollection.md)
- [Collection](../swift/collection.md)
- [Comparable](../swift/comparable.md)
- [Copyable](../swift/copyable.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomReflectable](../swift/customreflectable.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [Hashable](../swift/hashable.md)
- [MutableCollection](../swift/mutablecollection.md)
- [RandomAccessCollection](../swift/randomaccesscollection.md)
- [ReferenceConvertible](referenceconvertible.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [Sequence](../swift/sequence.md)

## See Also

- [struct IndexSet](indexset.md)
  A collection of unique integer values that represent the indexes of elements in another collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/indexpath)*