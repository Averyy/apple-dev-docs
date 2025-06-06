# ARView.EntityGestures

**Framework**: RealityKit  
**Kind**: struct

The set of possible entity gesture recognizers.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+

## Declaration

```swift
struct EntityGestures
```

## Topics

### Recognizing gesture types
- [static let all: ARView.EntityGestures](arview/entitygestures/all.md)
  All gesture types.
- [static let rotation: ARView.EntityGestures](arview/entitygestures/rotation.md)
  A multitouch gesture used to rotate an entity.
- [static let scale: ARView.EntityGestures](arview/entitygestures/scale.md)
  A pinch gesture used to scale an entity.
- [static let translation: ARView.EntityGestures](arview/entitygestures/translation.md)
  A single touch pan gesture used to move entities along their anchoring plane.
### Creating gesture option sets
- [init()](arview/entitygestures/init.md)
  Creates an empty option set.
- [init<S>(S)](arview/entitygestures/init(_:).md)
  Creates a new set from a finite sequence of items.
- [init(arrayLiteral: Self.Element...)](arview/entitygestures/init(arrayliteral:).md)
  Creates a set containing the elements of the given array literal.
- [ARView.EntityGestures.Element](arview/entitygestures/element.md)
  The element type of the option set.
- [ARView.EntityGestures.ArrayLiteralElement](arview/entitygestures/arrayliteralelement.md)
  The type of the elements of an array literal.
- [init(rawValue: Int)](arview/entitygestures/init(rawvalue:).md)
  Creates a new option set from the given raw value.
- [let rawValue: Int](arview/entitygestures/rawvalue-swift.property.md)
  The corresponding value of the raw type.
- [ARView.EntityGestures.RawValue](arview/entitygestures/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Testing for membership
- [var isEmpty: Bool](arview/entitygestures/isempty.md)
  A Boolean value that indicates whether the set has no elements.
- [func contains(Self) -> Bool](arview/entitygestures/contains(_:).md)
  Returns a Boolean value that indicates whether a given element is a member of the option set.
### Adding and removing options
- [func insert(Self.Element) -> (inserted: Bool, memberAfterInsert: Self.Element)](arview/entitygestures/insert(_:).md)
  Adds the given element to the option set if it is not already a member.
- [func update(with: Self.Element) -> Self.Element?](arview/entitygestures/update(with:).md)
  Inserts the given element into the set.
- [func remove(Self.Element) -> Self.Element?](arview/entitygestures/remove(_:).md)
  Removes the given element and all elements subsumed by it.
- [func subtract(Self)](arview/entitygestures/subtract(_:).md)
  Removes the elements of the given set from this set.
- [func subtracting(Self) -> Self](arview/entitygestures/subtracting(_:).md)
  Returns a new set containing the elements of this set that do not occur in the given set.
### Combining options
- [func union(Self) -> Self](arview/entitygestures/union(_:).md)
  Returns a new option set of the elements contained in this set, in the given set, or in both.
- [func formUnion(Self)](arview/entitygestures/formunion(_:).md)
  Inserts the elements of another set into this option set.
- [func intersection(Self) -> Self](arview/entitygestures/intersection(_:).md)
  Returns a new option set with only the elements contained in both this set and the given set.
- [func formIntersection(Self)](arview/entitygestures/formintersection(_:).md)
  Removes all elements of this option set that are not also present in the given set.
- [func symmetricDifference(Self) -> Self](arview/entitygestures/symmetricdifference(_:).md)
  Returns a new option set with the elements contained in this set or in the given set, but not in both.
- [func formSymmetricDifference(Self)](arview/entitygestures/formsymmetricdifference(_:).md)
  Replaces this set with a new set containing all elements contained in either this set or the given set, but not in both.
### Comparing options
- [static func != (Self, Self) -> Bool](arview/entitygestures/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
- [func isSubset(of: Self) -> Bool](arview/entitygestures/issubset(of:).md)
  Returns a Boolean value that indicates whether the set is a subset of another set.
- [func isStrictSubset(of: Self) -> Bool](arview/entitygestures/isstrictsubset(of:).md)
  Returns a Boolean value that indicates whether this set is a strict subset of the given set.
- [func isSuperset(of: Self) -> Bool](arview/entitygestures/issuperset(of:).md)
  Returns a Boolean value that indicates whether the set is a superset of the given set.
- [func isStrictSuperset(of: Self) -> Bool](arview/entitygestures/isstrictsuperset(of:).md)
  Returns a Boolean value that indicates whether this set is a strict superset of the given set.
- [func isDisjoint(with: Self) -> Bool](arview/entitygestures/isdisjoint(with:).md)
  Returns a Boolean value that indicates whether the set has no members in common with the given set.
### Using entity gestures
- [protocol EntityGestureRecognizer](entitygesturerecognizer.md)
  A gesture recognizer that works on entities.
- [class EntityRotationGestureRecognizer](entityrotationgesturerecognizer.md)
  A gesture recognizer that uses rotation gestures involving two touches to rotate a given entity.
- [class EntityScaleGestureRecognizer](entityscalegesturerecognizer.md)
  A gesture recognizer that uses a pinch gesture to scale or zoom an entity.
- [class EntityTranslationGestureRecognizer](entitytranslationgesturerecognizer.md)
  A gesture recognizer that uses a pan gesture to move an entity.
### Default Implementations
- [Equatable Implementations](arview/entitygestures/equatable-implementations.md)
- [OptionSet Implementations](arview/entitygestures/optionset-implementations.md)
- [SetAlgebra Implementations](arview/entitygestures/setalgebra-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [class EntityRotationGestureRecognizer](entityrotationgesturerecognizer.md)
  A gesture recognizer that uses rotation gestures involving two touches to rotate a given entity.
- [class EntityScaleGestureRecognizer](entityscalegesturerecognizer.md)
  A gesture recognizer that uses a pinch gesture to scale or zoom an entity.
- [class EntityTranslationGestureRecognizer](entitytranslationgesturerecognizer.md)
  A gesture recognizer that uses a pan gesture to move an entity.
- [protocol EntityGestureRecognizer](entitygesturerecognizer.md)
  A gesture recognizer that works on entities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/arview/entitygestures)*