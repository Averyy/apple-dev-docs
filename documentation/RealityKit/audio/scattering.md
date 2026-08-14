# Audio.Scattering

**Framework**: RealityKit  
**Kind**: struct

An object that holds a set of scattering data.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct Scattering
```

#### Overview

The scattering coefficient is a value between zero and one that describes the proportion of incident sound energy that is diffused or redirected by a surface, rather than absorbed.

Create scattering data from an array of ten octave-band coefficients, a dictionary of frequency–coefficient pairs, or a dictionary literal:

```swift
// From an array of ten octave-band coefficients:
let data = Audio.Scattering([0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.10])

// From a dictionary of frequency–coefficient pairs:
let data = Audio.Scattering([500: 0.3, 1000: 0.4, 4000: 0.5])

// From a dictionary literal:
let data: Audio.Scattering = [500: 0.3, 1000: 0.4, 4000: 0.5]
```

## Topics

### Creating a scattering value
- [static func uniform(Float) -> Audio.Scattering](audio/scattering/uniform(_:).md)
  Creates a scattering data set with the coefficient applied uniformly for every frequency.
### Scaling scattering
- [func scaled(by: (Float) -> Float) -> Audio.Scattering](audio/scattering/scaled(by:).md)
  Scale the scattering data by a frequency-dependent scalar value between -1 and 1.
### Initializers
- [init(_:)](audio/scattering/init(_:).md)
  Creates a scattering data set from a sequence of pairs of center frequency and scattering coefficient.
### Type Properties
- [static let `default`: Audio.Scattering](audio/scattering/default.md)
  The default set of scattering data.
### Default Implementations
- [ExpressibleByDictionaryLiteral Implementations](audio/scattering/expressiblebydictionaryliteral-implementations.md)

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [ExpressibleByDictionaryLiteral](../swift/expressiblebydictionaryliteral.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [struct Material](audio/material.md)
  A type that describes the acoustic characteristics of a surface.
- [struct Absorption](audio/absorption.md)
  An object that holds a set of absorption data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audio/scattering)*