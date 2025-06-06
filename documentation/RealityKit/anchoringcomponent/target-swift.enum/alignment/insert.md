# insert(_:)

**Framework**: RealityKit  
**Kind**: method

Adds the given element to the option set if it is not already a member.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

## Declaration

```swift
@discardableResult
mutating func insert(_ newMember: Self.Element) -> (inserted: Bool, memberAfterInsert: Self.Element)
```

#### Return Value

`(true, newMember)` if `newMember` was not contained in `self`. Otherwise, returns `(false, oldMember)`, where `oldMember` is the member of the set equal to `newMember`.

#### Discussion

In the following example, the `.secondDay` shipping option is added to the `freeOptions` option set if `purchasePrice` is greater than 50.0. For the `ShippingOptions` declaration, see the `OptionSet` protocol discussion.

```None
let purchasePrice = 87.55

var freeOptions: ShippingOptions = [.standard, .priority]
if purchasePrice > 50 {
    freeOptions.insert(.secondDay)
}
print(freeOptions.contains(.secondDay))
// Prints "true"
```

## Parameters

- `newMember`: The element to insert.

## See Also

- [static func != (Self, Self) -> Bool](anchoringcomponent/target-swift.enum/alignment/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
- [AnchoringComponent.Target.Alignment.ArrayLiteralElement](anchoringcomponent/target-swift.enum/alignment/arrayliteralelement.md)
  The type of the elements of an array literal.
- [AnchoringComponent.Target.Alignment.Element](anchoringcomponent/target-swift.enum/alignment/element.md)
  The element type of the option set.
- [AnchoringComponent.Target.Alignment.RawValue](anchoringcomponent/target-swift.enum/alignment/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
- [var isEmpty: Bool](anchoringcomponent/target-swift.enum/alignment/isempty.md)
  A Boolean value that indicates whether the set has no elements.
- [let rawValue: UInt8](anchoringcomponent/target-swift.enum/alignment/rawvalue-swift.property.md)
  The corresponding value of the raw type.
- [func contains(Self) -> Bool](anchoringcomponent/target-swift.enum/alignment/contains(_:).md)
  Returns a Boolean value that indicates whether a given element is a member of the option set.
- [func formIntersection(Self)](anchoringcomponent/target-swift.enum/alignment/formintersection(_:).md)
  Removes all elements of this option set that are not also present in the given set.
- [func formSymmetricDifference(Self)](anchoringcomponent/target-swift.enum/alignment/formsymmetricdifference(_:).md)
  Replaces this set with a new set containing all elements contained in either this set or the given set, but not in both.
- [func formUnion(Self)](anchoringcomponent/target-swift.enum/alignment/formunion(_:).md)
  Inserts the elements of another set into this option set.
- [func intersection(Self) -> Self](anchoringcomponent/target-swift.enum/alignment/intersection(_:).md)
  Returns a new option set with only the elements contained in both this set and the given set.
- [func isDisjoint(with: Self) -> Bool](anchoringcomponent/target-swift.enum/alignment/isdisjoint(with:).md)
  Returns a Boolean value that indicates whether the set has no members in common with the given set.
- [func isStrictSubset(of: Self) -> Bool](anchoringcomponent/target-swift.enum/alignment/isstrictsubset(of:).md)
  Returns a Boolean value that indicates whether this set is a strict subset of the given set.
- [func isStrictSuperset(of: Self) -> Bool](anchoringcomponent/target-swift.enum/alignment/isstrictsuperset(of:).md)
  Returns a Boolean value that indicates whether this set is a strict superset of the given set.
- [func isSubset(of: Self) -> Bool](anchoringcomponent/target-swift.enum/alignment/issubset(of:).md)
  Returns a Boolean value that indicates whether the set is a subset of another set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/anchoringcomponent/target-swift.enum/alignment/insert(_:))*