# CIKernel

**Framework**: Core Image  
**Kind**: class  
**Role**: Class

A GPU-based image-processing routine used to create custom Core Image filters.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS
- visionOS 1.0+

## Declaration

```swift
class CIKernel
```

```objc
@interface CIKernel : NSObject
```

## Mentions

- [Writing Custom Kernels](./writing-custom-kernels.md)

#### Overview

> **Note**:  If your custom filter uses both color and geometry information, but does not require processing both at the same time, you can improve performance by separating your image processing code: use a [`CIColorKernel`](./cicolorkernel.md) object for the color processing step and a [`CIWarpKernel`](./ciwarpkernel.md) object for the geometry processing step.

The kernel language routine for a general-purpose filter kernel has the following characteristics:

- Its return type is `vec4` (Core Image Kernel Language) or `float4` (Metal Shading Language); that is, it returns a pixel color for the output image.
- It may use zero or more input images. Each input image is represented by a parameter of type `sampler`.

A kernel routine typically produces its output by calculating source image coordinates (using the `destCoord` and `samplerTransform` functions or the `samplerTransform` function), samples from the source images (using the `sample` function), and computes a final pixel color (output using the `return` keyword). For example, the Metal Shading Language source below implements a filter that passes through its input image unchanged.

```c
#include <CoreImage/CoreImage.h>
 
extern "C" {
    namespace coreimage {
        float4 do_nothing(sampler src) {
            return src.sample(src.coord());
        }
    }
}
```

The equivalent code in Core Image Kernel Language is:

```c
kernel vec4 do_nothing(sampler image) {
    vec2 dc = destCoord();
    return sample(image, samplerTransform(image, dc));
}
```

The Core Image Kernel Language is a dialect of the OpenGL Shading Language. See [Core Image Kernel Language Reference](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Reference/CIKernelLangRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004397) and [Core Image Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreImaging/ci_intro/ci_intro.html#//apple_ref/doc/uid/TP30001185) for more details.

## Topics

### Creating a Kernel Using Metal Shading Language
- [convenience init(functionName: String, fromMetalLibraryData: Data) throws](./cikernel/init%28functionname,frommetallibrarydata%29.md)
  Creates a single kernel object using a Metal Shading Language (MSL) kernel function.
- [convenience init(functionName: String, fromMetalLibraryData: Data, outputPixelFormat: CIFormat) throws](./cikernel/init%28functionname,frommetallibrarydata,outputpixelformat%29.md)
  Creates a single kernel object using a Metal Shading Language kernel function with optional pixel format.
- [class func kernelNames(fromMetalLibraryData: Data) -> [String]](./cikernel/kernelnames%28frommetallibrarydata%29.md)
  Return an array of strings containing the names of all of the kernels contained in the Metal library.
- [class func kernels(withMetalString: String) throws -> [CIKernel]](./cikernel/kernels%28withmetalstring%29.md)
  Load kernels from a Metal language string.
### Getting a Kernel Name
- [var name: String](./cikernel/name.md)
  The name of the kernel routine.
### Identifying the Region of Interest for the Kernel
- [func setROISelector(Selector)](./cikernel/setroiselector%28_%29.md)
  Sets the selector Core Image uses to query the region of interest for image processing with the kernel.
### Applying a Kernel to Filter an Image
- [func apply(extent: CGRect, roiCallback: CIKernelROICallback, arguments: [Any]) -> CIImage?](./cikernel/apply%28extent,roicallback,arguments%29.md)
  Creates a new image using the kernel and specified arguments.
- [typealias CIKernelROICallback](./cikernelroicallback.md)
  The signature for a block that computes the region of interest (ROI) for a given area of destination image pixels. Core Image calls this block when applying the kernel. You specify this block when using the [`apply(extent:roiCallback:arguments:)`](./cikernel/apply%28extent,roicallback,arguments%29.md) method.
### Deprecated
- [convenience init?(source: String)](./cikernel/init%28source%29.md)
  Creates a single kernel object.
- [class func makeKernels(source: String) -> [CIKernel]?](./cikernel/makekernels%28source%29.md)
  Creates and returns and array of  `CIKernel` objects.
### Initializers
- [convenience init?(string: String)](./cikernel/init%28string%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [CIColorKernel](./cicolorkernel.md)
- [CIWarpKernel](./ciwarpkernel.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Custom Filters
- [Writing Custom Kernels](./writing-custom-kernels.md)
  Write your own custom kernels in either the Core Image Kernel Language or the Metal Shading Language.
- [class CIColorKernel](./cicolorkernel.md)
  A GPU-based image-processing routine that processes only the color information in images, used to create custom Core Image filters.
- [class CIWarpKernel](./ciwarpkernel.md)
  A GPU-based image-processing routine that processes only the geometry information in an image, used to create custom Core Image filters.
- [class CIBlendKernel](./ciblendkernel.md)
  A GPU-based image-processing routine that is optimized for blending two images.
- [class CISampler](./cisampler.md)
  An object that retrieves pixel samples for processing by a filter kernel.
- [class CIFilterShape](./cifiltershape.md)
  A description of the bounding shape of a filter and the domain of definition for a filter operation.
- [struct CIFormat](./ciformat.md)
  Pixel data formats for image input, output, and processing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cikernel)*