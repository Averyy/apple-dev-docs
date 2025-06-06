# SetAlgebra Implementations

**Framework**: RealityKit

## Topics

### Initializers
- [init<S>(S)](accessibilitycomponent/supportedactions/init(_:).md)
  Creates a new set from a finite sequence of items.
- [init(arrayLiteral: Self.Element...)](accessibilitycomponent/supportedactions/init(arrayliteral:).md)
  Creates a set containing the elements of the given array literal.
### Instance Properties
- [var isEmpty: Bool](accessibilitycomponent/supportedactions/isempty.md)
  A Boolean value that indicates whether the set has no elements.
### Instance Methods
- [func isDisjoint(with: Self) -> Bool](accessibilitycomponent/supportedactions/isdisjoint(with:).md)
  Returns a Boolean value that indicates whether the set has no members in common with the given set.
- [func isStrictSubset(of: Self) -> Bool](accessibilitycomponent/supportedactions/isstrictsubset(of:).md)
  Returns a Boolean value that indicates whether this set is a strict subset of the given set.
- [func isStrictSuperset(of: Self) -> Bool](accessibilitycomponent/supportedactions/isstrictsuperset(of:).md)
  Returns a Boolean value that indicates whether this set is a strict superset of the given set.
- [func isSubset(of: Self) -> Bool](accessibilitycomponent/supportedactions/issubset(of:).md)
  Returns a Boolean value that indicates whether the set is a subset of another set.
- [func isSuperset(of: Self) -> Bool](accessibilitycomponent/supportedactions/issuperset(of:).md)
  Returns a Boolean value that indicates whether the set is a superset of the given set.
- [func subtract(Self)](accessibilitycomponent/supportedactions/subtract(_:).md)
  Removes the elements of the given set from this set.
- [func subtracting(Self) -> Self](accessibilitycomponent/supportedactions/subtracting(_:).md)
  Returns a new set containing the elements of this set that do not occur in the given set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/accessibilitycomponent/supportedactions/setalgebra-implementations)*