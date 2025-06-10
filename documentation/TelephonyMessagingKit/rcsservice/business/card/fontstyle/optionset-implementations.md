# OptionSet Implementations

**Framework**: TelephonyMessagingKit

## Topics

### Initializers
- [init()](rcsservice/business/card/fontstyle/init.md)
  Creates an empty option set.
### Instance Methods
- [func contains(Self) -> Bool](rcsservice/business/card/fontstyle/contains(_:).md)
  Returns a Boolean value that indicates whether a given element is a member of the option set.
- [func formIntersection(Self)](rcsservice/business/card/fontstyle/formintersection(_:).md)
  Removes all elements of this option set that are not also present in the given set.
- [func formSymmetricDifference(Self)](rcsservice/business/card/fontstyle/formsymmetricdifference(_:).md)
  Replaces this set with a new set containing all elements contained in either this set or the given set, but not in both.
- [func formUnion(Self)](rcsservice/business/card/fontstyle/formunion(_:).md)
  Inserts the elements of another set into this option set.
- [func insert(Self.Element) -> (inserted: Bool, memberAfterInsert: Self.Element)](rcsservice/business/card/fontstyle/insert(_:).md)
  Adds the given element to the option set if it is not already a member.
- [func intersection(Self) -> Self](rcsservice/business/card/fontstyle/intersection(_:).md)
  Returns a new option set with only the elements contained in both this set and the given set.
- [func remove(Self.Element) -> Self.Element?](rcsservice/business/card/fontstyle/remove(_:).md)
  Removes the given element and all elements subsumed by it.
- [func symmetricDifference(Self) -> Self](rcsservice/business/card/fontstyle/symmetricdifference(_:).md)
  Returns a new option set with the elements contained in this set or in the given set, but not in both.
- [func union(Self) -> Self](rcsservice/business/card/fontstyle/union(_:).md)
  Returns a new option set of the elements contained in this set, in the given set, or in both.
- [func update(with: Self.Element) -> Self.Element?](rcsservice/business/card/fontstyle/update(with:).md)
  Inserts the given element into the set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/business/card/fontstyle/optionset-implementations)*