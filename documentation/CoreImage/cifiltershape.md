# CIFilterShape

**Framework**: Core Image  
**Kind**: class  
**Role**: Class

A description of the bounding shape of a filter and the domain of definition for a filter operation.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class CIFilterShape
```

```objc
@interface CIFilterShape : NSObject
```

#### Overview

You use `CIFilterShape` objects in conjunction with Core Image classes, such as [`CIFilter`](./cifilter-swift.class.md), [`CIKernel`](./cikernel.md), and [`CISampler`](./cisampler.md), to create custom filters.

## Topics

### Initializing a Filter Shape
- [init(rect: CGRect)](./cifiltershape/init%28rect%29.md)
  Initializes a filter shape object with a rectangle.
### Inspecting a Filter Shape
- [var extent: CGRect](./cifiltershape/extent.md)
  The extent of the filter shape.
### Modifying a Filter Shape
- [func insetBy(x: Int32, y: Int32) -> CIFilterShape](./cifiltershape/insetby%28x,y%29.md)
  Modifies a filter shape object so that it is inset by the specified x and y values.
- [func intersect(with: CIFilterShape) -> CIFilterShape](./cifiltershape/intersect%28with%29-8iw.md)
  Creates a filter shape object that represents the intersection of the current filter shape and the specified filter shape object.
- [func intersect(with: CGRect) -> CIFilterShape](./cifiltershape/intersect%28with%29-2o2n8.md)
  Creates a filter shape that represents the intersection of the current filter shape and a rectangle.
- [func transform(by: CGAffineTransform, interior: Bool) -> CIFilterShape](./cifiltershape/transform%28by,interior%29.md)
  Creates a filter shape that results from applying a transform to the current filter shape.
- [func union(with: CIFilterShape) -> CIFilterShape](./cifiltershape/union%28with%29-52mnd.md)
  Creates a filter shape that results from the union of the current filter shape and another filter shape object.
- [func union(with: CGRect) -> CIFilterShape](./cifiltershape/union%28with%29-75ebo.md)
  Creates a filter shape that results from the union of the current filter shape and a rectangle.
### Creating a Filter Shape
- [+ shapeWithRect:](./cifiltershape/shapewithrect_.md)
  Creates a filter shape object and initializes it with a rectangle.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Custom Filters
- [Writing Custom Kernels](./writing-custom-kernels.md)
  Write your own custom kernels in either the Core Image Kernel Language or the Metal Shading Language.
- [class CIKernel](./cikernel.md)
  A GPU-based image-processing routine used to create custom Core Image filters.
- [class CIColorKernel](./cicolorkernel.md)
  A GPU-based image-processing routine that processes only the color information in images, used to create custom Core Image filters.
- [class CIWarpKernel](./ciwarpkernel.md)
  A GPU-based image-processing routine that processes only the geometry information in an image, used to create custom Core Image filters.
- [class CIBlendKernel](./ciblendkernel.md)
  A GPU-based image-processing routine that is optimized for blending two images.
- [class CISampler](./cisampler.md)
  An object that retrieves pixel samples for processing by a filter kernel.
- [struct CIFormat](./ciformat.md)
  Pixel data formats for image input, output, and processing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifiltershape)*