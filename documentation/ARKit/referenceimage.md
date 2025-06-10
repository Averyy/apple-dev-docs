# ReferenceImage

**Framework**: ARKit  
**Kind**: struct

A 2D image the system uses as a reference to find the same image in a person’s surroundings.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
struct ReferenceImage
```

## Topics

### Creating a reference image
- [init(cgimage: CGImage, physicalSize: CGSize, orientation: CGImagePropertyOrientation)](referenceimage/init(cgimage:physicalsize:orientation:).md)
  Creates a reference image from a Core Graphics image.
- [init(pixelBuffer: CVPixelBuffer, physicalSize: CGSize, orientation: CGImagePropertyOrientation)](referenceimage/init(pixelbuffer:physicalsize:orientation:).md)
  Creates a reference image from a pixel buffer.
- [static func loadReferenceImages(inGroupNamed: String, bundle: Bundle?) -> [ReferenceImage]](referenceimage/loadreferenceimages(ingroupnamed:bundle:).md)
  Creates multiple reference images based on their group name in an asset catalog.
### Inspecting a reference image
- [var physicalSize: CGSize](referenceimage/physicalsize.md)
  The size, in meters, of a reference image in the real world.
- [var name: String?](referenceimage/name.md)
  The name of a reference image.
- [var resourceGroupName: String?](referenceimage/resourcegroupname.md)
  A string value the represents the name of the resource group the framework loads an image from.
- [var description: String](referenceimage/description.md)
  A textual representation of this reference image.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Tracking and altering images](tracking-and-altering-images.md)
  Create images from rectangular shapes found in the user’s environment, and augment their appearance.
- [Detecting Images in an AR Experience](detecting-images-in-an-ar-experience.md)
  React to known 2D images in the user’s environment, and use their positions to place AR content.
- [Tracking preregistered images in 3D space](../visionOS/tracking-images-in-3d-space.md)
  Place content based on the current position of a known image in a person’s surroundings.
- [class ImageTrackingProvider](imagetrackingprovider.md)
  A source of live data about a 2D image’s position in a person’s surroundings.
- [struct ImageAnchor](imageanchor.md)
  A 2D image’s position in a person’s surroundings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/referenceimage)*