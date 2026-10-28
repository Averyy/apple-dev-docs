# IKRig.Constraint

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

A definition of a rig constraint.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
struct Constraint
```

## Overview

Each constraint can have its position and orientation demands enabled individually.

## Topics

### Structures
- [IKRig.Constraint.ID](./constraint/id-swift.struct.md)
  The identity type for a constraint in a rig.
- [IKRig.Constraint.IKOrientationDemand](./constraint/ikorientationdemand.md)
  A definition of an orientational demand.
- [IKRig.Constraint.IKPositionDemand](./constraint/ikpositiondemand.md)
  A definition of a positional demand.
### Instance Properties
- [var id: IKRig.Constraint.ID](./constraint/id-swift.property.md)
  The identifier of the constraint.
- [var jointName: String](./constraint/jointname.md)
  The name of the constrained joint.
- [var name: String](./constraint/name.md)
  The name of the constraint.
- [var offset: Transform](./constraint/offset.md)
  A constraint target offset.
- [var orientationDemand: IKRig.Constraint.IKOrientationDemand?](./constraint/orientationdemand.md)
  The settings of the orientational demand.
- [var positionDemand: IKRig.Constraint.IKPositionDemand?](./constraint/positiondemand.md)
  The settings of the positional demand.
### Type Methods
- [static func lookAtAbsolute(named: String, on: String, lookingAlong: SIMD3<Float>, orientationWeight: SIMD3<Float>) -> IKRig.Constraint](./constraint/lookatabsolute%28named,on,lookingalong,orientationweight%29.md)
  Creates a constraint with only an orientational demand in absolute look-at mode.
- [static func lookAtAdditive(named: String, on: String, lookingAlong: SIMD3<Float>, orientationWeight: SIMD3<Float>) -> IKRig.Constraint](./constraint/lookatadditive%28named,on,lookingalong,orientationweight%29.md)
  Creates a constraint with only an orientational demand in additive look-at mode.
- [static func orient(named: String, on: String, orientationWeight: SIMD3<Float>) -> IKRig.Constraint](./constraint/orient%28named,on,orientationweight%29.md)
  Creates a constraint with only an orientation demand.
- [static func parent(named: String, on: String, positionWeight: SIMD3<Float>, orientationWeight: SIMD3<Float>) -> IKRig.Constraint](./constraint/parent%28named,on,positionweight,orientationweight%29.md)
  Creates a constraint with both a positional and an orientational demands.
- [static func point(named: String, on: String, positionWeight: SIMD3<Float>) -> IKRig.Constraint](./constraint/point%28named,on,positionweight%29.md)
  Creates a constraint with only a positional demand.

## Relationships

### Conforms To
- [Identifiable](../../Swift/identifiable.md)

## See Also

### Inverse kinematics rigs
- [struct IKRig](../ikrig.md)
  A full body inverse kinematics rig definition for a single skeleton.
- [struct Joint](./joint.md)
  A definition of a rig joint and its IK solver settings.
- [struct JointCollection](./jointcollection.md)
  Ordered dictionary-like container with a fixed size.
- [struct ConstraintsCollection](./constraintscollection.md)
  Ordered dictionary-like container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/ikrig/constraint)*