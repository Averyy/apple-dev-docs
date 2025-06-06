# isSubset(of:)

**Framework**: System  
**Kind**: method

Returns a Boolean value that indicates whether the set is a subset of another set.

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
func isSubset(of other: Self) -> Bool
```

#### Return Value

`true` if the set is a subset of `other`; otherwise, `false`.

#### Discussion

Set  is a subset of another set  if every member of  is also a member of .

```swift
let employees: Set = ["Alicia", "Bethany", "Chris", "Diana", "Eric"]
let attendees: Set = ["Alicia", "Bethany", "Diana"]
print(attendees.isSubset(of: employees))
// Prints "true"
```

## Parameters

- `other`: A set of the same type as the current set.

## See Also

- [init()](filedescriptor/openoptions/init.md)
  Creates an empty option set.
- [init<S>(S)](filedescriptor/openoptions/init(_:).md)
  Creates a new set from a finite sequence of items.
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
- [func isSuperset(of: Self) -> Bool](filedescriptor/openoptions/issuperset(of:).md)
  Returns a Boolean value that indicates whether the set is a superset of the given set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filedescriptor/openoptions/issubset(of:))*