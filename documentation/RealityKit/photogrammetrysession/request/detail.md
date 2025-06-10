# PhotogrammetrySession.Request.Detail

**Framework**: RealityKit  
**Kind**: enum

Supported levels of detail for a request.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
enum Detail
```

#### Overview

On iOS, only one detail level – `.reduced` – is currently supported.  This level is optimized for generation and viewing entirely on mobile devices.

On macOS, RealityKit object creation can generate models at different levels of detail. Higher levels of detail may take longer to create, require more memory and processing power to generate, and create objects with more complex geometry and texture requirements.

##### Set a Level of Complexity

Each detail level corresponds to an object of a specific size and complexity. Here’s the expected final size of the generated object from each detail level.

| Detail Level | Triangles | Estimated File Size |
| --- | --- | --- |
| `.preview` | <25k | ≈5MB |
| `.reduced` | <50k | ≈10MB |
| `.medium` | <100k | ≈30MB |
| `.full` | <250k | ≈100MB |
| `.raw` | <30M | Varies |
| `.custom` | Varies | Varies |

##### Create Texture Maps

Each detail level produces a 3D object with texture maps. The higher the complexity level, the larger the generated texture maps, and the more memory the system requires to display those objects in an AR scene.

RealityKit creates five texture maps at the `.full` detail level: a single diffuse map, normal map, ambient occlusion map, roughness map, and displacement map. For `.preview`, `.reduced`, and `.medium`  detail levels, it produces just the single diffuse, normal and ambient occlusion maps.

When producing a model at the `.raw` detail level, only diffuse texture maps are created, but RealityKit may create up to 16 diffuse maps, each covering different parts of the model. Raw models are produced at the highest resolution possible from the source images, so they don’t benefit from having the other types of texture maps, which are used to supplement a low-resolution model with data from a higher-resolution version of the same model.

Raw models aren’t suitable for use in an AR scene and you should only use this setting if you plan to export the model to a 3D software package.

Custom detail level can be used to specify several parameters of the output mesh and textures to provide more control over the produced assets than the preset levels.

Here are the texture map sizes generated for each detail level and the amount of texture memory the uncompressed textures use at runtime.

| Detail Level | Texture Size | Texture Memory Required |
| --- | --- | --- |
| `.preview` | 1024 x 1024 | 10.666667 MB |
| `.reduced` | 2048 x 2048 | 42.666667 MB |
| `.medium` | 4096 x 4096 | 170.666667 MB |
| `.full` | 8192 x 8192 | 853.33333 MB |
| `.raw` | 8192 x 8192 (multiple) | Varies |
| `.custom` | Varies | Varies |

## Topics

### Specifying a level of detail
- [PhotogrammetrySession.Request.Detail.preview](photogrammetrysession/request/detail/preview.md)
  A fast, low-quality object for previewing the final result.
- [PhotogrammetrySession.Request.Detail.reduced](photogrammetrysession/request/detail/reduced.md)
  A mobile-quality object with low resource requirements.
- [PhotogrammetrySession.Request.Detail.medium](photogrammetrysession/request/detail/medium.md)
  A medium-quality object with moderate resource requirements.
- [PhotogrammetrySession.Request.Detail.full](photogrammetrysession/request/detail/full.md)
  A high-quality object with significant resource requirements.
- [PhotogrammetrySession.Request.Detail.raw](photogrammetrysession/request/detail/raw.md)
  The raw-created object at the highest possible resolution.
### Enumeration Cases
- [PhotogrammetrySession.Request.Detail.custom](photogrammetrysession/request/detail/custom.md)
  A custom quality for the model, with specifics defined by the photogrammetry session.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [case modelFile(url: URL, detail: PhotogrammetrySession.Request.Detail, geometry: PhotogrammetrySession.Request.Geometry?)](photogrammetrysession/request/modelfile(url:detail:geometry:).md)
  An object-creation request saved to a USDZ file or a folder (for OBJ output).
- [case modelEntity(detail: PhotogrammetrySession.Request.Detail, geometry: PhotogrammetrySession.Request.Geometry?)](photogrammetrysession/request/modelentity(detail:geometry:).md)
  An object-creation request stored in-memory for immediate display.
- [PhotogrammetrySession.Request.bounds](photogrammetrysession/request/bounds.md)
  An object-creation request that returns a box the same size as the created model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/photogrammetrysession/request/detail)*