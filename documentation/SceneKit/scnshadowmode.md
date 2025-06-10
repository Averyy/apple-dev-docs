# SCNShadowMode

**Framework**: SceneKit  
**Kind**: enum

Options for SceneKit’s rendering of shadows cast by a light, used by the [`shadowMode`](scnlight/shadowmode.md) property.

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
enum SCNShadowMode
```

#### Overview

Each shadow mode may have a positive or negative effect on rendering performance, depending on the contents of the scene. Test your app to determine which shadow mode provides the best balance between performance and quality for the scenes you want to render.

## Topics

### Constants
- [SCNShadowMode.forward](scnshadowmode/forward.md)
  SceneKit renders shadows during lighting computations.
- [SCNShadowMode.deferred](scnshadowmode/deferred.md)
  SceneKit renders shadows in a postprocessing pass.
- [SCNShadowMode.modulated](scnshadowmode/modulated.md)
  SceneKit renders shadows by projecting the light’s [`gobo`](scnlight/gobo.md) image. The light does not illuminate the scene.
### Initializers
- [init?(rawValue: Int)](scnshadowmode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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
- [var shadowBias: CGFloat](scnlight/shadowbias.md)
  The amount of correction to apply to the shadow to prevent rendering artifacts.
- [var orthographicScale: CGFloat](scnlight/orthographicscale.md)
  The orthographic scale SceneKit uses when rendering the shadow map for a directional light.
- [var zFar: CGFloat](scnlight/zfar.md)
  The maximum distance between the light and a visible surface for casting shadows.
- [var zNear: CGFloat](scnlight/znear.md)
  The minimum distance between the light and a visible surface for casting shadows. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnshadowmode)*