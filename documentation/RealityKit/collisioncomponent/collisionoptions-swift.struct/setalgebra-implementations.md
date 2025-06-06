# SetAlgebra Implementations

**Framework**: RealityKit

## Topics

### Initializers
- [init<S>(S)](collisioncomponent/collisionoptions-swift.struct/init(_:).md)
  Creates a new set from a finite sequence of items.
- [init(arrayLiteral: Self.Element...)](collisioncomponent/collisionoptions-swift.struct/init(arrayliteral:).md)
  Creates a set containing the elements of the given array literal.
### Instance Properties
- [var isEmpty: Bool](collisioncomponent/collisionoptions-swift.struct/isempty.md)
  A Boolean value that indicates whether the set has no elements.
### Instance Methods
- [func isDisjoint(with: Self) -> Bool](collisioncomponent/collisionoptions-swift.struct/isdisjoint(with:).md)
  Returns a Boolean value that indicates whether the set has no members in common with the given set.
- [func isStrictSubset(of: Self) -> Bool](collisioncomponent/collisionoptions-swift.struct/isstrictsubset(of:).md)
  Returns a Boolean value that indicates whether this set is a strict subset of the given set.
- [func isStrictSuperset(of: Self) -> Bool](collisioncomponent/collisionoptions-swift.struct/isstrictsuperset(of:).md)
  Returns a Boolean value that indicates whether this set is a strict superset of the given set.
- [func isSubset(of: Self) -> Bool](collisioncomponent/collisionoptions-swift.struct/issubset(of:).md)
  Returns a Boolean value that indicates whether the set is a subset of another set.
- [func isSuperset(of: Self) -> Bool](collisioncomponent/collisionoptions-swift.struct/issuperset(of:).md)
  Returns a Boolean value that indicates whether the set is a superset of the given set.
- [func subtract(Self)](collisioncomponent/collisionoptions-swift.struct/subtract(_:).md)
  Removes the elements of the given set from this set.
- [func subtracting(Self) -> Self](collisioncomponent/collisionoptions-swift.struct/subtracting(_:).md)
  Returns a new set containing the elements of this set that do not occur in the given set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/collisioncomponent/collisionoptions-swift.struct/setalgebra-implementations)*