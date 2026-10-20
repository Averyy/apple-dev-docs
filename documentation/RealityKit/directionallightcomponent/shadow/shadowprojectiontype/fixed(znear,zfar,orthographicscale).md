# DirectionalLightComponent.Shadow.ShadowProjectionType.fixed(zNear:zFar:orthographicScale:)

**Framework**: RealityKit  
**Kind**: case  
**Role**: Case

Shadow projection is manually set up with near plane, far plane, and orthographicScale for width and height

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
case fixed(zNear: Float = 0.01, zFar: Float = 10, orthographicScale: Float = 1)
```

## See Also

### Shadow projection types
- [DirectionalLightComponent.Shadow.ShadowProjectionType.automatic(maximumDistance:)](./automatic%28maximumdistance%29.md)
  Shadow projection is automatically fit with the camera frustum, range is within maximumDistance from camera


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/directionallightcomponent/shadow/shadowprojectiontype/fixed(znear:zfar:orthographicscale:))*