# unapplying(_:)

**Framework**: Spatial  
**Kind**: method

Returns the primitive that results from applying a scaled pose to the primitive.

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
func unapplying(_ scaledPose: ScaledPose3DFloat) -> Rect3DFloat
```

#### Discussion

- Returns The transformed primitive.

> **Note**: The pose’s rotation angle must be zero, otherwise this function returns `self`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/rect3dfloat/unapplying(_:)-4dm1d)*