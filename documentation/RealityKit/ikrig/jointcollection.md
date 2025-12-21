# IKRig.JointCollection

**Framework**: RealityKit  
**Kind**: struct

Ordered dictionary-like container with a fixed size.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
struct JointCollection
```

#### Overview

Supports subscripting by index, element’s identifier or element’s name.

## Topics

### Instance Properties
- [var count: Int](ikrig/jointcollection/count.md)
  The number of elements in the collection.
- [var isEmpty: Bool](ikrig/jointcollection/isempty.md)
  A Boolean value indicating whether the collection is empty.
### Instance Methods
- [func contains(IKRig.JointCollection.Element.ID) -> Bool](ikrig/jointcollection/contains(_:).md)
  Returns a Boolean value that indicates whether the collection contains an element with a specific identifier.
- [func forEach(descendantOf: String, inclusive: Bool, update: (inout IKRig.JointCollection.Element) -> Void)](ikrig/jointcollection/foreach(descendantof:inclusive:update:).md)
  Calls the provided closure on each element in the hierarchy rooted at the named joint.
- [func set(IKRig.JointCollection.Element) -> IKRig.JointCollection.Element?](ikrig/jointcollection/set(_:).md)
  Updates the element with identifier matching the provided value’s identifier.
### Subscripts
- [subscript(_:)](ikrig/jointcollection/subscript(_:).md)
  Accesses the element with the specified identifier.

## Relationships

### Conforms To
- [Collection](../Swift/Collection.md)
- [Sequence](../Swift/Sequence.md)

## See Also

- [struct IKRig](ikrig.md)
  A full body inverse kinematics rig definition for a single skeleton.
- [struct Joint](ikrig/joint.md)
  A definition of a rig joint and its IK solver settings.
- [struct Constraint](ikrig/constraint.md)
  A definition of a rig constraint.
- [struct ConstraintsCollection](ikrig/constraintscollection.md)
  Ordered dictionary-like container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/ikrig/jointcollection)*