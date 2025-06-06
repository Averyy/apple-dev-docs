# CGImagePropertyOrientation

**Framework**: Image I/O  
**Kind**: enum

A value describing the intended display orientation for an image.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.0+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
@frozen
enum CGImagePropertyOrientation
```

#### Overview

Values of this type define the position of the pixel coordinate origin point (`0,0`) and the directions of the coordinate axes relative to the intended display orientation of the image. Orientation values are commonly found in image metadata, and specifying image orientation correctly can be important both for displaying the image and for certain image processing tasks such as face recognition.

For example, the pixel data for an image captured by an iOS device camera is encoded in the camera sensor’s native landscape orientation. When the user captures a photo while holding the device in portrait orientation, iOS writes an orientation value of [`CGImagePropertyOrientation.right`](cgimagepropertyorientation/right.md) in the resulting image file. Software displaying the image can then, after reading that value from the file’s metadata, apply a 90° clockwise rotation to the image data so that the image appears in the photographer’s intended orientation.

![To correct an image with right orientation for display, rotate it 90° clockwise.](https://docs-assets.developer.apple.com/published/a4de8a358cbf9a76800cc595fceb8892/media-2948298%402x.png)

##### Compatibility with Uiimageorientation

The [`CGImagePropertyOrientation`](cgimagepropertyorientation.md) type covers the same set of orientation names available in from the [`UIImage.Orientation`](https://developer.apple.com/documentation/UIKit/UIImage/Orientation) type, but the underlying numeric values of each type do not match. (For example, the “left mirrored” orientation has an underlying value of 5 in [`CGImagePropertyOrientation`](cgimagepropertyorientation.md), but an underlying value of 7 in [`UIImage.Orientation`](https://developer.apple.com/documentation/UIKit/UIImage/Orientation).) If you have an orientation value in one type and need a semantically equivalent value in the other, use a function such as those below to produce the same-named value in the other type:

Listing 1. Converting between CGImagePropertyOrientation and UIImageOrientation

##### Working with Raw Tiffexif Numeric Values

Some APIs describe image orientation with basic integer values, intended for interpretation according to the TIFF and Exif specifications. The [`CGImagePropertyOrientation`](cgimagepropertyorientation.md) type simply defines symbolic names for those values, so you can convert to and from the raw numeric type with C type-cast syntax or the inherited [`init(rawValue:)`](https://developer.apple.com/documentation/Swift/RawRepresentable/init(rawValue:)) initializer and [`rawValue`](https://developer.apple.com/documentation/Swift/RawRepresentable/rawValue-swift.property) property in Swift.

## Topics

### Image Orientations
- [CGImagePropertyOrientation.up](cgimagepropertyorientation/up.md)
  The encoded image data matches the image’s intended display orientation.
- [CGImagePropertyOrientation.upMirrored](cgimagepropertyorientation/upmirrored.md)
  The encoded image data is horizontally flipped from the image’s intended display orientation.
- [CGImagePropertyOrientation.down](cgimagepropertyorientation/down.md)
  The encoded image data is rotated 180° from the image’s intended display orientation.
- [CGImagePropertyOrientation.downMirrored](cgimagepropertyorientation/downmirrored.md)
  The encoded image data is vertically flipped from the image’s intended display orientation.
- [CGImagePropertyOrientation.leftMirrored](cgimagepropertyorientation/leftmirrored.md)
  The encoded image data is horizontally flipped and rotated 90° counter-clockwise from the image’s intended display orientation.
- [CGImagePropertyOrientation.right](cgimagepropertyorientation/right.md)
  The encoded image data is rotated 90° clockwise from the image’s intended display orientation.
- [CGImagePropertyOrientation.rightMirrored](cgimagepropertyorientation/rightmirrored.md)
  The encoded image data is horizontally flipped and rotated 90° clockwise from the image’s intended display orientation.
- [CGImagePropertyOrientation.left](cgimagepropertyorientation/left.md)
  The encoded image data is rotated 90° clockwise from the image’s intended display orientation.
### Initializers
- [init?(rawValue: UInt32)](cgimagepropertyorientation/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [let kCGImagePropertyImageCount: CFString](kcgimagepropertyimagecount.md)
  The number of images in the file.
- [let kCGImagePropertyIsIndexed: CFString](kcgimagepropertyisindexed.md)
  A Boolean value that indicates whether the image contains indexed pixel samples.
- [let kCGImagePropertyImages: CFString](kcgimagepropertyimages.md)
  An array of dictionaries, each of which contains metadata for one of the images in the file.
- [let kCGImagePropertyThumbnailImages: CFString](kcgimagepropertythumbnailimages.md)
- [let kCGImagePropertyPrimaryImage: CFString](kcgimagepropertyprimaryimage.md)
  The index of the primary image in the file.
- [let kCGImagePropertyIsFloat: CFString](kcgimagepropertyisfloat.md)
  A Boolean value that indicates whether the image contains floating-point pixel samples.
- [let kCGImagePropertyOrientation: CFString](kcgimagepropertyorientation.md)
  The intended display orientation of the image.
- [Individual Image Properties](individual-image-properties.md)
  Properties that apply to an individual image in an image source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/cgimagepropertyorientation)*