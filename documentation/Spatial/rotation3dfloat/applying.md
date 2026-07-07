# applying(_:)

**Framework**: Spatial  
**Kind**: method

Returns a rotation that’s transformed by the specified projective transform.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
func applying(_ transform: ProjectiveTransform3DFloat) -> Rotation3DFloat
```

#### Discussion

- Returns The transformed rotation. In the case where Spatial is unable to successfully apply the transform, the function returns `.identity`.

This function applies the transform to the rotation.

## Parameters

- `transform`: The projective transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/rotation3dfloat/applying(_:))*