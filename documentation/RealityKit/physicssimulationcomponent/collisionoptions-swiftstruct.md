# PhysicsSimulationComponent.CollisionOptions

**Framework**: RealityKit  
**Kind**: struct

The options set that defines how a physics simulation reports collisions.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
struct CollisionOptions
```

## Topics

### Initializers
- [init(rawValue: UInt8)](physicssimulationcomponent/collisionoptions-swift.struct/init(rawvalue:).md)
  Creates a new option set from the given raw value.
### Instance Properties
- [let rawValue: UInt8](physicssimulationcomponent/collisionoptions-swift.struct/rawvalue-swift.property.md)
  The corresponding value of the raw type.
### Type Aliases
- [PhysicsSimulationComponent.CollisionOptions.ArrayLiteralElement](physicssimulationcomponent/collisionoptions-swift.struct/arrayliteralelement.md)
  The type of the elements of an array literal.
- [PhysicsSimulationComponent.CollisionOptions.Element](physicssimulationcomponent/collisionoptions-swift.struct/element.md)
  The element type of the option set.
- [PhysicsSimulationComponent.CollisionOptions.RawValue](physicssimulationcomponent/collisionoptions-swift.struct/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Type Properties
- [static let all: PhysicsSimulationComponent.CollisionOptions](physicssimulationcomponent/collisionoptions-swift.struct/all.md)
  Reports collisions between kinematic objects and both static and kinematic objects.
- [static let none: PhysicsSimulationComponent.CollisionOptions](physicssimulationcomponent/collisionoptions-swift.struct/none.md)
  Opts out of reporting collisions.
- [static let reportKinematicVsKinematic: PhysicsSimulationComponent.CollisionOptions](physicssimulationcomponent/collisionoptions-swift.struct/reportkinematicvskinematic.md)
  Reports collisions between kinematic objects.
- [static let reportKinematicVsStatic: PhysicsSimulationComponent.CollisionOptions](physicssimulationcomponent/collisionoptions-swift.struct/reportkinematicvsstatic.md)
  Reports collisions between kinematic objects and static objects.
### Default Implementations
- [Equatable Implementations](physicssimulationcomponent/collisionoptions-swift.struct/equatable-implementations.md)
- [OptionSet Implementations](physicssimulationcomponent/collisionoptions-swift.struct/optionset-implementations.md)
- [SetAlgebra Implementations](physicssimulationcomponent/collisionoptions-swift.struct/setalgebra-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicssimulationcomponent/collisionoptions-swift.struct)*