# applying(_:)

**Framework**: Spatial  
**Kind**: method

Returns a ray that’s transformed by the specified pose.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
func applying(_ pose: Pose3DFloat) -> Ray3DFloat
```

#### Discussion

- Returns The transformed ray. This function rotates the ray’s direction by the pose’s rotation and offsets the ray’s origin by the pose’s position.

## Parameters

- `pose`: The pose.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/ray3dfloat/applying(_:)-3spgk)*