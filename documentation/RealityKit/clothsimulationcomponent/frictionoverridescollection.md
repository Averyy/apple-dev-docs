# ClothSimulationComponent.FrictionOverridesCollection

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

A collection of materials pairs whose combined frictions are overridden.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct FrictionOverridesCollection
```

## Topics

### Identifying overrides
- [ClothSimulationComponent.FrictionOverridesCollection.Key](./frictionoverridescollection/key.md)
  The pair of materials whose combined frictions are overridden.
- [ClothSimulationComponent.FrictionOverridesCollection.Value](./frictionoverridescollection/value.md)
  The combined frictions that override the frictions used between a pair of materials.
### Removing overrides
- [func removeOverride(forKey: ClothSimulationComponent.FrictionOverridesCollection.Key)](./frictionoverridescollection/removeoverride%28forkey%29.md)
### Subscripts
- [subscript(ClothSimulationComponent.FrictionOverridesCollection.Key) -> ClothSimulationComponent.FrictionOverridesCollection.Value?](./frictionoverridescollection/subscript%28_%29.md)
  Accesses the friction override for the given material pair, returning `nil` if no override exists.

## Relationships

### Conforms To
- [Collection](../../Swift/collection.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [Sequence](../../Swift/sequence.md)

## See Also

### Overriding friction
- [var frictionOverrides: ClothSimulationComponent.FrictionOverridesCollection](./frictionoverrides.md)
  A map to manually override friction values between pairs of materials.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothsimulationcomponent/frictionoverridescollection)*