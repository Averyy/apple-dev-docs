# LightmapComponent.SurfaceExtractor.ExtractionMode

**Framework**: RealityKit  
**Kind**: enum

Specifies what surface property to extract.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
enum ExtractionMode
```

## Topics

### Choosing the extraction mode
- [LightmapComponent.SurfaceExtractor.ExtractionMode.finalShadedColor](lightmapcomponent/surfaceextractor/extractionmode/finalshadedcolor.md)
  This will extract the final shaded color as it would be normally rendered, with all the effects from lights, shadows, etc. View-dependent effects like specular highlights will be consistent with the camera transform provided to `extractSurfacesForAtlasSlice`.
- [LightmapComponent.SurfaceExtractor.ExtractionMode.baseColor](lightmapcomponent/surfaceextractor/extractionmode/basecolor.md)

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)

## See Also

- [func extractSurfacesForAtlasSlice(mode: LightmapComponent.SurfaceExtractor.ExtractionMode, atlasTextureIndex: Int, textureSliceIndex: Int, cameraOutput: RealityRenderer.CameraOutput, cameraTransform: Transform, cameraFOVDegrees: Float, onComplete: (() -> Void)?) throws](lightmapcomponent/surfaceextractor/extractsurfacesforatlasslice(mode:atlastextureindex:texturesliceindex:cameraoutput:cameratransform:camerafovdegrees:oncomplete:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lightmapcomponent/surfaceextractor/extractionmode)*