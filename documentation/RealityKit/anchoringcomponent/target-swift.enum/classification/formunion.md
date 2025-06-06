# formUnion(_:)

**Framework**: RealityKit  
**Kind**: method

Inserts the elements of another set into this option set.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

## Declaration

```swift
mutating func formUnion(_ other: Self)
```

#### Discussion

This method is implemented as a `|` (bitwise OR) operation on the two sets’ raw values.

## Parameters

- `other`: An option set.

## See Also

- [static func != (Self, Self) -> Bool](anchoringcomponent/target-swift.enum/classification/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
- [AnchoringComponent.Target.Classification.ArrayLiteralElement](anchoringcomponent/target-swift.enum/classification/arrayliteralelement.md)
  The type of the elements of an array literal.
- [AnchoringComponent.Target.Classification.Element](anchoringcomponent/target-swift.enum/classification/element.md)
  The element type of the option set.
- [AnchoringComponent.Target.Classification.RawValue](anchoringcomponent/target-swift.enum/classification/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
- [var isEmpty: Bool](anchoringcomponent/target-swift.enum/classification/isempty.md)
  A Boolean value that indicates whether the set has no elements.
- [let rawValue: UInt64](anchoringcomponent/target-swift.enum/classification/rawvalue-swift.property.md)
  The corresponding value of the raw type.
- [func contains(Self) -> Bool](anchoringcomponent/target-swift.enum/classification/contains(_:).md)
  Returns a Boolean value that indicates whether a given element is a member of the option set.
- [func formIntersection(Self)](anchoringcomponent/target-swift.enum/classification/formintersection(_:).md)
  Removes all elements of this option set that are not also present in the given set.
- [func formSymmetricDifference(Self)](anchoringcomponent/target-swift.enum/classification/formsymmetricdifference(_:).md)
  Replaces this set with a new set containing all elements contained in either this set or the given set, but not in both.
- [func insert(Self.Element) -> (inserted: Bool, memberAfterInsert: Self.Element)](anchoringcomponent/target-swift.enum/classification/insert(_:).md)
  Adds the given element to the option set if it is not already a member.
- [func intersection(Self) -> Self](anchoringcomponent/target-swift.enum/classification/intersection(_:).md)
  Returns a new option set with only the elements contained in both this set and the given set.
- [func isDisjoint(with: Self) -> Bool](anchoringcomponent/target-swift.enum/classification/isdisjoint(with:).md)
  Returns a Boolean value that indicates whether the set has no members in common with the given set.
- [func isStrictSubset(of: Self) -> Bool](anchoringcomponent/target-swift.enum/classification/isstrictsubset(of:).md)
  Returns a Boolean value that indicates whether this set is a strict subset of the given set.
- [func isStrictSuperset(of: Self) -> Bool](anchoringcomponent/target-swift.enum/classification/isstrictsuperset(of:).md)
  Returns a Boolean value that indicates whether this set is a strict superset of the given set.
- [func isSubset(of: Self) -> Bool](anchoringcomponent/target-swift.enum/classification/issubset(of:).md)
  Returns a Boolean value that indicates whether the set is a subset of another set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/anchoringcomponent/target-swift.enum/classification/formunion(_:))*