# IndexSet

**Framework**: Foundation  
**Kind**: struct

A collection of unique integer values that represent the indexes of elements in another collection.

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
struct IndexSet
```

#### Overview

The range of valid integer values is `0...Int.max-1`. Anything outside this range is an error.

## Topics

### Creating an Index Set
- [init()](indexset/init.md)
  Initializes an empty index set.
- [init(integer: IndexSet.Element)](indexset/init(integer:).md)
  Initializes an index set with a single integer.
- [init(integersIn: Range<IndexSet.Element>)](indexset/init(integersin:)-40cz3.md)
  Initializes an index set with a range of integers.
### Counting Items in a Set
- [func count(in: Range<IndexSet.Element>) -> Int](indexset/count(in:)-v622.md)
  Returns the count of integers in `self` that intersect `range`.
### Combining Index Sets
- [func formIntersection(IndexSet)](indexset/formintersection(_:).md)
  Intersects the `IndexSet` with `other`.
- [func formSymmetricDifference(IndexSet)](indexset/formsymmetricdifference(_:).md)
  Exclusive or the `IndexSet` with `other`.
- [func formUnion(IndexSet)](indexset/formunion(_:).md)
  Union the `IndexSet` with `other`.
- [func intersection(IndexSet) -> IndexSet](indexset/intersection(_:).md)
  Intersects the `IndexSet` with `other`.
- [func symmetricDifference(IndexSet) -> IndexSet](indexset/symmetricdifference(_:).md)
  Exclusive or the `IndexSet` with `other`.
- [func union(IndexSet) -> IndexSet](indexset/union(_:).md)
  Union the `IndexSet` with `other`.
### Inserting Elements
- [func insert(IndexSet.Element) -> (inserted: Bool, memberAfterInsert: IndexSet.Element)](indexset/insert(_:).md)
  Insert an integer into the `IndexSet`.
- [func insert(integersIn: Range<IndexSet.Element>)](indexset/insert(integersin:)-28eld.md)
  Insert a range of integers into the `IndexSet`.
- [func update(with: IndexSet.Element) -> IndexSet.Element?](indexset/update(with:).md)
  Insert an integer into the `IndexSet`.
### Removing Elements
- [func remove(IndexSet.Element) -> IndexSet.Element?](indexset/remove(_:).md)
  Remove an integer from the `IndexSet`.
- [func remove(integersIn: Range<IndexSet.Element>)](indexset/remove(integersin:)-7dhfw.md)
  Remove a range of integers from the `IndexSet`.
- [func remove(integersIn: ClosedRange<IndexSet.Element>)](indexset/remove(integersin:)-54370.md)
  Remove a range of integers from the `IndexSet`.
- [func removeAll()](indexset/removeall.md)
  Remove all values from the `IndexSet`.
### Testing Set Membership
- [func contains(IndexSet.Element) -> Bool](indexset/contains(_:).md)
  Returns `true` if `self` contains `integer`.
- [func contains(integersIn: IndexSet) -> Bool](indexset/contains(integersin:)-9frtv.md)
  Returns `true` if `self` contains all of the integers in `indexSet`.
- [func contains(integersIn: Range<IndexSet.Element>) -> Bool](indexset/contains(integersin:)-sma8.md)
  Returns `true` if `self` contains all of the integers in `range`.
- [func intersects(integersIn: Range<IndexSet.Element>) -> Bool](indexset/intersects(integersin:)-3sdmv.md)
  Returns `true` if `self` intersects any of the integers in `range`.
### Manipulating Indexes
- [func indexRange(in: Range<IndexSet.Element>) -> Range<IndexSet.Index>](indexset/indexrange(in:)-539lz.md)
  Return a `Range<IndexSet.Index>` which can be used to subscript the index set.
### Finding Elements
- [func integerLessThanOrEqualTo(IndexSet.Element) -> IndexSet.Element?](indexset/integerlessthanorequalto(_:).md)
  Returns an integer contained in `self` which is less than or equal to `integer`, or `nil` if a result could not be found.
- [func integerGreaterThan(IndexSet.Element) -> IndexSet.Element?](indexset/integergreaterthan(_:).md)
  Returns an integer contained in `self` which is greater than `integer`, or `nil` if a result could not be found.
- [func integerGreaterThanOrEqualTo(IndexSet.Element) -> IndexSet.Element?](indexset/integergreaterthanorequalto(_:).md)
  Returns an integer contained in `self` which is greater than or equal to `integer`, or `nil` if a result could not be found.
- [func integerLessThan(IndexSet.Element) -> IndexSet.Element?](indexset/integerlessthan(_:).md)
  Returns an integer contained in `self` which is less than `integer`, or `nil` if a result could not be found.
### Selecting Elements
- [func filteredIndexSet(in: Range<IndexSet.Element>, includeInteger: (IndexSet.Element) throws -> Bool) rethrows -> IndexSet](indexset/filteredindexset(in:includeinteger:)-6cdvc.md)
  Returns an IndexSet filtered according to the result of `includeInteger`.
- [func filteredIndexSet(in: ClosedRange<IndexSet.Element>, includeInteger: (IndexSet.Element) throws -> Bool) rethrows -> IndexSet](indexset/filteredindexset(in:includeinteger:)-9dn86.md)
  Returns an IndexSet filtered according to the result of `includeInteger`.
- [func filteredIndexSet(includeInteger: (IndexSet.Element) throws -> Bool) rethrows -> IndexSet](indexset/filteredindexset(includeinteger:).md)
  Returns an IndexSet filtered according to the result of `includeInteger`.
### Shifting Index Groups
- [func shift(startingAt: IndexSet.Element, by: Int)](indexset/shift(startingat:by:).md)
  For a positive delta, shifts the indexes in [index, INT_MAX] to the right, thereby inserting an “empty space” [index, delta], for a negative delta, shifts the indexes in [index, INT_MAX] to the left, thereby deleting the indexes in the range [index - delta, delta].
### Getting a Range-Based View
- [func rangeView(of: Range<IndexSet.Element>) -> IndexSet.RangeView](indexset/rangeview(of:)-5xqe8.md)
  Returns a `Range`-based view of `self`.
- [var rangeView: IndexSet.RangeView](indexset/rangeview-swift.property.md)
  Returns a `Range`-based view of the entire contents of `self`.
- [IndexSet.RangeView](indexset/rangeview-swift.struct.md)
  A view of the contents of an IndexSet, organized by range.
### Using Reference Types
- [class NSIndexSet](nsindexset.md)
  An immutable collection of unique integer values that represent indexes in another collection.
- [class NSMutableIndexSet](nsmutableindexset.md)
  A mutable collection of unique integer values that represent indexes in another collection.
### Structures
- [IndexSet.Index](indexset/index.md)
  The mechanism for accessing the integers stored in an IndexSet.
### Initializers
- [init<R>(integersIn: R)](indexset/init(integersin:)-2zs95.md)
  Initialize an `IndexSet` with a range of integers.
- [init?(integersIn: RangeSet<Int>)](indexset/init(integersin:)-54nqd.md)
### Instance Properties
- [var count: Int](indexset/count.md)
  Returns the number of integers in `self`.
- [var first: IndexSet.Element?](indexset/first.md)
  The first integer in `self`, or nil if `self` is empty.
- [var isEmpty: Bool](indexset/isempty.md)
  Returns `true` if self contains no values.
- [var last: IndexSet.Element?](indexset/last.md)
  The last integer in `self`, or nil if `self` is empty.
### Instance Methods
- [func contains<R>(integersIn: R) -> Bool](indexset/contains(integersin:)-4k1o8.md)
  Returns `true` if `self` contains all of the integers in `range`.
- [func count<R>(in: R) -> Int](indexset/count(in:)-7irji.md)
  Returns the count of integers in `self` that intersect `range`.
- [func indexRange<R>(in: R) -> Range<IndexSet.Index>](indexset/indexrange(in:)-6057o.md)
  Return a `Range<IndexSet.Index>` which can be used to subscript the index set.
- [func insert<R>(integersIn: R)](indexset/insert(integersin:)-9wcrp.md)
  Insert a range of integers into the `IndexSet`.
- [func intersects<R>(integersIn: R) -> Bool](indexset/intersects(integersin:)-9cq7w.md)
  Returns `true` if `self` intersects any of the integers in `range`.
- [func rangeView<R>(of: R) -> IndexSet.RangeView](indexset/rangeview(of:)-4jdy1.md)
  Returns a `Range`-based view of `self`.

## Relationships

### Conforms To
- [BidirectionalCollection](../Swift/BidirectionalCollection.md)
- [Collection](../Swift/Collection.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomReflectable](../Swift/CustomReflectable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [Hashable](../Swift/Hashable.md)
- [ReferenceConvertible](referenceconvertible.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [Sequence](../Swift/Sequence.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [struct IndexPath](indexpath.md)
  A list of indexes that together represent the path to a specific location in a tree of nested arrays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/indexset)*