# LightmapComponent.SurfaceExtractor.ExtractionMode

**Framework**: RealityKit  
**Kind**: enum  
**Role**: Enumeration

Specifies what surface property to extract.

**Availability**:
- macOS 27.0+

## Declaration

```swift
enum ExtractionMode
```

## Topics

### Choosing the extraction mode
- [LightmapComponent.SurfaceExtractor.ExtractionMode.finalShadedColor](./extractionmode/finalshadedcolor.md)
  This will extract the final shaded color as it would be normally rendered, with all the effects from lights, shadows, etc. View-dependent effects like specular highlights will be consistent with the camera transform provided to `extractSurfacesForAtlasSlice`.
- [LightmapComponent.SurfaceExtractor.ExtractionMode.baseColor](./extractionmode/basecolor.md)

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)

## See Also

### Extracting surfaces
- [func extractSurfacesForAtlasSlice(mode: LightmapComponent.SurfaceExtractor.ExtractionMode, atlasTextureIndex: Int, textureSliceIndex: Int, cameraOutput: RealityRenderer.CameraOutput, cameraTransform: Transform, cameraFOVDegrees: Float, onComplete: (() -> Void)?) throws](./extractsurfacesforatlasslice%28mode,atlastextureindex,texturesliceindex,cameraoutput,cameratransform,camerafovdegrees,oncomplete%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lightmapcomponent/surfaceextractor/extractionmode)*