# scattering(_:)

**Framework**: RealityKit  
**Kind**: method

Creates a new audio material with the provided scattering data.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

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