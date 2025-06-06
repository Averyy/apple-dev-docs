# Character control, skeletons, and inverse kinematics

**Framework**: RealityKit

Direct the movements and animation of models.

#### Overview

Games and immersive game-like experiences often rely on animated character models to represent the player or non-player characters. The `CharacterControllerComponent` simplifies the process of moving a character around a scene. It handles basic movement, including navigating up and down stairs and slopes and jumping. It also allows you to sync the character movement with specific animations.

To further animate models in the scene, you may need to define a [`SkeletalPose`](skeletalpose.md) or adopt a full inverse kinematics solution with [`IKComponent`](ikcomponent.md).

## Topics

### Character control
- [struct CharacterControllerComponent](charactercontrollercomponent.md)
  A component that manages character movement.
- [CharacterControllerComponent.Collision](charactercontrollercomponent/collision.md)
  A container that holds collision state for the character controller.
- [CharacterControllerComponent.CollisionFlags](charactercontrollercomponent/collisionflags.md)
  An option set that specifies which parts of the character capsule have collided with other objects.
- [struct CharacterControllerStateComponent](charactercontrollerstatecomponent.md)
  A component that represents the state of a character controller.
### Skeletons
- [struct SkeletalPosesComponent](skeletalposescomponent.md)
  A component that exposes the collection of named animation skeletal poses.
- [struct SkeletalPose](skeletalpose.md)
  A container that holds the position and orientation of each joint in a single animation skeleton.
- [SkeletalPose.ID](skeletalpose/id-swift.typealias.md)
  A type representing the stable identity of the entity associated with an instance.
- [struct SkeletalPoseSet](skeletalposeset.md)
  A collection of named skeletal poses.
- [SkeletalPoseSet.Element](skeletalposeset/element.md)
  A type representing the sequence’s elements.
### Inverse kinematics components
- [struct IKComponent](ikcomponent.md)
  A component that allows you to procedurally animate a skeletal model using a full body inverse kinematics solver.
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
- [IKSolverDefinition.ID](iksolverdefinition/id-swift.typealias.md)
  A type representing the stable identity of the entity associated with an instance.
### Inverse kinematics rigs
- [struct IKRig](ikrig.md)
  A full body inverse kinematics rig definition for a single skeleton.
- [struct Joint](ikrig/joint.md)
  A definition of a rig joint and its IK solver settings.
- [struct JointCollection](ikrig/jointcollection.md)
  Ordered dictionary-like container with a fixed size.
- [struct Constraint](ikrig/constraint.md)
  A definition of a rig constraint.
- [struct ConstraintsCollection](ikrig/constraintscollection.md)
  Ordered dictionary-like container.

## See Also

- [Gaming sample code projects](game-development-sample-code.md)
  Explore a collection of projects relating to game development.
- [Entity animations](game-development-entity-animations.md)
  Dynamically move, rotate, and scale entities at runtime.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/game-development-character-skeletons)*