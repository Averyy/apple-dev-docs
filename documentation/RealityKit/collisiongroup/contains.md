# contains(_:)

**Framework**: RealityKit  
**Kind**: method

Returns a Boolean value that indicates whether a given element is a member of the option set.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

## Declaration

```swift
func contains(_ member: Self) -> Bool
```

#### Return Value

`true` if the option set contains `member`; otherwise, `false`.

#### Discussion

This example uses the `contains(_:)` method to check whether next-day shipping is in the `availableOptions` instance.

```None
let availableOptions = ShippingOptions.express
if availableOptions.contains(.nextDay) {
    print("Next day shipping available")
}
// Prints "Next day shipping available"
```

## Parameters

- `member`: The element to look for in the option set.

## See Also

- [let rawValue: UInt32](collisiongroup/rawvalue-swift.property.md)
  The corresponding value of the raw type.
- [static func != (Self, Self) -> Bool](collisiongroup/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
- [CollisionGroup.Element](collisiongroup/element.md)
  The element type of the option set.
- [var isEmpty: Bool](collisiongroup/isempty.md)
  A Boolean value that indicates whether the set has no elements.
- [let rawValue: UInt32](collisiongroup/rawvalue-swift.property.md)
  The corresponding value of the raw type.
- [func formIntersection(Self)](collisiongroup/formintersection(_:).md)
  Removes all elements of this option set that are not also present in the given set.
- [func formSymmetricDifference(Self)](collisiongroup/formsymmetricdifference(_:).md)
  Replaces this set with a new set containing all elements contained in either this set or the given set, but not in both.
- [func formUnion(Self)](collisiongroup/formunion(_:).md)
  Inserts the elements of another set into this option set.
- [func insert(Self.Element) -> (inserted: Bool, memberAfterInsert: Self.Element)](collisiongroup/insert(_:).md)
  Adds the given element to the option set if it is not already a member.
- [func intersection(Self) -> Self](collisiongroup/intersection(_:).md)
  Returns a new option set with only the elements contained in both this set and the given set.
- [func isDisjoint(with: Self) -> Bool](collisiongroup/isdisjoint(with:).md)
  Returns a Boolean value that indicates whether the set has no members in common with the given set.
- [func isStrictSubset(of: Self) -> Bool](collisiongroup/isstrictsubset(of:).md)
  Returns a Boolean value that indicates whether this set is a strict subset of the given set.
- [func isStrictSuperset(of: Self) -> Bool](collisiongroup/isstrictsuperset(of:).md)
  Returns a Boolean value that indicates whether this set is a strict superset of the given set.
- [func isSubset(of: Self) -> Bool](collisiongroup/issubset(of:).md)
  Returns a Boolean value that indicates whether the set is a subset of another set.
- [func isSuperset(of: Self) -> Bool](collisiongroup/issuperset(of:).md)
  Returns a Boolean value that indicates whether the set is a superset of the given set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/collisiongroup/contains(_:))*