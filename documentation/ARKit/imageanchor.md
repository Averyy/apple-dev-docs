# ImageAnchor

**Framework**: ARKit  
**Kind**: struct

A 2D image’s position in a person’s surroundings.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
struct ImageAnchor
```

## Topics

### Getting image information
- [var originFromAnchorTransform: simd_float4x4](imageanchor/originfromanchortransform.md)
  The location and orientation of the image in world space.
- [var referenceImage: ReferenceImage](imageanchor/referenceimage.md)
  The reference image that this image anchor tracks.
- [var estimatedScaleFactor: Float](imageanchor/estimatedscalefactor.md)
  The estimated scale factor between the tracked image’s physical size and the reference image’s size.
- [var isTracked: Bool](imageanchor/istracked.md)
  A Boolean value that indicates whether ARKit is currently tracking this image.
- [var description: String](imageanchor/description.md)
  A textual representation of this anchor.
- [var id: UUID](imageanchor/id.md)
  The unique identifier of this anchor.

## Relationships

### Conforms To
- [Anchor](anchor.md)
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [TrackableAnchor](trackableanchor.md)

## See Also

- [Tracking and altering images](tracking-and-altering-images.md)
  Create images from rectangular shapes found in the user’s environment, and augment their appearance.
- [Detecting Images in an AR Experience](detecting-images-in-an-ar-experience.md)
  React to known 2D images in the user’s environment, and use their positions to place AR content.
- [Tracking preregistered images in 3D space](../visionOS/tracking-images-in-3d-space.md)
  Place content based on the current position of a known image in a person’s surroundings.
- [class ImageTrackingProvider](imagetrackingprovider.md)
  A source of live data about a 2D image’s position in a person’s surroundings.
- [struct ReferenceImage](referenceimage.md)
  A 2D image the system uses as a reference to find the same image in a person’s surroundings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/imageanchor)*