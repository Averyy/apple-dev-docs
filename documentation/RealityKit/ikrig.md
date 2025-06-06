# IKRig

**Framework**: RealityKit  
**Kind**: struct

A full body inverse kinematics rig definition for a single skeleton.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
struct IKRig
```

#### Overview

Describes the skeleton, its tuning, and the active constraints for the solver instance.

##### Balance of Demands Weights in a Full Body Solver

The full body solver calculates the final pose by balancing the various demands based on their assigned weights. This process ensures that each demand, ranging from forward kinematics (FK) demands to constraints on joint movement, affects the pose proportionally to its importance.

The solver reads the FK demands from the [`SkeletalPosesComponent`](skeletalposescomponent.md). As such these demands are either a playing animation for the model, or just a static pose.

All demands have an element specific weight, and some have a global rig weight. The rig weights influence the overall rig, while element weights adjust individual aspects of the model.

The table below provides detailed mappings of these weights to their respective demand types.

| Demand type | Rig weight | Element weight |
| --- | --- | --- |
| FK demands | [`globalFkWeight`](ikrig/globalfkweight.md) | [`fkWeightPerAxis`](ikrig/joint/fkweightperaxis.md) |
| Joint rotation limits | [`globalLimitsWeight`](ikrig/globallimitsweight.md) | [`weight`](ikrig/joint/limitsdefinition/weight.md) |
| Constraint position | Not applicable | [`weight`](ikrig/constraint/ikpositiondemand/weight.md) |
| Constraint orientation | Not applicable | [`weight`](ikrig/constraint/ikorientationdemand/weight.md) |

> **Note**: While constraints do not have rig weight, they have blending weight between automatic and custom targets. See [`animationOverrideWeight`](ikcomponent/constraint/animationoverrideweight.md) for more information.

While constraints do not have rig weight, they have blending weight between automatic and custom targets. See [`animationOverrideWeight`](ikcomponent/constraint/animationoverrideweight.md) for more information.

## Topics

### Structures
- [struct Constraint](ikrig/constraint.md)
  A definition of a rig constraint.
- [struct ConstraintsCollection](ikrig/constraintscollection.md)
  Ordered dictionary-like container.
- [struct Joint](ikrig/joint.md)
  A definition of a rig joint and its IK solver settings.
- [struct JointCollection](ikrig/jointcollection.md)
  Ordered dictionary-like container with a fixed size.
### Initializers
- [init(for: MeshResource.Skeleton) throws](ikrig/init(for:).md)
  Creates an inverse kinematics rig definition for the provided skeleton.
### Instance Properties
- [var constraints: IKRig.ConstraintsCollection](ikrig/constraints.md)
  A collection of all of the rig’s constraint settings.
- [var globalFkWeight: Float](ikrig/globalfkweight.md)
  The solver global weight for the forward kinematics demands.
- [var globalLimitsWeight: Float](ikrig/globallimitsweight.md)
  The solver global weight for the joint rotation limits.
- [var joints: IKRig.JointCollection](ikrig/joints.md)
  A collection of all of the rig’s joint settings.
- [var maxIterations: Int](ikrig/maxiterations.md)
  The maximum number of iterations the solver is allowed to do per frame.

## See Also

- [struct Joint](ikrig/joint.md)
  A definition of a rig joint and its IK solver settings.
- [struct JointCollection](ikrig/jointcollection.md)
  Ordered dictionary-like container with a fixed size.
- [struct Constraint](ikrig/constraint.md)
  A definition of a rig constraint.
- [struct ConstraintsCollection](ikrig/constraintscollection.md)
  Ordered dictionary-like container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/ikrig)*