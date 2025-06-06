# remove(_:)

**Framework**: RealityKit  
**Kind**: method

Removes the given element and all elements subsumed by it.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

## Declaration

```swift
@discardableResult
mutating func remove(_ member: Self.Element) -> Self.Element?
```

#### Return Value

The intersection of `[member]` and the set, if the intersection was nonempty; otherwise, `nil`.

#### Discussion

In the following example, the `.priority` shipping option is removed from the `options` option set. Attempting to remove the same shipping option a second time results in `nil`, because `options` no longer contains `.priority` as a member.

```None
var options: ShippingOptions = [.secondDay, .priority]
let priorityOption = options.remove(.priority)
print(priorityOption == .priority)
// Prints "true"

print(options.remove(.priority))
// Prints "nil"
```

In the next example, the `.express` element is passed to `remove(_:)`. Although `.express` is not a member of `options`, `.express` subsumes the remaining `.secondDay` element of the option set. Therefore, `options` is emptied and the intersection between `.express` and `options` is returned.

```None
let expressOption = options.remove(.express)
print(expressOption == .express)
// Prints "false"
print(expressOption == .secondDay)
// Prints "true"
```

## Parameters

- `member`: The element of the set to remove.

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
- [func insert(Self.Element) -> (inserted: Bool, memberAfterInsert: Self.Element)](anchoringcomponent/target-swift.enum/alignment/insert(_:).md)
  Adds the given element to the option set if it is not already a member.
- [func intersection(Self) -> Self](anchoringcomponent/target-swift.enum/alignment/intersection(_:).md)
  Returns a new option set with only the elements contained in both this set and the given set.
- [func isDisjoint(with: Self) -> Bool](anchoringcomponent/target-swift.enum/alignment/isdisjoint(with:).md)
  Returns a Boolean value that indicates whether the set has no members in common with the given set.
- [func isStrictSubset(of: Self) -> Bool](anchoringcomponent/target-swift.enum/alignment/isstrictsubset(of:).md)
  Returns a Boolean value that indicates whether this set is a strict subset of the given set.
- [func isStrictSuperset(of: Self) -> Bool](anchoringcomponent/target-swift.enum/alignment/isstrictsuperset(of:).md)
  Returns a Boolean value that indicates whether this set is a strict superset of the given set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/anchoringcomponent/target-swift.enum/alignment/remove(_:))*