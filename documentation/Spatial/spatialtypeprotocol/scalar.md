# Scalar

**Framework**: Spatial  
**Kind**: associatedtype  
**Required**: Yes

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
associatedtype Scalar : Numeric where Self.Scalar == Self.AffineTransform.Scalar, Self.AffineTransform.Scalar == Self.Point.Scalar, Self.Point.Scalar == Self.Pose.Scalar, Self.Pose.Scalar == Self.ProjectiveTransform.Scalar, Self.ProjectiveTransform.Scalar == Self.Rect.Scalar, Self.Rect.Scalar == Self.Rotation.Scalar, Self.Rotation.Scalar == Self.Size.Scalar, Self.Size.Scalar == Self.Vector.Scalar
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/spatialtypeprotocol/scalar)*