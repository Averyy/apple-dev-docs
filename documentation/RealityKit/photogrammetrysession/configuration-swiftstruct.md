# PhotogrammetrySession.Configuration

**Framework**: RealityKit  
**Kind**: struct

The configuration parameters for a photogrammetry session.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
struct Configuration
```

## Mentions

- [Creating 3D objects from photographs](creating-3d-objects-from-photographs.md)

#### Overview

A [`PhotogrammetrySession.Configuration`](photogrammetrysession/configuration-swift.struct.md) instance may be passed in to any of the [`PhotogrammetrySession`](photogrammetrysession.md) initializers to override its default values.

Use the default values in most instances. In some cases, you may improve the quality of the generated 3D object by specifying different values. If, for example, your source images have few landmarks or poor contrast, you might set [`featureSensitivity`](photogrammetrysession/configuration-swift.struct/featuresensitivity-swift.property.md) to [`PhotogrammetrySession.Configuration.FeatureSensitivity.high`](photogrammetrysession/configuration-swift.struct/featuresensitivity-swift.enum/high.md) to compensate for it.

## Topics

### Creating a configuration
- [init()](photogrammetrysession/configuration-swift.struct/init.md)
  Creates a configuration using default values.
### Configuring object masking
- [var isObjectMaskingEnabled: Bool](photogrammetrysession/configuration-swift.struct/isobjectmaskingenabled.md)
  A Boolean value that indicates whether the session uses object masks.
### Configuring sample ordering
- [var sampleOrdering: PhotogrammetrySession.Configuration.SampleOrdering](photogrammetrysession/configuration-swift.struct/sampleordering-swift.property.md)
  The order of the image samples.
- [PhotogrammetrySession.Configuration.SampleOrdering](photogrammetrysession/configuration-swift.struct/sampleordering-swift.enum.md)
  The ordering of samples.
### Configuring feature sensitivity
- [var featureSensitivity: PhotogrammetrySession.Configuration.FeatureSensitivity](photogrammetrysession/configuration-swift.struct/featuresensitivity-swift.property.md)
  The precision of landmark detection.
- [PhotogrammetrySession.Configuration.FeatureSensitivity](photogrammetrysession/configuration-swift.struct/featuresensitivity-swift.enum.md)
  The sensitivity to sample landmarks.
### Structures
- [PhotogrammetrySession.Configuration.CustomDetailSpecification](photogrammetrysession/configuration-swift.struct/customdetailspecification-swift.struct.md)
  A structure for specifying various customizable options on the reconstructed model and textures.
### Operators
- [static func == (PhotogrammetrySession.Configuration, PhotogrammetrySession.Configuration) -> Bool](photogrammetrysession/configuration-swift.struct/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Initializers
- [init(checkpointDirectory: URL)](photogrammetrysession/configuration-swift.struct/init(checkpointdirectory:).md)
### Instance Properties
- [var checkpointDirectory: URL?](photogrammetrysession/configuration-swift.struct/checkpointdirectory.md)
  The directory that a the photogrammetry session uses for checkpoints during reconstruction.
- [var customDetailSpecification: PhotogrammetrySession.Configuration.CustomDetailSpecification](photogrammetrysession/configuration-swift.struct/customdetailspecification-swift.property.md)
  Defines custom detail level specifications for a photogrammetry session with custom detail level.
- [var ignoreBoundingBox: Bool](photogrammetrysession/configuration-swift.struct/ignoreboundingbox.md)
  Ignores any bounding box information embedded in the input images and instead returns all possible geometry that can be automatically estimated using the image set.  The resulting mesh will likely need post-processing. Note: to recover the entire scene geometry as well as ignore the box, `isObjectMaskingEnabled` should also be set to false.
- [var meshPrimitive: PhotogrammetrySession.Configuration.MeshPrimitive](photogrammetrysession/configuration-swift.struct/meshprimitive-swift.property.md)
  On macOS, this property can be used to change the output geometry mesh primitive for all output geometry in the session, regardless of `Detail` setting. This will also change the mesh primitives in both OBJ and USD outputs. By default, triangle meshes are created.
### Enumerations
- [PhotogrammetrySession.Configuration.MeshPrimitive](photogrammetrysession/configuration-swift.struct/meshprimitive-swift.enum.md)
  The type of geometric mesh primitives to create in model output
### Default Implementations
- [Equatable Implementations](photogrammetrysession/configuration-swift.struct/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)

## See Also

- [var configuration: PhotogrammetrySession.Configuration](photogrammetrysession/configuration-swift.property.md)
  Readonly property  containing the session configuration set in the construction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/photogrammetrysession/configuration-swift.struct)*