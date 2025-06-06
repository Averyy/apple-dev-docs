# formUnion(_:)

**Framework**: Swift  
**Kind**: method  
**Required**: Yes

Adds the elements of the given set to the set.

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
mutating func formUnion(_ other: Self)
```

#### Discussion

In the following example, the elements of the `visitors` set are added to the `attendees` set:

```swift
var attendees: Set = ["Alicia", "Bethany", "Diana"]
let visitors: Set = ["Diana", "Marcia", "Nathaniel"]
attendees.formUnion(visitors)
print(attendees)
// Prints "["Diana", "Nathaniel", "Bethany", "Alicia", "Marcia"]"
```

If the set already contains one or more elements that are also in `other`, the existing members are kept.

```swift
var initialIndices = Set(0..<5)
initialIndices.formUnion([2, 3, 6, 7])
print(initialIndices)
// Prints "[2, 4, 6, 7, 0, 1, 3]"
```

## Parameters

- `other`: A set of the same type as the current set.

## See Also

- [func union(Self) -> Self](setalgebra/union(_:).md)
  Returns a new set with the elements of both this and the given set.
- [func intersection(Self) -> Self](setalgebra/intersection(_:).md)
  Returns a new set with the elements that are common to both this set and the given set.
- [func formIntersection(Self)](setalgebra/formintersection(_:).md)
  Removes the elements of this set that aren’t also in the given set.
- [func symmetricDifference(Self) -> Self](setalgebra/symmetricdifference(_:).md)
  Returns a new set with the elements that are either in this set or in the given set, but not in both.
- [func formSymmetricDifference(Self)](setalgebra/formsymmetricdifference(_:).md)
  Removes the elements of the set that are also in the given set and adds the members of the given set that are not already in the set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/setalgebra/formunion(_:))*