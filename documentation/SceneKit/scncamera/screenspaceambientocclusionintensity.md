# screenSpaceAmbientOcclusionIntensity

**Framework**: SceneKit  
**Kind**: property

The intensity of the screen-space ambient occlusion effect applied in camera rendering.

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
var screenSpaceAmbientOcclusionIntensity: CGFloat { get set }
```

#### Discussion

Ambient occlusion is an effect that improves material shading by calculating the amounts of ambient light that reach various parts of a surface, creating shadows on parts of a geometry where incoming light is obscured by other parts of the geometry. (You can provide pre-rendered ambient occlusion effects for a material using its [`ambientOcclusion`](scnmaterial/ambientocclusion.md) property.)  (SSAO) provides a real-time approximation of this effect for the entire scene viewed through the camera.

The default value of this property is zero, disabling SSAO effects. Increasing the intensity value creates deeper, bolder shadows.

## See Also

- [var screenSpaceAmbientOcclusionRadius: CGFloat](scncamera/screenspaceambientocclusionradius.md)
  The distance, in units of scene space, at which ambient occlusion takes effect.
- [var screenSpaceAmbientOcclusionBias: CGFloat](scncamera/screenspaceambientocclusionbias.md)
  An offset for modulating ambient occlusion effects.
- [var screenSpaceAmbientOcclusionDepthThreshold: CGFloat](scncamera/screenspaceambientocclusiondepththreshold.md)
  The maximum depth difference, in units of scene space, at which to apply ambient occlusion effects.
- [var screenSpaceAmbientOcclusionNormalThreshold: CGFloat](scncamera/screenspaceambientocclusionnormalthreshold.md)
  The magnitude of the blur effect applied to create ambient occlusion shadows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncamera/screenspaceambientocclusionintensity)*