# PhysicsSimulationComponent.CollisionOptions

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

The options set that defines how a physics simulation reports collisions.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 1.0+

## Declaration

```swift
struct CollisionOptions
```

## Topics

### Type Properties
- [static let all: PhysicsSimulationComponent.CollisionOptions](./collisionoptions-swift.struct/all.md)
  Reports collisions between kinematic objects and both static and kinematic objects.
- [static let none: PhysicsSimulationComponent.CollisionOptions](./collisionoptions-swift.struct/none.md)
  Opts out of reporting collisions.
- [static let reportKinematicVsKinematic: PhysicsSimulationComponent.CollisionOptions](./collisionoptions-swift.struct/reportkinematicvskinematic.md)
  Reports collisions between kinematic objects.
- [static let reportKinematicVsStatic: PhysicsSimulationComponent.CollisionOptions](./collisionoptions-swift.struct/reportkinematicvsstatic.md)
  Reports collisions between kinematic objects and static objects.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [SetAlgebra](../../Swift/setalgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicssimulationcomponent/collisionoptions-swift.struct)*