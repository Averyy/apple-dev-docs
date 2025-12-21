# init()

**Framework**: RealityKit  
**Kind**: init

Creates a physics body component with default settings.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
init()
```

#### Discussion

For the default settings used in a new physics body component, see the discussions of the component’s individual properties.

## See Also

- [init(massProperties: PhysicsMassProperties, material: PhysicsMaterialResource?, mode: PhysicsBodyMode)](physicsbodycomponent/init(massproperties:material:mode:).md)
  Creates a physics body component with the given mass properties, material, and mode.
- [init(shapes: [ShapeResource], density: Float, material: PhysicsMaterialResource?, mode: PhysicsBodyMode)](physicsbodycomponent/init(shapes:density:material:mode:).md)
  Creates a physics body component deriving mass properties from shape and density.
- [init(shapes: [ShapeResource], mass: Float, material: PhysicsMaterialResource?, mode: PhysicsBodyMode)](physicsbodycomponent/init(shapes:mass:material:mode:).md)
  Creates a physics body component deriving mass properties from shape and mass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicsbodycomponent/init())*