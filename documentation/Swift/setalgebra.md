# SetAlgebra

**Framework**: Swift  
**Kind**: protocol

A type that provides mathematical set operations.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
protocol SetAlgebra<Element> : Equatable, ExpressibleByArrayLiteral
```

#### Overview

You use types that conform to the `SetAlgebra` protocol when you need efficient membership tests or mathematical set operations such as intersection, union, and subtraction. In the standard library, you can use the `Set` type with elements of any hashable type, or you can easily create bit masks with `SetAlgebra` conformance using the `OptionSet` protocol. See those types for more information.

> **Note**: Unlike ordinary set types, the `Element` type of an `OptionSet` is identical to the `OptionSet` type itself. The `SetAlgebra` protocol is specifically designed to accommodate both kinds of set.

### Conforming to the Setalgebra Protocol

When implementing a custom type that conforms to the `SetAlgebra` protocol, you must implement the required initializers and methods. For the inherited methods to work properly, conforming types must meet the following axioms. Assume that `S` is a custom type that conforms to the `SetAlgebra` protocol, `x` and `y` are instances of `S`, and `e` is of type `S.Element`—the type that the set holds.

- `S() == []`
- `x.intersection(x) == x`
- `x.intersection([]) == []`
- `x.union(x) == x`
- `x.union([]) == x`
- `x.contains(e)` implies `x.union(y).contains(e)`
- `x.union(y).contains(e)` implies `x.contains(e) || y.contains(e)`
- `x.contains(e) && y.contains(e)` if and only if `x.intersection(y).contains(e)`
- `x.isSubset(of: y)` implies `x.union(y) == y`
- `x.isSuperset(of: y)` implies `x.union(y) == x`
- `x.isSubset(of: y)` if and only if `y.isSuperset(of: x)`
- `x.isStrictSuperset(of: y)` if and only if `x.isSuperset(of: y) && x != y`
- `x.isStrictSubset(of: y)` if and only if `x.isSubset(of: y) && x != y`

## Topics

### Creating a Set
- [init()](setalgebra/init.md)
  Creates an empty set.
### Testing for Membership
- [func contains(Self.Element) -> Bool](setalgebra/contains(_:).md)
  Returns a Boolean value that indicates whether the given element exists in the set.
- [associatedtype Element](setalgebra/element.md)
  A type for which the conforming type provides a containment test.
### Adding and Removing Elements
- [func insert(Self.Element) -> (inserted: Bool, memberAfterInsert: Self.Element)](setalgebra/insert(_:).md)
  Inserts the given element in the set if it is not already present.
- [func update(with: Self.Element) -> Self.Element?](setalgebra/update(with:).md)
  Inserts the given element into the set unconditionally.
- [func remove(Self.Element) -> Self.Element?](setalgebra/remove(_:).md)
  Removes the given element and any elements subsumed by the given element.
### Combining Sets
- [func union(Self) -> Self](setalgebra/union(_:).md)
  Returns a new set with the elements of both this and the given set.
- [func formUnion(Self)](setalgebra/formunion(_:).md)
  Adds the elements of the given set to the set.
- [func intersection(Self) -> Self](setalgebra/intersection(_:).md)
  Returns a new set with the elements that are common to both this set and the given set.
- [func formIntersection(Self)](setalgebra/formintersection(_:).md)
  Removes the elements of this set that aren’t also in the given set.
- [func symmetricDifference(Self) -> Self](setalgebra/symmetricdifference(_:).md)
  Returns a new set with the elements that are either in this set or in the given set, but not in both.
- [func formSymmetricDifference(Self)](setalgebra/formsymmetricdifference(_:).md)
  Removes the elements of the set that are also in the given set and adds the members of the given set that are not already in the set.
### Comparing Sets
- [func isStrictSubset(of: Self) -> Bool](setalgebra/isstrictsubset(of:).md)
  Returns a Boolean value that indicates whether this set is a strict subset of the given set.
- [func isStrictSuperset(of: Self) -> Bool](setalgebra/isstrictsuperset(of:).md)
  Returns a Boolean value that indicates whether this set is a strict superset of the given set.
### Initializers
- [init<S>(S)](setalgebra/init(_:).md)
  Creates a new set from a finite sequence of items.
### Instance Properties
- [var isEmpty: Bool](setalgebra/isempty.md)
  A Boolean value that indicates whether the set has no elements.
### Instance Methods
- [func isDisjoint(with: Self) -> Bool](setalgebra/isdisjoint(with:).md)
  Returns a Boolean value that indicates whether the set has no members in common with the given set.
- [func isSubset(of: Self) -> Bool](setalgebra/issubset(of:).md)
  Returns a Boolean value that indicates whether the set is a subset of another set.
- [func isSuperset(of: Self) -> Bool](setalgebra/issuperset(of:).md)
  Returns a Boolean value that indicates whether the set is a superset of the given set.
- [func subtract(Self)](setalgebra/subtract(_:).md)
  Removes the elements of the given set from this set.
- [func subtracting(Self) -> Self](setalgebra/subtracting(_:).md)
  Returns a new set containing the elements of this set that do not occur in the given set.

## Relationships

### Inherits From
- [Equatable](equatable.md)
- [ExpressibleByArrayLiteral](expressiblebyarrayliteral.md)
### Inherited By
- [OptionSet](optionset.md)
### Conforming Types
- [Set](set.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/setalgebra)*