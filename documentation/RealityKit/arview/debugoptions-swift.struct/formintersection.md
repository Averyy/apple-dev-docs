# formIntersection(_:)

**Framework**: RealityKit  
**Kind**: method

Removes all elements of this option set that are not also present in the given set.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
mutating func formIntersection(_ other: Self)
```

#### Discussion

This method is implemented as a `&` (bitwise AND) operation on the two sets’ raw values.

## Parameters

- `other`: An option set.

## See Also

- [func union(Self) -> Self](arview/debugoptions-swift.struct/union(_:).md)
  Returns a new option set of the elements contained in this set, in the given set, or in both.
- [func formUnion(Self)](arview/debugoptions-swift.struct/formunion(_:).md)
  Inserts the elements of another set into this option set.
- [func intersection(Self) -> Self](arview/debugoptions-swift.struct/intersection(_:).md)
  Returns a new option set with only the elements contained in both this set and the given set.
- [func symmetricDifference(Self) -> Self](arview/debugoptions-swift.struct/symmetricdifference(_:).md)
  Returns a new option set with the elements contained in this set or in the given set, but not in both.
- [func formSymmetricDifference(Self)](arview/debugoptions-swift.struct/formsymmetricdifference(_:).md)
  Replaces this set with a new set containing all elements contained in either this set or the given set, but not in both.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/arview/debugoptions-swift.struct/formintersection(_:))*