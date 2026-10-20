# LightmapComponent.SurfaceExtractor

**Framework**: RealityKit  
**Kind**: class  
**Role**: Class

This is a helper for extracting certain surface properties from entities within a lightmapped scene and rendering them out into the atlas defined by the light map.

**Availability**:
- macOS 27.0+

## Declaration

```swift
@MainActor
class SurfaceExtractor
```

## Topics

### Creating a surface extractor
- [init(lightmapRootEntity: Entity) throws](./surfaceextractor/init%28lightmaprootentity%29.md)
### Extracting surfaces
- [func extractSurfacesForAtlasSlice(mode: LightmapComponent.SurfaceExtractor.ExtractionMode, atlasTextureIndex: Int, textureSliceIndex: Int, cameraOutput: RealityRenderer.CameraOutput, cameraTransform: Transform, cameraFOVDegrees: Float, onComplete: (() -> Void)?) throws](./surfaceextractor/extractsurfacesforatlasslice%28mode,atlastextureindex,texturesliceindex,cameraoutput,cameratransform,camerafovdegrees,oncomplete%29.md)
- [LightmapComponent.SurfaceExtractor.ExtractionMode](./surfaceextractor/extractionmode.md)
  Specifies what surface property to extract.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lightmapcomponent/surfaceextractor)*