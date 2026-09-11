# scattering(_:)

**Framework**: RealityKit  
**Kind**: method

Creates a new audio material with the provided scattering data.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func scattering(_ data: Audio.Scattering) -> Audio.Material
```

#### Discussion

Example usage:

```None
let material: Audio.Material = .wood.scattering([500: 0.3, 1000: 0.4, 4000: 0.5])
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audio/material/scattering(_:))*