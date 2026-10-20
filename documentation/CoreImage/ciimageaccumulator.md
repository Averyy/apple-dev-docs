# CIImageAccumulator

**Framework**: Core Image  
**Kind**: class  
**Role**: Class

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

```objc
@interface CIImageAccumulator : NSObject
```

#### Overview

The `CIImageAccumulator` class enables feedback-based image processing for such things as iterative painting operations or fluid dynamics simulations. You use `CIImageAccumulator` objects in conjunction with other Core Image classes, such as  [`CIFilter`](./cifilter-swift.class.md), [`CIImage`](./ciimage.md), [`CIVector`](./civector.md), and [`CIContext`](./cicontext.md), to take advantage of the built-in Core Image filters when processing images.

## Topics

### Initializing an Image Accumulator
- [init?(extent: CGRect, format: CIFormat)](./ciimageaccumulator/init%28extent,format%29.md)
  Initializes an image accumulator with the specified extent and pixel format.
- [init?(extent: CGRect, format: CIFormat, colorSpace: CGColorSpace)](./ciimageaccumulator/init%28extent,format,colorspace%29.md)
  Initializes an image accumulator with the specified extent, pixel format, and color space.
### Setting an Image
- [func setImage(CIImage)](./ciimageaccumulator/setimage%28_%29.md)
  Sets the contents of the image accumulator to the contents of the specified image object.
- [func setImage(CIImage, dirtyRect: CGRect)](./ciimageaccumulator/setimage%28_,dirtyrect%29.md)
  Updates an image accumulator with a subregion of an image object.
### Obtaining Data From an Image Accumulator
- [var extent: CGRect](./ciimageaccumulator/extent.md)
  The extent of the image associated with the image accumulator.
- [var format: CIFormat](./ciimageaccumulator/format.md)
  The pixel format of the image accumulator.
- [func image() -> CIImage](./ciimageaccumulator/image%28%29.md)
  Returns the current contents of the image accumulator.
### Resetting an Accumulator
- [func clear()](./ciimageaccumulator/clear%28%29.md)
  Resets the accumulator, discarding any pending updates and the current content.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageaccumulator)*