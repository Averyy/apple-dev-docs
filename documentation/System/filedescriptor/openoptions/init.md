# init(_:)

**Framework**: System  
**Kind**: init

Creates a new set from a finite sequence of items.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
init<S>(_ sequence: S) where S : Sequence, Self.Element == S.Element
```

#### Discussion

Use this initializer to create a new set from an existing sequence, like an array or a range:

```swift
let validIndices = Set(0..<7).subtracting([2, 4, 5])
print(validIndices)
// Prints "[6, 0, 1, 3]"
```

## Parameters

- `sequence`: The elements to use as members of the new set.

## See Also

- [init()](filedescriptor/openoptions/init.md)
  Creates an empty option set.
- [init(arrayLiteral: Self.Element...)](filedescriptor/openoptions/init(arrayliteral:).md)
  Creates a set containing the elements of the given array literal.
- [func contains(Self) -> Bool](filedescriptor/openoptions/contains(_:).md)
  Returns a Boolean value that indicates whether a given element is a member of the option set.
- [func formIntersection(Self)](filedescriptor/openoptions/formintersection(_:).md)
  Removes all elements of this option set that are not also present in the given set.
- [func formIntersection(Self)](filedescriptor/openoptions/formintersection(_:).md)
  Removes all elements of this option set that are not also present in the given set.
- [func formSymmetricDifference(Self)](filedescriptor/openoptions/formsymmetricdifference(_:).md)
  Replaces this set with a new set containing all elements contained in either this set or the given set, but not in both.
- [func formUnion(Self)](filedescriptor/openoptions/formunion(_:).md)
  Inserts the elements of another set into this option set.
- [func insert(Self.Element) -> (inserted: Bool, memberAfterInsert: Self.Element)](filedescriptor/openoptions/insert(_:).md)
  Adds the given element to the option set if it is not already a member.
- [func intersection(Self) -> Self](filedescriptor/openoptions/intersection(_:).md)
  Returns a new option set with only the elements contained in both this set and the given set.
- [func isDisjoint(with: Self) -> Bool](filedescriptor/openoptions/isdisjoint(with:).md)
  Returns a Boolean value that indicates whether the set has no members in common with the given set.
- [var isEmpty: Bool](filedescriptor/openoptions/isempty.md)
  A Boolean value that indicates whether the set has no elements.
- [func isStrictSubset(of: Self) -> Bool](filedescriptor/openoptions/isstrictsubset(of:).md)
  Returns a Boolean value that indicates whether this set is a strict subset of the given set.
- [func isStrictSuperset(of: Self) -> Bool](filedescriptor/openoptions/isstrictsuperset(of:).md)
  Returns a Boolean value that indicates whether this set is a strict superset of the given set.
- [func isSubset(of: Self) -> Bool](filedescriptor/openoptions/issubset(of:).md)
  Returns a Boolean value that indicates whether the set is a subset of another set.
- [func isSuperset(of: Self) -> Bool](filedescriptor/openoptions/issuperset(of:).md)
  Returns a Boolean value that indicates whether the set is a superset of the given set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filedescriptor/openoptions/init(_:))*