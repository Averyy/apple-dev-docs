# applying(_:)

**Framework**: Spatial  
**Kind**: method

Returns a pose that’s transformed by the specified projective transform.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
func applying(_ transform: ProjectiveTransform3D) -> Pose3D
```

#### Discussion

- Returns The transformed pose.

This function applies the transform to the pose.

## Parameters

- `transform`: The projective transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/pose3d/applying(_:))*