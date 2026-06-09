# ClothSimulationComponent.FrictionOverridesCollection.Value

**Framework**: RealityKit  
**Kind**: struct

The combined frictions that override the frictions used between a pair of materials.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct Value
```

## Topics

### Creating a friction value
- [init(kineticFriction: Float, staticFriction: Float)](clothsimulationcomponent/frictionoverridescollection/value/init(kineticfriction:staticfriction:).md)
  Creates a friction override value with the given friction coefficients.
### Accessing friction values
- [var staticFriction: Float](clothsimulationcomponent/frictionoverridescollection/value/staticfriction.md)
  The static friction to use between the material pair.
- [var kineticFriction: Float](clothsimulationcomponent/frictionoverridescollection/value/kineticfriction.md)
  The kinetic friction to use between the material pair.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [ClothSimulationComponent.FrictionOverridesCollection.Key](clothsimulationcomponent/frictionoverridescollection/key.md)
  The pair of materials whose combined frictions are overridden.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothsimulationcomponent/frictionoverridescollection/value)*