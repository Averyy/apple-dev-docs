# formUnion(_:)

**Framework**: System  
**Kind**: method

Inserts the elements of another set into this option set.

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
mutating func formUnion(_ other: Self)
```

#### Discussion

This method is implemented as a `|` (bitwise OR) operation on the two sets’ raw values.

## Parameters

- `other`: An option set.

## See Also

- [init()](filepermissions/init.md)
  Creates an empty option set.
- [init<S>(S)](filepermissions/init(_:).md)
  Creates a new set from a finite sequence of items.
- [init(arrayLiteral: Self.Element...)](filepermissions/init(arrayliteral:).md)
  Creates a set containing the elements of the given array literal.
- [func contains(Self) -> Bool](filepermissions/contains(_:).md)
  Returns a Boolean value that indicates whether a given element is a member of the option set.
- [func formIntersection(Self)](filepermissions/formintersection(_:).md)
  Removes all elements of this option set that are not also present in the given set.
- [func formIntersection(Self)](filepermissions/formintersection(_:).md)
  Removes all elements of this option set that are not also present in the given set.
- [func formSymmetricDifference(Self)](filepermissions/formsymmetricdifference(_:).md)
  Replaces this set with a new set containing all elements contained in either this set or the given set, but not in both.
- [func insert(Self.Element) -> (inserted: Bool, memberAfterInsert: Self.Element)](filepermissions/insert(_:).md)
  Adds the given element to the option set if it is not already a member.
- [func intersection(Self) -> Self](filepermissions/intersection(_:).md)
  Returns a new option set with only the elements contained in both this set and the given set.
- [func isDisjoint(with: Self) -> Bool](filepermissions/isdisjoint(with:).md)
  Returns a Boolean value that indicates whether the set has no members in common with the given set.
- [var isEmpty: Bool](filepermissions/isempty.md)
  A Boolean value that indicates whether the set has no elements.
- [func isStrictSubset(of: Self) -> Bool](filepermissions/isstrictsubset(of:).md)
  Returns a Boolean value that indicates whether this set is a strict subset of the given set.
- [func isStrictSuperset(of: Self) -> Bool](filepermissions/isstrictsuperset(of:).md)
  Returns a Boolean value that indicates whether this set is a strict superset of the given set.
- [func isSubset(of: Self) -> Bool](filepermissions/issubset(of:).md)
  Returns a Boolean value that indicates whether the set is a subset of another set.
- [func isSuperset(of: Self) -> Bool](filepermissions/issuperset(of:).md)
  Returns a Boolean value that indicates whether the set is a superset of the given set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filepermissions/formunion(_:))*