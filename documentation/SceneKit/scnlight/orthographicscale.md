# orthographicScale

**Framework**: SceneKit  
**Kind**: property

The orthographic scale SceneKit uses when rendering the shadow map for a directional light.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var orthographicScale: CGFloat { get set }
```

#### Discussion

SceneKit draws a shadow map image by rendering the scene from the point of view of the node containing the light. Directional lights ignore the [`position`](scnnode/position.md) property of the node containing them because their light has a constant direction. Therefore, rendering a shadow map for a directional light requires an orthographic projection. Like the [`orthographicScale`](scncamera/orthographicscale.md) property of a camera object, this property specifies the extent of the scene “visible to” the light when rendering the shadow map.

This property applies only if the light’s [`type`](scnlight/type.md) property is [`directional`](scnlight/lighttype/directional.md).

## See Also

- [var castsShadow: Bool](scnlight/castsshadow.md)
  A Boolean value that determines whether the light casts shadows.
- [var shadowRadius: CGFloat](scnlight/shadowradius.md)
  A number that specifies the amount of blurring around the edges of shadows cast by the light. Animatable.
- [var shadowColor: Any](scnlight/shadowcolor.md)
  The color of shadows cast by the light. Animatable.
- [var shadowMapSize: CGSize](scnlight/shadowmapsize.md)
  The size of the shadow map image that SceneKit renders when creating shadows.
- [var shadowSampleCount: Int](scnlight/shadowsamplecount.md)
  The number of samples from the shadow map that SceneKit uses to render each pixel.
- [var shadowMode: SCNShadowMode](scnlight/shadowmode.md)
  The mode SceneKit uses to render shadows.
- [enum SCNShadowMode](scnshadowmode.md)
  Options for SceneKit’s rendering of shadows cast by a light, used by the [`shadowMode`](scnlight/shadowmode.md) property.
- [var shadowBias: CGFloat](scnlight/shadowbias.md)
  The amount of correction to apply to the shadow to prevent rendering artifacts.
- [var zFar: CGFloat](scnlight/zfar.md)
  The maximum distance between the light and a visible surface for casting shadows.
- [var zNear: CGFloat](scnlight/znear.md)
  The minimum distance between the light and a visible surface for casting shadows. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnlight/orthographicscale)*