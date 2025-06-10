# shadowMapSize

**Framework**: SceneKit  
**Kind**: property

The size of the shadow map image that SceneKit renders when creating shadows.

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
var shadowMapSize: CGSize { get set }
```

#### Discussion

SceneKit produces shadows by rendering the silhouettes of scene geometry into a 2D shadow map image and then projecting that image into the rendered scene. A larger shadow map image produces more detailed shadows at a higher cost to rendering performance; a smaller shadow map renders more quickly but results in pixelation at the edges of shadows.

The default value is [`CGSizeZero`](https://developer.apple.com/documentation/CoreGraphics/CGSizeZero), specifying that SceneKit chooses a shadow map size automatically.

## See Also

- [var castsShadow: Bool](scnlight/castsshadow.md)
  A Boolean value that determines whether the light casts shadows.
- [var shadowRadius: CGFloat](scnlight/shadowradius.md)
  A number that specifies the amount of blurring around the edges of shadows cast by the light. Animatable.
- [var shadowColor: Any](scnlight/shadowcolor.md)
  The color of shadows cast by the light. Animatable.
- [var shadowSampleCount: Int](scnlight/shadowsamplecount.md)
  The number of samples from the shadow map that SceneKit uses to render each pixel.
- [var shadowMode: SCNShadowMode](scnlight/shadowmode.md)
  The mode SceneKit uses to render shadows.
- [enum SCNShadowMode](scnshadowmode.md)
  Options for SceneKit’s rendering of shadows cast by a light, used by the [`shadowMode`](scnlight/shadowmode.md) property.
- [var shadowBias: CGFloat](scnlight/shadowbias.md)
  The amount of correction to apply to the shadow to prevent rendering artifacts.
- [var orthographicScale: CGFloat](scnlight/orthographicscale.md)
  The orthographic scale SceneKit uses when rendering the shadow map for a directional light.
- [var zFar: CGFloat](scnlight/zfar.md)
  The maximum distance between the light and a visible surface for casting shadows.
- [var zNear: CGFloat](scnlight/znear.md)
  The minimum distance between the light and a visible surface for casting shadows. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnlight/shadowmapsize)*