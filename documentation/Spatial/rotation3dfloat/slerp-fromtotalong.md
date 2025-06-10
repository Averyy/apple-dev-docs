# slerp(from:to:t:along:)

**Framework**: Spatial  
**Kind**: method

Returns the spherical linear interpolation along the either the shortest or longest arc between two rotations.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
static func slerp(from: Rotation3DFloat, to: Rotation3DFloat, t: Float, along path: Rotation3D.SlerpPath = .shortest) -> Rotation3DFloat
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/rotation3dfloat/slerp(from:to:t:along:))*