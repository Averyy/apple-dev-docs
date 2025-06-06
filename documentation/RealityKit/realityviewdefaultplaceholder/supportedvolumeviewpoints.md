# supportedVolumeViewpoints(_:)

**Framework**: RealityKit  
**Kind**: method

Specifies which viewpoints are supported for the window bar and ornaments in a volume.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
nonisolated
func supportedVolumeViewpoints(_ viewpoints: SquareAzimuth.Set) -> some View
```

#### Discussion

This defaults to all viewpoints and determines which viewpoints the window bar and ornaments will ‘follow’ the user to as they move around the volume.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityviewdefaultplaceholder/supportedvolumeviewpoints(_:))*