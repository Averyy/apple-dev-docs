# Reverb

**Framework**: RealityKit  
**Kind**: struct

The reverberation RealityKit applies to spatial audio sources.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
struct Reverb
```

#### Overview

You can configure the reverb for spatial audio sources in your RealityKit content with the [`ReverbComponent`](reverbcomponent.md).

```swift
let cinema = Entity()
let reverb: Reverb = .preset(.mediumRoomDry)
cinema.components.set(ReverbComponent(reverb: reverb))
```

## Topics

### Structures
- [Reverb.Preset](reverb/preset.md)
  Reverbs defined by a preset environment.
### Type Properties
- [static let anechoic: Reverb](reverb/anechoic.md)
  A reverb instance that applies no reverberation to spatial audio sources.
### Type Methods
- [static func preset(Reverb.Preset) -> Reverb](reverb/preset(_:).md)
  Returns a reverb instance that you can set on a reverb component.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Reverb.Preset](reverb/preset.md)
  Reverbs defined by a preset environment.
- [struct ReverbComponent](reverbcomponent.md)
  A component that defines the reverberation of spatial audio sources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/reverb)*