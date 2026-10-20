# IKRig.ConstraintsCollection

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

Ordered dictionary-like container.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
struct ConstraintsCollection
```

#### Overview

Supports subscripting by index, element’s identifier or element’s name.

## Topics

### Initializers
- [init([IKRig.ConstraintsCollection.Element])](./constraintscollection/init%28_%29.md)
  Creates a collection with the provided constraints.
### Instance Properties
- [var count: Int](./constraintscollection/count.md)
  The number of elements in the collection.
- [var isEmpty: Bool](./constraintscollection/isempty.md)
  A Boolean value indicating whether the collection is empty.
### Instance Methods
- [func contains(IKRig.ConstraintsCollection.Element.ID) -> Bool](./constraintscollection/contains%28_%29.md)
  Returns a Boolean value that indicates whether the collection contains an element with a specific identifier.
- [func set(IKRig.ConstraintsCollection.Element) -> IKRig.ConstraintsCollection.Element?](./constraintscollection/set%28_%29.md)
  Updates the element with identifier matching the provided value’s identifier.
### Subscripts
- [subscript(_:)](./constraintscollection/subscript%28_%29.md)
  Accesses the element with the specified identifier.

## Relationships

### Conforms To
- [Collection](../../Swift/collection.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [Sequence](../../Swift/sequence.md)

## See Also

### Inverse kinematics rigs
- [struct IKRig](../ikrig.md)
  A full body inverse kinematics rig definition for a single skeleton.
- [struct Joint](./joint.md)
  A definition of a rig joint and its IK solver settings.
- [struct JointCollection](./jointcollection.md)
  Ordered dictionary-like container with a fixed size.
- [struct Constraint](./constraint.md)
  A definition of a rig constraint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/ikrig/constraintscollection)*