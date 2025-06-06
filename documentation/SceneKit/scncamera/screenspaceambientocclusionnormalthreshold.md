# screenSpaceAmbientOcclusionNormalThreshold

**Framework**: SceneKit  
**Kind**: property

The magnitude of the blur effect applied to create ambient occlusion shadows.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var screenSpaceAmbientOcclusionNormalThreshold: CGFloat { get set }
```

#### Discussion

Ambient occlusion is an effect that improves material shading by calculating the amounts of ambient light that reach various parts of a surface, creating shadows on parts of a geometry where incoming light is obscured by other parts of the geometry. (You can provide pre-rendered ambient occlusion effects for a material using its [`ambientOcclusion`](scnmaterial/ambientocclusion.md) property.)  (SSAO) provides a real-time approximation of this effect for the entire scene viewed through the camera.

SSAO shadowing includes a blur effect to realistically soften differences in shadow between adjacent pixels, which depends on both the smoothness of scene geometry and this factor. Larger blur factors create a softer, more spread-out blur; smaller factors create coarser shadowing effects.

## See Also

- [var screenSpaceAmbientOcclusionIntensity: CGFloat](scncamera/screenspaceambientocclusionintensity.md)
  The intensity of the screen-space ambient occlusion effect applied in camera rendering.
- [var screenSpaceAmbientOcclusionRadius: CGFloat](scncamera/screenspaceambientocclusionradius.md)
  The distance, in units of scene space, at which ambient occlusion takes effect.
- [var screenSpaceAmbientOcclusionBias: CGFloat](scncamera/screenspaceambientocclusionbias.md)
  An offset for modulating ambient occlusion effects.
- [var screenSpaceAmbientOcclusionDepthThreshold: CGFloat](scncamera/screenspaceambientocclusiondepththreshold.md)
  The maximum depth difference, in units of scene space, at which to apply ambient occlusion effects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncamera/screenspaceambientocclusionnormalthreshold)*