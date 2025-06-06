# OptionSet Implementations

**Framework**: RealityKit

## Topics

### Initializers
- [init()](charactercontrollercomponent/collisionflags/init.md)
  Creates an empty option set.
### Instance Methods
- [func contains(Self) -> Bool](charactercontrollercomponent/collisionflags/contains(_:).md)
  Returns a Boolean value that indicates whether a given element is a member of the option set.
- [func formIntersection(Self)](charactercontrollercomponent/collisionflags/formintersection(_:).md)
  Removes all elements of this option set that are not also present in the given set.
- [func formSymmetricDifference(Self)](charactercontrollercomponent/collisionflags/formsymmetricdifference(_:).md)
  Replaces this set with a new set containing all elements contained in either this set or the given set, but not in both.
- [func formUnion(Self)](charactercontrollercomponent/collisionflags/formunion(_:).md)
  Inserts the elements of another set into this option set.
- [func insert(Self.Element) -> (inserted: Bool, memberAfterInsert: Self.Element)](charactercontrollercomponent/collisionflags/insert(_:).md)
  Adds the given element to the option set if it is not already a member.
- [func intersection(Self) -> Self](charactercontrollercomponent/collisionflags/intersection(_:).md)
  Returns a new option set with only the elements contained in both this set and the given set.
- [func remove(Self.Element) -> Self.Element?](charactercontrollercomponent/collisionflags/remove(_:).md)
  Removes the given element and all elements subsumed by it.
- [func symmetricDifference(Self) -> Self](charactercontrollercomponent/collisionflags/symmetricdifference(_:).md)
  Returns a new option set with the elements contained in this set or in the given set, but not in both.
- [func union(Self) -> Self](charactercontrollercomponent/collisionflags/union(_:).md)
  Returns a new option set of the elements contained in this set, in the given set, or in both.
- [func update(with: Self.Element) -> Self.Element?](charactercontrollercomponent/collisionflags/update(with:).md)
  Inserts the given element into the set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/charactercontrollercomponent/collisionflags/optionset-implementations)*