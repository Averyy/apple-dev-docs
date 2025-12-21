# IKComponent

**Framework**: RealityKit  
**Kind**: struct

A component that allows you to procedurally animate a skeletal model using a full body inverse kinematics solver.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
struct IKComponent
```

#### Overview

Video games and live productions use inverse kinematics (IK) solvers to procedurally adapt the animation of virtual characters to the environment and the person using the experience. Full body IK solvers produce more life like motion due to each demand affecting the whole body.

Use `IKComponent` to create and control a full body iterative IK solver for your character. The solver procedurally adjusts the pose of your character to the demands you set. This component also maintains the state of the entity’s IK solvers within the overall skeletal animation system.

##### Create a Solver

Define an inverse kinematics rig for the skeleton of the model you want to animate and generate an immutable resource containing it. Create a new component value with the resource.

```swift
// Load a model containing a skeletal mesh.
let armEntity = try await Entity(named: "Arm")

// Fetch the skeleton from the model's MeshResource.
guard let meshResource = entity.components[ModelComponent.self]?.mesh else {
    fatalError("No mesh found")
}

let modelSkeleton = meshResource.contents.skeletons[0]

// Start with the default rig instance for the skeleton without any constraints.
var rig = try IKRig(for: modelSkeleton)

// This is a good place to change default rig level settings. For example, reducing
// the maximum solver iterations reduces the performance cost of the solve but can
// increase error in reaching the demands.
rig.maxIterations = 30

// Refine joint settings.
rig.joints["root/arm_joint/forearm_joint"]?.fkWeightPerAxis = .zero

// Define the joint constraints for the rig.
rig.constraints = [
    // A point constraint is a standard term for a position demand. 
    // See ``IKRig/Constraint/point(named:on:positionWeight:)``
    .point(named: "base_constraint", on: "root/arm_joint", positionWeight: [5.0, 5.0, 5.0]),
    // A parent constraint is a standard term for both position and orientation demands as
    // a single transformation. See ``IKRig/Constraint/parent(named:on:positionWeight:orientationWeight:)``
    .parent(named: "end_constraint", on: "root/arm_joint/forearm_joint/hand_joint",
            positionWeight: [4.0, 4.0, 4.0]),
]

// Make a resource containing the rig.
let resource = try IKResource(rig: rig)

// Add the component to the entity using the new resource.
armEntity.components.set(IKComponent(resource: resource))
```

##### Update Settings and Demands

The initialized component provides update objects matching the structure of the rig. The update objects expose limited set of parameters and the ability to set the constraint demands that can be adjusted each frame.

The forward kinematics (FK) demand is not set in this component. The solver uses the animation pose stored in the [`SkeletalPosesComponent`](skeletalposescomponent.md).

```swift
// Get the IK component value with the current constraint targets.
var component = armEntity.components[IKComponent.self]!

// Compute new demands. In this case a position animated along a circle.
let x = 0.1 * sin(elapsedTime)
let y = 0.1 * cos(elapsedTime)

// Set the new demands and update other relevant settings.
component.solvers[0].constraints["end_constraint"]!.target.translation = [x, y, 0]
component.solvers[0].constraints["end_constraint"]!.animationOverrideWeight.position = 1.0

// Set the updated component value for the updates to be applied to the solver instance.
armEntity.components.set(component)
```

Use a chained call in cases where only a single setting or demand is updated.

```swift
armEntity.components[IKComponent.self]!.solvers[0].constraints["end_constraint"]!
    .animationOverrideWeight.position = 1.0
```

> **Note**: Any value updates won’t be reflected until the modified [`IKComponent`](ikcomponent.md) is set on the [`Entity`](entity.md).

## Topics

### Classes
- [IKComponent.Constraint](ikcomponent/constraint.md)
  The update stage object that lets you read and update the current settings of a single constraint in an IK solver.
- [IKComponent.Joint](ikcomponent/joint.md)
  The update stage object that lets you read and update the current settings of a single joint in an IK solver.
- [IKComponent.Solver](ikcomponent/solver.md)
  The update stage object that lets you read and update the current settings of a single solver instance.
### Structures
- [IKComponent.ConstraintCollection](ikcomponent/constraintcollection.md)
  Ordered dictionary like container with fixed size.
- [IKComponent.JointCollection](ikcomponent/jointcollection.md)
  Ordered dictionary like container with fixed size.
- [IKComponent.SolverCollection](ikcomponent/solvercollection.md)
  Ordered dictionary like container with fixed size.
### Initializers
- [init(resource: IKResource?)](ikcomponent/init(resource:).md)
  Creates a new component value referencing the specified resource.
### Instance Properties
- [var resource: IKResource?](ikcomponent/resource.md)
  Reference to the resource describing the desired inverse kinematics setup.
- [var solvers: IKComponent.SolverCollection](ikcomponent/solvers.md)
  The currently active solvers.

## Relationships

### Conforms To
- [Component](component.md)

## See Also

- [IKComponent.Joint](ikcomponent/joint.md)
  The update stage object that lets you read and update the current settings of a single joint in an IK solver.
- [IKComponent.JointCollection](ikcomponent/jointcollection.md)
  Ordered dictionary like container with fixed size.
- [IKComponent.Solver](ikcomponent/solver.md)
  The update stage object that lets you read and update the current settings of a single solver instance.
- [IKComponent.SolverCollection](ikcomponent/solvercollection.md)
  Ordered dictionary like container with fixed size.
- [IKComponent.Constraint](ikcomponent/constraint.md)
  The update stage object that lets you read and update the current settings of a single constraint in an IK solver.
- [IKComponent.ConstraintCollection](ikcomponent/constraintcollection.md)
  Ordered dictionary like container with fixed size.
- [class IKResource](ikresource.md)
  A reference counted immutable resource which contains one or more inverse kinematics solver rigs.
- [struct IKSolverDefinition](iksolverdefinition.md)
  A container describing a solver instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/ikcomponent)*