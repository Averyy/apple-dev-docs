# formUnion(_:)

**Framework**: RealityKit  
**Kind**: method

Inserts the elements of another set into this option set.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+

## Declaration

```swift
mutating func formUnion(_ other: Self)
```

#### Discussion

This method is implemented as a `|` (bitwise OR) operation on the two sets’ raw values.

## Parameters

- `other`: An option set.

## See Also

- [func union(Self) -> Self](arview/entitygestures/union(_:).md)
  Returns a new option set of the elements contained in this set, in the given set, or in both.
- [func intersection(Self) -> Self](arview/entitygestures/intersection(_:).md)
  Returns a new option set with only the elements contained in both this set and the given set.
- [func formIntersection(Self)](arview/entitygestures/formintersection(_:).md)
  Removes all elements of this option set that are not also present in the given set.
- [func symmetricDifference(Self) -> Self](arview/entitygestures/symmetricdifference(_:).md)
  Returns a new option set with the elements contained in this set or in the given set, but not in both.
- [func formSymmetricDifference(Self)](arview/entitygestures/formsymmetricdifference(_:).md)
  Replaces this set with a new set containing all elements contained in either this set or the given set, but not in both.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/arview/entitygestures/formunion(_:))*