# extractSurfacesForAtlasSlice(mode:atlasTextureIndex:textureSliceIndex:cameraOutput:cameraTransform:cameraFOVDegrees:onComplete:)

**Framework**: RealityKit  
**Kind**: method

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
func extractSurfacesForAtlasSlice(mode: LightmapComponent.SurfaceExtractor.ExtractionMode, atlasTextureIndex: Int, textureSliceIndex: Int, cameraOutput: RealityRenderer.CameraOutput, cameraTransform: Transform = .init(), cameraFOVDegrees: Float = 90, onComplete: (@Sendable () -> Void)? = nil) throws
```

## See Also

- [LightmapComponent.SurfaceExtractor.ExtractionMode](lightmapcomponent/surfaceextractor/extractionmode.md)
  Specifies what surface property to extract.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lightmapcomponent/surfaceextractor/extractsurfacesforatlasslice(mode:atlastextureindex:texturesliceindex:cameraoutput:cameratransform:camerafovdegrees:oncomplete:))*