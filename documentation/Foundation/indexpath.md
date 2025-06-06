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
### Working with Special Node Names
- [var item: Int](indexpath/item-8cp0y.md)
  The value of the item element of the index path.
- [var row: Int](indexpath/row.md)
  The value of the row element of the index path.
- [var section: Int](indexpath/section-8h7wo.md)
  The value of the section element of the index path.
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
### Excluding Nodes
- [func dropLast() -> IndexPath](indexpath/droplast.md)
  Return a new index path containing all but the last element.
### Comparing Index Paths
- [func compare(IndexPath) -> ComparisonResult](indexpath/compare(_:).md)
  Compares this index path to another in depth-first traversal order.
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
- [BidirectionalCollection](../Swift/BidirectionalCollection.md)
- [Collection](../Swift/Collection.md)
- [Comparable](../Swift/Comparable.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomReflectable](../Swift/CustomReflectable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [Hashable](../Swift/Hashable.md)
- [MutableCollection](../Swift/MutableCollection.md)
- [RandomAccessCollection](../Swift/RandomAccessCollection.md)
- [ReferenceConvertible](referenceconvertible.md)
- [Sendable](../Swift/Sendable.md)
- [Sequence](../Swift/Sequence.md)

## See Also

- [struct IndexSet](indexset.md)
  A collection of unique integer values that represent the indexes of elements in another collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/indexpath)*