# screenSpaceAmbientOcclusionIntensity

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The intensity of the screen-space ambient occlusion effect applied in camera rendering.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
var screenSpaceAmbientOcclusionIntensity: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat screenSpaceAmbientOcclusionIntensity;
```

## Discussion

Ambient occlusion is an effect that improves material shading by calculating the amounts of ambient light that reach various parts of a surface, creating shadows on parts of a geometry where incoming light is obscured by other parts of the geometry. (You can provide pre-rendered ambient occlusion effects for a material using its [`ambientOcclusion`](../scnmaterial/ambientocclusion.md) property.) *Screen-space ambient occlusion* (SSAO) provides a real-time approximation of this effect for the entire scene viewed through the camera.

The default value of this property is zero, disabling SSAO effects. Increasing the intensity value creates deeper, bolder shadows.

## See Also

### Adding Screen-Space Ambient Occlusion
- [var screenSpaceAmbientOcclusionRadius: CGFloat](./screenspaceambientocclusionradius.md)
  The distance, in units of scene space, at which ambient occlusion takes effect.
- [var screenSpaceAmbientOcclusionBias: CGFloat](./screenspaceambientocclusionbias.md)
  An offset for modulating ambient occlusion effects.
- [var screenSpaceAmbientOcclusionDepthThreshold: CGFloat](./screenspaceambientocclusiondepththreshold.md)
  The maximum depth difference, in units of scene space, at which to apply ambient occlusion effects.
- [var screenSpaceAmbientOcclusionNormalThreshold: CGFloat](./screenspaceambientocclusionnormalthreshold.md)
  The magnitude of the blur effect applied to create ambient occlusion shadows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncamera/screenspaceambientocclusionintensity)*