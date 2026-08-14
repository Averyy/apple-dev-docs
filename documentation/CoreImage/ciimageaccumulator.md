# CIImageAccumulator

**Framework**: Core Image  
**Kind**: class

An object that manages feedback-based image processing for tasks such as painting or fluid simulation.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class CIImageAccumulator
```

#### Overview

The `CIImageAccumulator` class enables feedback-based image processing for such things as iterative painting operations or fluid dynamics simulations. You use `CIImageAccumulator` objects in conjunction with other Core Image classes, such as  [`CIFilter`](cifilter-swift.class.md), [`CIImage`](ciimage.md), [`CIVector`](civector.md), and [`CIContext`](cicontext.md), to take advantage of the built-in Core Image filters when processing images.

## Topics

### Initializing an Image Accumulator
- [init?(extent: CGRect, format: CIFormat)](ciimageaccumulator/init(extent:format:).md)
  Initializes an image accumulator with the specified extent and pixel format.
- [init?(extent: CGRect, format: CIFormat, colorSpace: CGColorSpace)](ciimageaccumulator/init(extent:format:colorspace:).md)
  Initializes an image accumulator with the specified extent, pixel format, and color space.
### Setting an Image
- [func setImage(CIImage)](ciimageaccumulator/setimage(_:).md)
  Sets the contents of the image accumulator to the contents of the specified image object.
- [func setImage(CIImage, dirtyRect: CGRect)](ciimageaccumulator/setimage(_:dirtyrect:).md)
  Updates an image accumulator with a subregion of an image object.
### Obtaining Data From an Image Accumulator
- [var extent: CGRect](ciimageaccumulator/extent.md)
  The extent of the image associated with the image accumulator.
- [var format: CIFormat](ciimageaccumulator/format.md)
  The pixel format of the image accumulator.
- [func image() -> CIImage](ciimageaccumulator/image.md)
  Returns the current contents of the image accumulator.
### Resetting an Accumulator
- [func clear()](ciimageaccumulator/clear.md)
  Resets the accumulator, discarding any pending updates and the current content.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageaccumulator)*