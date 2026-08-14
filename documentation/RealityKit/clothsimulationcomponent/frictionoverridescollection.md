# ClothSimulationComponent.FrictionOverridesCollection

**Framework**: RealityKit  
**Kind**: struct

A collection of materials pairs whose combined frictions are overridden.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct FrictionOverridesCollection
```

## Topics

### Identifying overrides
- [ClothSimulationComponent.FrictionOverridesCollection.Key](clothsimulationcomponent/frictionoverridescollection/key.md)
  The pair of materials whose combined frictions are overridden.
- [ClothSimulationComponent.FrictionOverridesCollection.Value](clothsimulationcomponent/frictionoverridescollection/value.md)
  The combined frictions that override the frictions used between a pair of materials.
### Removing overrides
- [func removeOverride(forKey: ClothSimulationComponent.FrictionOverridesCollection.Key)](clothsimulationcomponent/frictionoverridescollection/removeoverride(forkey:).md)
### Subscripts
- [subscript(ClothSimulationComponent.FrictionOverridesCollection.Key) -> ClothSimulationComponent.FrictionOverridesCollection.Value?](clothsimulationcomponent/frictionoverridescollection/subscript(_:).md)
  Accesses the friction override for the given material pair, returning `nil` if no override exists.

## Relationships

### Conforms To
- [Collection](../swift/collection.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [Sequence](../swift/sequence.md)

## See Also

- [var frictionOverrides: ClothSimulationComponent.FrictionOverridesCollection](clothsimulationcomponent/frictionoverrides.md)
  A map to manually override friction values between pairs of materials.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothsimulationcomponent/frictionoverridescollection)*