# cascades

**Framework**: RealityKit  
**Kind**: property

Number of shadow cascades to use when rendering shadows for this light.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var cascades: DirectionalLightComponent.Shadow.Cascades { get set }
```

#### Discussion

Cascaded shadow maps can significantly increase the shadow resolution of directional lights and help reduce perspective aliasing, particularly effective in expansive scenes with viewing angles displaying both objects close to the viewer and in the far distance. By default, the light uses one cascade which means a single shadow map texture is mapped to the entire area covered by the directional light. The more cascades are used, the higher the effective resolution of the shadows cast by the light. However, note that using two cascades would take up twice as much texture memory in your app, three cascades three times as much, and so on.

Note that a light with [`DirectionalLightComponent.Shadow.ShadowProjectionType.fixed(zNear:zFar:orthographicScale:)`](directionallightcomponent/shadow/shadowprojectiontype/fixed(znear:zfar:orthographicscale:).md) shadow projection will not participate in cascaded shadow maps.

## See Also

- [DirectionalLightComponent.Shadow.Cascades](directionallightcomponent/shadow/cascades-swift.struct.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/directionallightcomponent/shadow/cascades-swift.property)*