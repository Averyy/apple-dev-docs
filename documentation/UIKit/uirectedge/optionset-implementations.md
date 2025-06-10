# OptionSet Implementations

**Framework**: UIKit

## Topics

### Initializers
- [init()](uirectedge/init.md)
  Creates an empty option set.
### Instance Methods
- [func contains(Self) -> Bool](uirectedge/contains(_:).md)
  Returns a Boolean value that indicates whether a given element is a member of the option set.
- [func formIntersection(Self)](uirectedge/formintersection(_:).md)
  Removes all elements of this option set that are not also present in the given set.
- [func formSymmetricDifference(Self)](uirectedge/formsymmetricdifference(_:).md)
  Replaces this set with a new set containing all elements contained in either this set or the given set, but not in both.
- [func formUnion(Self)](uirectedge/formunion(_:).md)
  Inserts the elements of another set into this option set.
- [func insert(Self.Element) -> (inserted: Bool, memberAfterInsert: Self.Element)](uirectedge/insert(_:).md)
  Adds the given element to the option set if it is not already a member.
- [func intersection(Self) -> Self](uirectedge/intersection(_:).md)
  Returns a new option set with only the elements contained in both this set and the given set.
- [func remove(Self.Element) -> Self.Element?](uirectedge/remove(_:).md)
  Removes the given element and all elements subsumed by it.
- [func symmetricDifference(Self) -> Self](uirectedge/symmetricdifference(_:).md)
  Returns a new option set with the elements contained in this set or in the given set, but not in both.
- [func union(Self) -> Self](uirectedge/union(_:).md)
  Returns a new option set of the elements contained in this set, in the given set, or in both.
- [func update(with: Self.Element) -> Self.Element?](uirectedge/update(with:).md)
  Inserts the given element into the set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uirectedge/optionset-implementations)*