# frictionOverrides

**Framework**: RealityKit  
**Kind**: property

A map to manually override friction values between pairs of materials.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var frictionOverrides: ClothSimulationComponent.FrictionOverridesCollection
```

#### Discussion

Each material has its own friction properties. When two materials come into contact and no override exists for that pair, the effective friction is the product of the two materials’ friction values. When an override is present, it replaces that combined value entirely for both static and kinetic friction. This way, it is possible to customize exactly what friction values should be used between a given pair of materials.

## See Also

- [ClothSimulationComponent.FrictionOverridesCollection](clothsimulationcomponent/frictionoverridescollection.md)
  A collection of materials pairs whose combined frictions are overridden.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothsimulationcomponent/frictionoverrides)*