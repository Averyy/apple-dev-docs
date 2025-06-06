# SetAlgebra Implementations

**Framework**: RealityKit

## Topics

### Initializers
- [init<S>(S)](charactercontrollercomponent/collisionflags/init(_:).md)
  Creates a new set from a finite sequence of items.
- [init(arrayLiteral: Self.Element...)](charactercontrollercomponent/collisionflags/init(arrayliteral:).md)
  Creates a set containing the elements of the given array literal.
### Instance Properties
- [var isEmpty: Bool](charactercontrollercomponent/collisionflags/isempty.md)
  A Boolean value that indicates whether the set has no elements.
### Instance Methods
- [func isDisjoint(with: Self) -> Bool](charactercontrollercomponent/collisionflags/isdisjoint(with:).md)
  Returns a Boolean value that indicates whether the set has no members in common with the given set.
- [func isStrictSubset(of: Self) -> Bool](charactercontrollercomponent/collisionflags/isstrictsubset(of:).md)
  Returns a Boolean value that indicates whether this set is a strict subset of the given set.
- [func isStrictSuperset(of: Self) -> Bool](charactercontrollercomponent/collisionflags/isstrictsuperset(of:).md)
  Returns a Boolean value that indicates whether this set is a strict superset of the given set.
- [func isSubset(of: Self) -> Bool](charactercontrollercomponent/collisionflags/issubset(of:).md)
  Returns a Boolean value that indicates whether the set is a subset of another set.
- [func isSuperset(of: Self) -> Bool](charactercontrollercomponent/collisionflags/issuperset(of:).md)
  Returns a Boolean value that indicates whether the set is a superset of the given set.
- [func subtract(Self)](charactercontrollercomponent/collisionflags/subtract(_:).md)
  Removes the elements of the given set from this set.
- [func subtracting(Self) -> Self](charactercontrollercomponent/collisionflags/subtracting(_:).md)
  Returns a new set containing the elements of this set that do not occur in the given set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/charactercontrollercomponent/collisionflags/setalgebra-implementations)*