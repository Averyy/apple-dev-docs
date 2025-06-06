# AnchoringComponent.Target.Alignment

**Framework**: RealityKit  
**Kind**: struct

Defines the alignment of real-world surfaces to seek as targets.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
struct Alignment
```

## Topics

### Choosing an alignment
- [static let horizontal: AnchoringComponent.Target.Alignment](anchoringcomponent/target-swift.enum/alignment/horizontal.md)
  Horizontal surfaces.
- [static let vertical: AnchoringComponent.Target.Alignment](anchoringcomponent/target-swift.enum/alignment/vertical.md)
  Vertical surfaces.
- [static let any: AnchoringComponent.Target.Alignment](anchoringcomponent/target-swift.enum/alignment/any.md)
  Surfaces of any alignment.
### Creating an alignment instance
- [init()](anchoringcomponent/target-swift.enum/alignment/init.md)
  Creates an empty option set.
- [init<S>(S)](anchoringcomponent/target-swift.enum/alignment/init(_:).md)
  Creates a new set from a finite sequence of items.
- [init(arrayLiteral: Self.Element...)](anchoringcomponent/target-swift.enum/alignment/init(arrayliteral:).md)
  Creates a set containing the elements of the given array literal.
- [init(rawValue: UInt8)](anchoringcomponent/target-swift.enum/alignment/init(rawvalue:).md)
  Creates a new option set from the given raw value.
### Option set conformance
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
- [func isSubset(of: Self) -> Bool](anchoringcomponent/target-swift.enum/alignment/issubset(of:).md)
  Returns a Boolean value that indicates whether the set is a subset of another set.
- [func isSuperset(of: Self) -> Bool](anchoringcomponent/target-swift.enum/alignment/issuperset(of:).md)
  Returns a Boolean value that indicates whether the set is a superset of the given set.
- [func remove(Self.Element) -> Self.Element?](anchoringcomponent/target-swift.enum/alignment/remove(_:).md)
  Removes the given element and all elements subsumed by it.
- [func subtract(Self)](anchoringcomponent/target-swift.enum/alignment/subtract(_:).md)
  Removes the elements of the given set from this set.
- [func subtracting(Self) -> Self](anchoringcomponent/target-swift.enum/alignment/subtracting(_:).md)
  Returns a new set containing the elements of this set that do not occur in the given set.
- [func symmetricDifference(Self) -> Self](anchoringcomponent/target-swift.enum/alignment/symmetricdifference(_:).md)
  Returns a new option set with the elements contained in this set or in the given set, but not in both.
- [func union(Self) -> Self](anchoringcomponent/target-swift.enum/alignment/union(_:).md)
  Returns a new option set of the elements contained in this set, in the given set, or in both.
- [func update(with: Self.Element) -> Self.Element?](anchoringcomponent/target-swift.enum/alignment/update(with:).md)
  Inserts the given element into the set.
### Default Implementations
- [Equatable Implementations](anchoringcomponent/target-swift.enum/alignment/equatable-implementations.md)
- [OptionSet Implementations](anchoringcomponent/target-swift.enum/alignment/optionset-implementations.md)
- [SetAlgebra Implementations](anchoringcomponent/target-swift.enum/alignment/setalgebra-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [AnchoringComponent.Target.Classification](anchoringcomponent/target-swift.enum/classification.md)
  Defines types of real-world surfaces to seek as targets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/anchoringcomponent/target-swift.enum/alignment)*