# PhotogrammetrySession.Configuration

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

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

- [Creating 3D objects from photographs](../creating-3d-objects-from-photographs.md)

## Overview

A [`PhotogrammetrySession.Configuration`](./configuration-swift.struct.md) instance may be passed in to any of the [`PhotogrammetrySession`](../photogrammetrysession.md) initializers to override its default values.

Use the default values in most instances. In some cases, you may improve the quality of the generated 3D object by specifying different values. If, for example, your source images have few landmarks or poor contrast, you might set [`featureSensitivity`](./configuration-swift.struct/featuresensitivity-swift.property.md) to [`PhotogrammetrySession.Configuration.FeatureSensitivity.high`](./configuration-swift.struct/featuresensitivity-swift.enum/high.md) to compensate for it.

## Topics

### Creating a configuration
- [init()](./configuration-swift.struct/init%28%29.md)
  Creates a configuration using default values.
### Configuring object masking
- [var isObjectMaskingEnabled: Bool](./configuration-swift.struct/isobjectmaskingenabled.md)
  A Boolean value that indicates whether the session uses object masks.
### Configuring sample ordering
- [var sampleOrdering: PhotogrammetrySession.Configuration.SampleOrdering](./configuration-swift.struct/sampleordering-swift.property.md)
  The order of the image samples.
- [PhotogrammetrySession.Configuration.SampleOrdering](./configuration-swift.struct/sampleordering-swift.enum.md)
  The ordering of samples.
### Configuring feature sensitivity
- [var featureSensitivity: PhotogrammetrySession.Configuration.FeatureSensitivity](./configuration-swift.struct/featuresensitivity-swift.property.md)
  The precision of landmark detection.
- [PhotogrammetrySession.Configuration.FeatureSensitivity](./configuration-swift.struct/featuresensitivity-swift.enum.md)
  The sensitivity to sample landmarks.
### Structures
- [PhotogrammetrySession.Configuration.CustomDetailSpecification](./configuration-swift.struct/customdetailspecification-swift.struct.md)
  A structure for specifying various customizable options on the reconstructed model and textures.
### Initializers
- [init(checkpointDirectory: URL)](./configuration-swift.struct/init%28checkpointdirectory%29.md)
### Instance Properties
- [var checkpointDirectory: URL?](./configuration-swift.struct/checkpointdirectory.md)
  The directory that a the photogrammetry session uses for checkpoints during reconstruction.
- [var customDetailSpecification: PhotogrammetrySession.Configuration.CustomDetailSpecification](./configuration-swift.struct/customdetailspecification-swift.property.md)
  Defines custom detail level specifications for a photogrammetry session with custom detail level.
- [var ignoreBoundingBox: Bool](./configuration-swift.struct/ignoreboundingbox.md)
  Ignores any bounding box information embedded in the input images and instead returns all possible geometry that can be automatically estimated using the image set.  The resulting mesh will likely need post-processing. Note: to recover the entire scene geometry as well as ignore the box, `isObjectMaskingEnabled` should also be set to false.
- [var meshPrimitive: PhotogrammetrySession.Configuration.MeshPrimitive](./configuration-swift.struct/meshprimitive-swift.property.md)
  On macOS, this property can be used to change the output geometry mesh primitive for all output geometry in the session, regardless of `Detail` setting. This will also change the mesh primitives in both OBJ and USD outputs. By default, triangle meshes are created.
### Enumerations
- [PhotogrammetrySession.Configuration.MeshPrimitive](./configuration-swift.struct/meshprimitive-swift.enum.md)
  The type of geometric mesh primitives to create in model output

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Configuring the session
- [var configuration: PhotogrammetrySession.Configuration](./configuration-swift.property.md)
  Readonly property  containing the session configuration set in the construction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/photogrammetrysession/configuration-swift.struct)*