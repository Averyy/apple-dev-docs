# Audio.Material

**Framework**: RealityKit  
**Kind**: struct

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct Material
```

## Topics

### Creating a material
- [init(name: String?, absorption: Audio.Absorption, scattering: Audio.Scattering)](audio/material/init(name:absorption:scattering:).md)
### Using hard surface materials
- [static let concrete: Audio.Material](audio/material/concrete.md)
- [static let brick: Audio.Material](audio/material/brick.md)
- [static let glass: Audio.Material](audio/material/glass.md)
- [static let metal: Audio.Material](audio/material/metal.md)
- [static let tile: Audio.Material](audio/material/tile.md)
- [static let marble: Audio.Material](audio/material/marble.md)
- [static let wood: Audio.Material](audio/material/wood.md)
- [static let parquet: Audio.Material](audio/material/parquet.md)
- [static let dryWall: Audio.Material](audio/material/drywall.md)
- [static let plaster: Audio.Material](audio/material/plaster.md)
### Using soft furnishing materials
- [static let carpet: Audio.Material](audio/material/carpet.md)
- [static let curtain: Audio.Material](audio/material/curtain.md)
- [static let mattress: Audio.Material](audio/material/mattress.md)
- [static let seatingUpholstered: Audio.Material](audio/material/seatingupholstered.md)
- [static let seatingHard: Audio.Material](audio/material/seatinghard.md)
### Using natural surface materials
- [static let water: Audio.Material](audio/material/water.md)
- [static let ice: Audio.Material](audio/material/ice.md)
- [static let snow: Audio.Material](audio/material/snow.md)
- [static let sand: Audio.Material](audio/material/sand.md)
- [static let soil: Audio.Material](audio/material/soil.md)
- [static let gravel: Audio.Material](audio/material/gravel.md)
- [static let trees: Audio.Material](audio/material/trees.md)
### Adjusting acoustic properties
- [func scalingAbsorption(by: (Float) -> Float) -> Audio.Material](audio/material/scalingabsorption(by:).md)
- [func scalingScattering(by: (Float) -> Float) -> Audio.Material](audio/material/scalingscattering(by:).md)
### Instance Properties
- [var name: String?](audio/material/name.md)
### Instance Methods
- [func absorption(Audio.Absorption) -> Audio.Material](audio/material/absorption(_:).md)
  Creates a new audio material with the provided absorption data.
- [func scattering(Audio.Scattering) -> Audio.Material](audio/material/scattering(_:).md)
  Creates a new audio material with the provided scattering data.
### Type Properties
- [static let `default`: Audio.Material](audio/material/default.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct Absorption](audio/absorption.md)
- [struct Scattering](audio/scattering.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audio/material)*