# ARReferenceImage

**Framework**: ARKit  
**Kind**: class

A 2D image that you want ARKit to detect in the physical environment.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.1+

## Declaration

```swift
class ARReferenceImage
```

#### Overview

To accurately detect the position and orientation of a 2D image in the real world, ARKit requires preprocessed image data and knowledge of the image’s real-world dimensions. The [`ARReferenceImage`](arreferenceimage.md) class encapsulates this information. To enable image detection in an AR session, pass a collection of reference images to your session configuration’s [`detectionImages`](arworldtrackingconfiguration/detectionimages.md) property.

Typically, you create reference images in your Xcode project’s asset catalog:

1. In your asset catalog, use the Add (+) button to create an AR Resource Group.
2. Drag image files into the resource group to create AR Reference Image entries in the asset catalog.
3. For each reference image, use the Xcode inspector panel to provide the real-world size at which you want ARKit to recognize the image. (You can also provide a descriptive name, which appears as the [`name`](arreferenceimage/name.md) property at runtime and can be useful for debugging.)

## Topics

### Loading Reference Images
- [class func referenceImages(inGroupNamed: String, bundle: Bundle?) -> Set<ARReferenceImage>?](arreferenceimage/referenceimages(ingroupnamed:bundle:).md)
  Loads all reference images in the specified AR Resource Group in your Xcode project’s asset catalog.
### Examining a Reference Image
- [var name: String?](arreferenceimage/name.md)
  A descriptive name for the image.
- [var physicalSize: CGSize](arreferenceimage/physicalsize.md)
  The real-world dimensions, in meters, of the image.
- [var resourceGroupName: String?](arreferenceimage/resourcegroupname.md)
  The AR resource group name for this image.
### Creating Reference Images
- [init(CGImage, orientation: CGImagePropertyOrientation, physicalWidth: CGFloat)](arreferenceimage/init(_:orientation:physicalwidth:)-8b3bs.md)
  Creates a new reference image from a Core Graphics image object.
- [init(CVPixelBuffer, orientation: CGImagePropertyOrientation, physicalWidth: CGFloat)](arreferenceimage/init(_:orientation:physicalwidth:)-ir2z.md)
  Creates a new reference image from a Core Video pixel buffer.
### Validating Reference Images
- [func validate(completionHandler: ((any Error)?) -> Void)](arreferenceimage/validate(completionhandler:).md)
  Determines whether the reference image is valid.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Tracking and altering images](tracking-and-altering-images.md)
  Create images from rectangular shapes found in the user’s environment, and augment their appearance.
- [Detecting Images in an AR Experience](detecting-images-in-an-ar-experience.md)
  React to known 2D images in the user’s environment, and use their positions to place AR content.
- [class ARImageAnchor](arimageanchor.md)
  An anchor for a known image that ARKit detects in the physical environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arreferenceimage)*