# applying(_:)

**Framework**: Spatial  
**Kind**: method

Returns a pose that’s transformed by the specified projective transform.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

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