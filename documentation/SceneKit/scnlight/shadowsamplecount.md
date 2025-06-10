# shadowSampleCount

**Framework**: SceneKit  
**Kind**: property

The number of samples from the shadow map that SceneKit uses to render each pixel.

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
var shadowSampleCount: Int { get set }
```

#### Discussion

SceneKit produces soft-edged shadows by rendering the silhouettes of scene geometry into a 2D shadow map and then using several weighted samples from the shadow map to determine the strength of the shadow at each pixel in the rendered scene. This property controls the number of samples from the shadow map used to render each pixel. Higher numbers result in smoother edges; lower numbers increase rendering performance.

The default value is `16` in macOS and `1` on iOS.

## See Also

- [var castsShadow: Bool](scnlight/castsshadow.md)
  A Boolean value that determines whether the light casts shadows.
- [var shadowRadius: CGFloat](scnlight/shadowradius.md)
  A number that specifies the amount of blurring around the edges of shadows cast by the light. Animatable.
- [var shadowColor: Any](scnlight/shadowcolor.md)
  The color of shadows cast by the light. Animatable.
- [var shadowMapSize: CGSize](scnlight/shadowmapsize.md)
  The size of the shadow map image that SceneKit renders when creating shadows.
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

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnlight/shadowsamplecount)*