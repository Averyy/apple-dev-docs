# Reverb

**Framework**: RealityKit  
**Kind**: struct

The reverberation RealityKit applies to spatial audio sources.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
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
cinema.components.set(ReverbComponent(reverb: reverb)
```

## Topics

### Structures
- [Reverb.Preset](reverb/preset.md)
  Reverbs defined by a preset environment.
### Operators
- [static func == (Reverb, Reverb) -> Bool](reverb/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](reverb/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](reverb/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Properties
- [static let anechoic: Reverb](reverb/anechoic.md)
  A reverb instance that applies no reverberation to spatial audio sources.
### Type Methods
- [static func preset(Reverb.Preset) -> Reverb](reverb/preset(_:).md)
  Returns a reverb instance that you can set on a reverb component.
### Default Implementations
- [Equatable Implementations](reverb/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Reverb.Preset](reverb/preset.md)
  Reverbs defined by a preset environment.
- [struct ReverbComponent](reverbcomponent.md)
  A component that defines the reverberation of spatial audio sources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/reverb)*