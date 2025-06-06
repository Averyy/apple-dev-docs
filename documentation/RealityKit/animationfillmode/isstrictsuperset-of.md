# isStrictSuperset(of:)

**Framework**: RealityKit  
**Kind**: method

Returns a Boolean value that indicates whether this set is a strict superset of the given set.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

## Declaration

```swift
func isStrictSuperset(of other: Self) -> Bool
```

#### Return Value

`true` if the set is a strict superset of `other`; otherwise, `false`.

#### Discussion

Set  is a strict superset of another set  if every member of  is also a member of  and  contains at least one element that is  a member of .

```None
let employees: Set = ["Alicia", "Bethany", "Chris", "Diana", "Eric"]
let attendees: Set = ["Alicia", "Bethany", "Diana"]
print(employees.isStrictSuperset(of: attendees))
// Prints "true"

// A set is never a strict superset of itself:
print(employees.isStrictSuperset(of: employees))
// Prints "false"
```

## Parameters

- `other`: A set of the same type as the current set.

## See Also

- [var isEmpty: Bool](animationfillmode/isempty.md)
  A Boolean value that indicates whether the set has no elements.
- [func contains(Self) -> Bool](animationfillmode/contains(_:).md)
  Returns a Boolean value that indicates whether a given element is a member of the option set.
- [func formIntersection(Self)](animationfillmode/formintersection(_:).md)
  Removes all elements of this option set that are not also present in the given set.
- [func formSymmetricDifference(Self)](animationfillmode/formsymmetricdifference(_:).md)
  Replaces this set with a new set containing all elements contained in either this set or the given set, but not in both.
- [func formUnion(Self)](animationfillmode/formunion(_:).md)
  Inserts the elements of another set into this option set.
- [func insert(Self.Element) -> (inserted: Bool, memberAfterInsert: Self.Element)](animationfillmode/insert(_:).md)
  Adds the given element to the option set if it is not already a member.
- [func intersection(Self) -> Self](animationfillmode/intersection(_:).md)
  Returns a new option set with only the elements contained in both this set and the given set.
- [func isDisjoint(with: Self) -> Bool](animationfillmode/isdisjoint(with:).md)
  Returns a Boolean value that indicates whether the set has no members in common with the given set.
- [func isStrictSubset(of: Self) -> Bool](animationfillmode/isstrictsubset(of:).md)
  Returns a Boolean value that indicates whether this set is a strict subset of the given set.
- [func isSubset(of: Self) -> Bool](animationfillmode/issubset(of:).md)
  Returns a Boolean value that indicates whether the set is a subset of another set.
- [func isSuperset(of: Self) -> Bool](animationfillmode/issuperset(of:).md)
  Returns a Boolean value that indicates whether the set is a superset of the given set.
- [func remove(Self.Element) -> Self.Element?](animationfillmode/remove(_:).md)
  Removes the given element and all elements subsumed by it.
- [func subtract(Self)](animationfillmode/subtract(_:).md)
  Removes the elements of the given set from this set.
- [func subtracting(Self) -> Self](animationfillmode/subtracting(_:).md)
  Returns a new set containing the elements of this set that do not occur in the given set.
- [func symmetricDifference(Self) -> Self](animationfillmode/symmetricdifference(_:).md)
  Returns a new option set with the elements contained in this set or in the given set, but not in both.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationfillmode/isstrictsuperset(of:))*