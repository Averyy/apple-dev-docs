# screenSpaceAmbientOcclusionRadius

**Framework**: SceneKit  
**Kind**: property

The distance, in units of scene space, at which ambient occlusion takes effect.

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
var screenSpaceAmbientOcclusionRadius: CGFloat { get set }
```

#### Discussion

Ambient occlusion is an effect that improves material shading by calculating the amounts of ambient light that reach various parts of a surface, creating shadows on parts of a geometry where incoming light is obscured by other parts of the geometry. (You can provide pre-rendered ambient occlusion effects for a material using its [`ambientOcclusion`](scnmaterial/ambientocclusion.md) property.)  (SSAO) provides a real-time approximation of this effect for the entire scene viewed through the camera.

SSAO effects work by storing relevant scene geometry information for each pixel, and using that information to produce per-pixel shading effects. This [`screenSpaceAmbientOcclusionRadius`](scncamera/screenspaceambientocclusionradius.md) property determines the area in scene space to consider around each pixel for determining the amount of incoming ambient light blocked by surrounding geometry (and thus the amount of shadow effect to apply). The default value is 5; smaller values cause SSAO effects to apply only to finer geometry details, while larger values affect coarser details.

## See Also

- [var screenSpaceAmbientOcclusionIntensity: CGFloat](scncamera/screenspaceambientocclusionintensity.md)
  The intensity of the screen-space ambient occlusion effect applied in camera rendering.
- [var screenSpaceAmbientOcclusionBias: CGFloat](scncamera/screenspaceambientocclusionbias.md)
  An offset for modulating ambient occlusion effects.
- [var screenSpaceAmbientOcclusionDepthThreshold: CGFloat](scncamera/screenspaceambientocclusiondepththreshold.md)
  The maximum depth difference, in units of scene space, at which to apply ambient occlusion effects.
- [var screenSpaceAmbientOcclusionNormalThreshold: CGFloat](scncamera/screenspaceambientocclusionnormalthreshold.md)
  The magnitude of the blur effect applied to create ambient occlusion shadows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncamera/screenspaceambientocclusionradius)*