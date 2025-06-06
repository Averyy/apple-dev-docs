# DirectionalLightComponent.Shadow.ShadowProjectionType

**Framework**: RealityKit  
**Kind**: enum

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
enum ShadowProjectionType
```

## Topics

### Shadow projection types
- [DirectionalLightComponent.Shadow.ShadowProjectionType.automatic(maximumDistance:)](directionallightcomponent/shadow/shadowprojectiontype/automatic(maximumdistance:).md)
  Shadow projection is automatically fit with the camera frustum, range is within maximumDistance from camera
- [DirectionalLightComponent.Shadow.ShadowProjectionType.fixed(zNear:zFar:orthographicScale:)](directionallightcomponent/shadow/shadowprojectiontype/fixed(znear:zfar:orthographicscale:).md)
  Shadow projection is manually set up with near plane, far plane, and orthographicScale for width and height
### Comparing shadow projection types
- [static func == (DirectionalLightComponent.Shadow.ShadowProjectionType, DirectionalLightComponent.Shadow.ShadowProjectionType) -> Bool](directionallightcomponent/shadow/shadowprojectiontype/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Default Implementations
- [Equatable Implementations](directionallightcomponent/shadow/shadowprojectiontype/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)

## See Also

- [struct DirectionalLightComponent](directionallightcomponent.md)
  A component that defines a directional light source.
- [DirectionalLightComponent.Shadow](directionallightcomponent/shadow.md)
  A directional light component that adds shadows to entities that it illuminates
- [DirectionalLightComponent.Shadow.ShadowMapCullMode](directionallightcomponent/shadow/shadowmapcullmode.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/directionallightcomponent/shadow/shadowprojectiontype)*