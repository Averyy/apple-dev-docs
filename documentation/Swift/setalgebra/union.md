# union(_:)

**Framework**: Swift  
**Kind**: method  
**Required**: Yes

Returns a new set with the elements of both this and the given set.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func union(_ other: Self) -> Self
```

#### Return Value

A new set with the unique elements of this set and `other`.

#### Discussion

In the following example, the `attendeesAndVisitors` set is made up of the elements of the `attendees` and `visitors` sets:

```swift
let attendees: Set = ["Alicia", "Bethany", "Diana"]
let visitors = ["Marcia", "Nathaniel"]
let attendeesAndVisitors = attendees.union(visitors)
print(attendeesAndVisitors)
// Prints "["Diana", "Nathaniel", "Bethany", "Alicia", "Marcia"]"
```

If the set already contains one or more elements that are also in `other`, the existing members are kept.

```swift
let initialIndices = Set(0..<5)
let expandedIndices = initialIndices.union([2, 3, 6, 7])
print(expandedIndices)
// Prints "[2, 4, 6, 7, 0, 1, 3]"
```

> **Note**: If this set and `other` contain elements that are equal but distinguishable (e.g. via `===`), which of these elements is present in the result is unspecified.

## Parameters

- `other`: A set of the same type as the current set.

## See Also

- [func formUnion(Self)](setalgebra/formunion(_:).md)
  Adds the elements of the given set to the set.
- [func intersection(Self) -> Self](setalgebra/intersection(_:).md)
  Returns a new set with the elements that are common to both this set and the given set.
- [func formIntersection(Self)](setalgebra/formintersection(_:).md)
  Removes the elements of this set that aren’t also in the given set.
- [func symmetricDifference(Self) -> Self](setalgebra/symmetricdifference(_:).md)
  Returns a new set with the elements that are either in this set or in the given set, but not in both.
- [func formSymmetricDifference(Self)](setalgebra/formsymmetricdifference(_:).md)
  Removes the elements of the set that are also in the given set and adds the members of the given set that are not already in the set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/setalgebra/union(_:))*