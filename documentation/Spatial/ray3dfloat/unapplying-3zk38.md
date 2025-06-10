# unapplying(_:)

**Framework**: Spatial  
**Kind**: method

Returns a ray that’s transformed by the inverse of the specified scaled pose.

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
func unapplying(_ scaledPose: ScaledPose3DFloat) -> Ray3DFloat
```

#### Discussion

- Returns The transformed ray. This function rotates the ray’s direction by the pose’s rotation and offsets the ray’s origin by the pose’s position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/ray3dfloat/unapplying(_:)-3zk38)*