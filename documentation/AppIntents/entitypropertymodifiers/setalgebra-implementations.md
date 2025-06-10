# SetAlgebra Implementations

**Framework**: App Intents

## Topics

### Initializers
- [init<S>(S)](entitypropertymodifiers/init(_:).md)
  Creates a new set from a finite sequence of items.
- [init(arrayLiteral: Self.Element...)](entitypropertymodifiers/init(arrayliteral:).md)
  Creates a set containing the elements of the given array literal.
### Instance Properties
- [var isEmpty: Bool](entitypropertymodifiers/isempty.md)
  A Boolean value that indicates whether the set has no elements.
### Instance Methods
- [func isDisjoint(with: Self) -> Bool](entitypropertymodifiers/isdisjoint(with:).md)
  Returns a Boolean value that indicates whether the set has no members in common with the given set.
- [func isStrictSubset(of: Self) -> Bool](entitypropertymodifiers/isstrictsubset(of:).md)
  Returns a Boolean value that indicates whether this set is a strict subset of the given set.
- [func isStrictSuperset(of: Self) -> Bool](entitypropertymodifiers/isstrictsuperset(of:).md)
  Returns a Boolean value that indicates whether this set is a strict superset of the given set.
- [func isSubset(of: Self) -> Bool](entitypropertymodifiers/issubset(of:).md)
  Returns a Boolean value that indicates whether the set is a subset of another set.
- [func isSuperset(of: Self) -> Bool](entitypropertymodifiers/issuperset(of:).md)
  Returns a Boolean value that indicates whether the set is a superset of the given set.
- [func subtract(Self)](entitypropertymodifiers/subtract(_:).md)
  Removes the elements of the given set from this set.
- [func subtracting(Self) -> Self](entitypropertymodifiers/subtracting(_:).md)
  Returns a new set containing the elements of this set that do not occur in the given set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entitypropertymodifiers/setalgebra-implementations)*