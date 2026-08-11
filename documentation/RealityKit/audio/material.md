# Audio.Material

**Framework**: RealityKit  
**Kind**: struct

A type that describes the acoustic characteristics of a surface.

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

#### Overview

An audio material defines how a surface absorbs and scatters sound energy across frequency bands. Use preset materials for common real-world surfaces, or create custom materials from raw absorption and scattering coefficients.

```swift
// Use a preset material:
let walls: Audio.Material = .concrete

// Create a custom material:
let custom = Audio.Material(
    absorption: .init([0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.10]),
    scattering: .init([0.10, 0.09, 0.08, 0.07, 0.06, 0.05, 0.04, 0.03, 0.02, 0.01])
)

// Modify a preset material:
let thickCarpet: Audio.Material = .carpet.scalingAbsorption { frequency in
    frequency > 1000 ? 0.5 : .zero
}
```

## Topics

### Creating a material
- [init(name: String?, absorption: Audio.Absorption, scattering: Audio.Scattering)](audio/material/init(name:absorption:scattering:).md)
  Creates an audio material from absorption and scattering data.
### Using hard surface materials
- [static let concrete: Audio.Material](audio/material/concrete.md)
  A material that simulates the acoustic properties of concrete.
- [static let brick: Audio.Material](audio/material/brick.md)
  A material that simulates the acoustic properties of brick.
- [static let glass: Audio.Material](audio/material/glass.md)
  A material that simulates the acoustic properties of glass.
- [static let metal: Audio.Material](audio/material/metal.md)
  A material that simulates the acoustic properties of metal.
- [static let tile: Audio.Material](audio/material/tile.md)
  A material that simulates the acoustic properties of tile.
- [static let marble: Audio.Material](audio/material/marble.md)
  A material that simulates the acoustic properties of marble.
- [static let wood: Audio.Material](audio/material/wood.md)
  A material that simulates the acoustic properties of wood.
- [static let parquet: Audio.Material](audio/material/parquet.md)
  A material that simulates the acoustic properties of parquet flooring.
- [static let dryWall: Audio.Material](audio/material/drywall.md)
  A material that simulates the acoustic properties of drywall.
- [static let plaster: Audio.Material](audio/material/plaster.md)
  A material that simulates the acoustic properties of plaster.
### Using soft furnishing materials
- [static let carpet: Audio.Material](audio/material/carpet.md)
  A material that simulates the acoustic properties of carpet.
- [static let curtain: Audio.Material](audio/material/curtain.md)
  A material that simulates the acoustic properties of a curtain.
- [static let mattress: Audio.Material](audio/material/mattress.md)
  A material that simulates the acoustic properties of a mattress.
- [static let seatingUpholstered: Audio.Material](audio/material/seatingupholstered.md)
  A material that simulates the acoustic properties of upholstered seating.
- [static let seatingHard: Audio.Material](audio/material/seatinghard.md)
  A material that simulates the acoustic properties of hard seating.
### Using natural surface materials
- [static let water: Audio.Material](audio/material/water.md)
  A material that simulates the acoustic properties of water.
- [static let ice: Audio.Material](audio/material/ice.md)
  A material that simulates the acoustic properties of ice.
- [static let snow: Audio.Material](audio/material/snow.md)
  A material that simulates the acoustic properties of snow.
- [static let sand: Audio.Material](audio/material/sand.md)
  A material that simulates the acoustic properties of sand.
- [static let soil: Audio.Material](audio/material/soil.md)
  A material that simulates the acoustic properties of soil.
- [static let gravel: Audio.Material](audio/material/gravel.md)
  A material that simulates the acoustic properties of gravel.
- [static let trees: Audio.Material](audio/material/trees.md)
  A material that simulates the acoustic properties of trees.
### Adjusting acoustic properties
- [func scalingAbsorption(by: (Float) -> Float) -> Audio.Material](audio/material/scalingabsorption(by:).md)
  Scale the absorption data by a frequency-dependent scalar value between -1 and 1.
- [func scalingScattering(by: (Float) -> Float) -> Audio.Material](audio/material/scalingscattering(by:).md)
  Scale the scattering data by a frequency-dependent scalar value between -1 and 1.
### Instance Properties
- [var name: String?](audio/material/name.md)
  The name of the audio material.
### Instance Methods
- [func absorption(Audio.Absorption) -> Audio.Material](audio/material/absorption(_:).md)
  Creates a new audio material with the provided absorption data.
- [func scattering(Audio.Scattering) -> Audio.Material](audio/material/scattering(_:).md)
  Creates a new audio material with the provided scattering data.
### Type Properties
- [static let `default`: Audio.Material](audio/material/default.md)
  Default audio material.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct Absorption](audio/absorption.md)
  An object that holds a set of absorption data.
- [struct Scattering](audio/scattering.md)
  An object that holds a set of scattering data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audio/material)*