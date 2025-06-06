# SetAlgebra Implementations

**Framework**: LightweightCodeRequirements

## Topics

### Initializers
- [init<S>(S)](ondiskcodesigningflags/valueset/init(_:).md)
  Creates a new set from a finite sequence of items.
- [init(arrayLiteral: Self.Element...)](ondiskcodesigningflags/valueset/init(arrayliteral:).md)
  Creates a set containing the elements of the given array literal.
### Instance Properties
- [var isEmpty: Bool](ondiskcodesigningflags/valueset/isempty.md)
  A Boolean value that indicates whether the set has no elements.
### Instance Methods
- [func isDisjoint(with: Self) -> Bool](ondiskcodesigningflags/valueset/isdisjoint(with:).md)
  Returns a Boolean value that indicates whether the set has no members in common with the given set.
- [func isStrictSubset(of: Self) -> Bool](ondiskcodesigningflags/valueset/isstrictsubset(of:).md)
  Returns a Boolean value that indicates whether this set is a strict subset of the given set.
- [func isStrictSuperset(of: Self) -> Bool](ondiskcodesigningflags/valueset/isstrictsuperset(of:).md)
  Returns a Boolean value that indicates whether this set is a strict superset of the given set.
- [func isSubset(of: Self) -> Bool](ondiskcodesigningflags/valueset/issubset(of:).md)
  Returns a Boolean value that indicates whether the set is a subset of another set.
- [func isSuperset(of: Self) -> Bool](ondiskcodesigningflags/valueset/issuperset(of:).md)
  Returns a Boolean value that indicates whether the set is a superset of the given set.
- [func subtract(Self)](ondiskcodesigningflags/valueset/subtract(_:).md)
  Removes the elements of the given set from this set.
- [func subtracting(Self) -> Self](ondiskcodesigningflags/valueset/subtracting(_:).md)
  Returns a new set containing the elements of this set that do not occur in the given set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/lightweightcoderequirements/ondiskcodesigningflags/valueset/setalgebra-implementations)*