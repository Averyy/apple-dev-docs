# LightmapComponent.SurfaceExtractor

**Framework**: RealityKit  
**Kind**: class

This is a helper for extracting certain surface properties from entities within a lightmapped scene and rendering them out into the atlas defined by the light map.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
class SurfaceExtractor
```

## Topics

### Creating a surface extractor
- [init(lightmapRootEntity: Entity) throws](lightmapcomponent/surfaceextractor/init(lightmaprootentity:).md)
### Extracting surfaces
- [func extractSurfacesForAtlasSlice(mode: LightmapComponent.SurfaceExtractor.ExtractionMode, atlasTextureIndex: Int, textureSliceIndex: Int, cameraOutput: RealityRenderer.CameraOutput, cameraTransform: Transform, cameraFOVDegrees: Float, onComplete: (() -> Void)?) throws](lightmapcomponent/surfaceextractor/extractsurfacesforatlasslice(mode:atlastextureindex:texturesliceindex:cameraoutput:cameratransform:camerafovdegrees:oncomplete:).md)
- [LightmapComponent.SurfaceExtractor.ExtractionMode](lightmapcomponent/surfaceextractor/extractionmode.md)
  Specifies what surface property to extract.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lightmapcomponent/surfaceextractor)*