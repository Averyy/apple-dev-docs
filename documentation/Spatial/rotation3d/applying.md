# applying(_:)

**Framework**: Spatial  
**Kind**: method

Returns a rotation that’s transformed by the specified projective transform.

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
func applying(_ transform: ProjectiveTransform3D) -> Rotation3D
```

#### Discussion

- Returns The transformed rotation. In the case where Spatial is unable to successfully apply the transform, the function returns `.identity`.

This function applies the transform to the rotation.

## Parameters

- `transform`: The projective transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/rotation3d/applying(_:))*