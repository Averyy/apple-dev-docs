# RangeSet

**Framework**: Swift  
**Kind**: struct

A set of values of any comparable type, represented by ranges.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct RangeSet<Bound> where Bound : Comparable
```

#### Overview

You can use a range set to efficiently represent a set of `Comparable` values that spans any number of discontiguous ranges. Range sets are commonly used to represent multiple subranges of a collection, by storing ranges of a collection’s index type.

In this example, `negativeSubranges` is a range set representing the locations of all the negative values in `numbers`:

```swift
var numbers = [10, 12, -5, 14, -3, -9, 15]
let negativeSubranges = numbers.indices(where: { $0 < 0 })
// numbers[negativeSubranges].count == 3

numbers.moveSubranges(negativeSubranges, to: 0)
// numbers == [-5, -3, -9, 10, 12, 14, 15]
```

## Topics

### Structures
- [RangeSet.Ranges](rangeset/ranges-swift.struct.md)
  A collection of the ranges that make up a range set.
### Initializers
- [init()](rangeset/init.md)
  Creates an empty range set.
- [init(Range<Bound>)](rangeset/init(_:)-230uy.md)
  Creates a range set containing the given range.
- [init(IndexSet)](rangeset/init(_:)-42v9u.md)
- [init(some Sequence<Range<Bound>>)](rangeset/init(_:)-9x0yj.md)
  Creates a range set containing the values in the given ranges.
- [init<S, C>(S, within: C)](rangeset/init(_:within:).md)
  Creates a new range set containing ranges that contain only the specified indices in the given collection.
### Instance Properties
- [var isEmpty: Bool](rangeset/isempty.md)
  A Boolean value indicating whether the range set is empty.
- [var ranges: RangeSet<Bound>.Ranges](rangeset/ranges-swift.property.md)
  A collection of the ranges that make up the range set.
### Instance Methods
- [func contains(Bound) -> Bool](rangeset/contains(_:).md)
  Returns a Boolean value indicating whether the given value is contained by the ranges in the range set.
- [func formIntersection(RangeSet<Bound>)](rangeset/formintersection(_:).md)
  Removes the contents of this range set that aren’t also in the given range set.
- [func formSymmetricDifference(RangeSet<Bound>)](rangeset/formsymmetricdifference(_:).md)
  Removes the contents of this range set that are also in the given set and adds the contents of the given set that are not already in this range set.
- [func formUnion(RangeSet<Bound>)](rangeset/formunion(_:).md)
  Adds the contents of the given range set to this range set.
- [func insert<C>(Bound, within: C) -> Bool](rangeset/insert(_:within:).md)
  Inserts a range that contains only the specified index into the range set.
- [func insert(contentsOf: Range<Bound>)](rangeset/insert(contentsof:).md)
  Inserts the given range into the range set.
- [func intersection(RangeSet<Bound>) -> RangeSet<Bound>](rangeset/intersection(_:).md)
  Returns a new range set containing the contents of both this set and the given set.
- [func isDisjoint(RangeSet<Bound>) -> Bool](rangeset/isdisjoint(_:).md)
  Returns a Boolean value that indicates whether this range set set has no members in common with the given set.
- [func isStrictSubset(of: RangeSet<Bound>) -> Bool](rangeset/isstrictsubset(of:).md)
  Returns a Boolean value that indicates whether this range set is a strict subset of the given set.
- [func isStrictSuperset(of: RangeSet<Bound>) -> Bool](rangeset/isstrictsuperset(of:).md)
  Returns a Boolean value that indicates whether this range set is a strict superset of the given set.
- [func isSubset(of: RangeSet<Bound>) -> Bool](rangeset/issubset(of:).md)
  Returns a Boolean value that indicates whether this range set is a subset of the given set.
- [func isSuperset(of: RangeSet<Bound>) -> Bool](rangeset/issuperset(of:).md)
  Returns a Boolean value that indicates whether this range set is a superset of the given set.
- [func isValid(within: DiscontiguousAttributedSubstring) -> Bool](rangeset/isvalid(within:)-38qb9.md)
  Indicates whether the range set is valid for use with the provided discontiguous attributed string.
- [func isValid(within: some AttributedStringProtocol) -> Bool](rangeset/isvalid(within:)-6u17e.md)
  Indicates whether the range set is valid for use with the provided attributed string.
- [func remove<C>(Bound, within: C)](rangeset/remove(_:within:).md)
  Removes the range that contains only the specified index from the range set.
- [func remove(contentsOf: Range<Bound>)](rangeset/remove(contentsof:).md)
  Removes the given range from the range set.
- [func subtract(RangeSet<Bound>)](rangeset/subtract(_:).md)
  Removes the contents of the given range set from this range set.
- [func subtracting(RangeSet<Bound>) -> RangeSet<Bound>](rangeset/subtracting(_:).md)
  Returns a new set containing the contents of this range set that are not also in the given range set.
- [func symmetricDifference(RangeSet<Bound>) -> RangeSet<Bound>](rangeset/symmetricdifference(_:).md)
  Returns a new range set representing the values in this range set or the given range set, but not both.
- [func union(RangeSet<Bound>) -> RangeSet<Bound>](rangeset/union(_:).md)
  Returns a new range set containing the contents of both this set and the given set.
### Default Implementations
- [CustomStringConvertible Implementations](rangeset/customstringconvertible-implementations.md)
- [Equatable Implementations](rangeset/equatable-implementations.md)
- [Hashable Implementations](rangeset/hashable-implementations.md)

## Relationships

### Conforms To
- [Copyable](copyable.md)
- [CustomStringConvertible](customstringconvertible.md)
- [Equatable](equatable.md)
- [Hashable](hashable.md)
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)

## See Also

- [static func ..< (Self, Self) -> Range<Self>](comparable/'.._(_:_:).md)
  Returns a half-open range that contains its lower bound but not its upper bound.
- [struct Range](range.md)
  A half-open interval from a lower bound up to, but not including, an upper bound.
- [static func ... (Self, Self) -> ClosedRange<Self>](comparable/'...(_:_:).md)
  Returns a closed range that contains both of its bounds.
- [struct ClosedRange](closedrange.md)
  An interval from a lower bound up to, and including, an upper bound.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/rangeset)*