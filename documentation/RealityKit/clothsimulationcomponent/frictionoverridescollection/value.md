# ClothSimulationComponent.FrictionOverridesCollection.Value

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

The combined frictions that override the frictions used between a pair of materials.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct Value
```

## Topics

### Creating a friction value
- [init(kineticFriction: Float, staticFriction: Float)](./value/init%28kineticfriction,staticfriction%29.md)
  Creates a friction override value with the given friction coefficients.
### Accessing friction values
- [var staticFriction: Float](./value/staticfriction.md)
  The static friction to use between the material pair.
- [var kineticFriction: Float](./value/kineticfriction.md)
  The kinetic friction to use between the material pair.

## Relationships

### Conforms To
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Identifying overrides
- [ClothSimulationComponent.FrictionOverridesCollection.Key](./key.md)
  The pair of materials whose combined frictions are overridden.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothsimulationcomponent/frictionoverridescollection/value)*