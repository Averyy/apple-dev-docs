# CollisionComponent.CollisionOptions

**Framework**: RealityKit  
**Kind**: struct

The options set that defines how a collision object reports collisions.

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
- [init(rawValue: UInt)](collisioncomponent/collisionoptions-swift.struct/init(rawvalue:).md)
  Creates a new option set from the given raw value.
### Instance Properties
- [let rawValue: UInt](collisioncomponent/collisionoptions-swift.struct/rawvalue-swift.property.md)
  The corresponding value of the raw type.
### Type Aliases
- [CollisionComponent.CollisionOptions.ArrayLiteralElement](collisioncomponent/collisionoptions-swift.struct/arrayliteralelement.md)
  The type of the elements of an array literal.
- [CollisionComponent.CollisionOptions.Element](collisioncomponent/collisionoptions-swift.struct/element.md)
  The element type of the option set.
- [CollisionComponent.CollisionOptions.RawValue](collisioncomponent/collisionoptions-swift.struct/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Type Properties
- [static let fullContactInformation: CollisionComponent.CollisionOptions](collisioncomponent/collisionoptions-swift.struct/fullcontactinformation.md)
  Reports full contact information for collision events.
- [static let none: CollisionComponent.CollisionOptions](collisioncomponent/collisionoptions-swift.struct/none.md)
  An option that reports the default collision information with dynamic collision objects.
- [static let `static`: CollisionComponent.CollisionOptions](collisioncomponent/collisionoptions-swift.struct/static.md)
  Omits reporting collisions with static collision objects.
### Default Implementations
- [Equatable Implementations](collisioncomponent/collisionoptions-swift.struct/equatable-implementations.md)
- [OptionSet Implementations](collisioncomponent/collisionoptions-swift.struct/optionset-implementations.md)
- [SetAlgebra Implementations](collisioncomponent/collisionoptions-swift.struct/setalgebra-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/collisioncomponent/collisionoptions-swift.struct)*