# MPSImageSobel

**Framework**: Metal Performance Shaders  
**Kind**: class

A filter that convolves an image with the Sobel operator.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class MPSImageSobel
```

#### Overview

When the color model (e.g. RGB, two-channel, grayscale, etc.) of the source and destination textures match, the filter is applied to each color channel separately. If the destination is single-channel (i.e. monochrome) but the source is multi-channel, the pixel values are converted to grayscale before applying the Sobel operator by using the linear gray color transform vector `v` shown in the code listing below.

```objc
Luminance = v[0] * pixel.x + v[1] * pixel.y + v[2] * pixel.z
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpsimagesobel/init(coder:device:).md)
### Methods
- [convenience init(device: any MTLDevice)](mpsimagesobel/init(device:).md)
  Initializes a Sobel filter on a given device using the default color transform.
- [init(device: any MTLDevice, linearGrayColorTransform: UnsafePointer<Float>)](mpsimagesobel/init(device:lineargraycolortransform:).md)
  Initializes a Sobel filter on a given device using a specific color transform.
### Properties
- [var colorTransform: UnsafePointer<Float>](mpsimagesobel/colortransform.md)
  The color transform used to initialize the Sobel filter.

## Relationships

### Inherits From
- [MPSUnaryImageKernel](mpsunaryimagekernel.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class MPSImageConvolution](mpsimageconvolution.md)
  A filter that convolves an image with a given kernel of odd width and height.
- [class MPSImageMedian](mpsimagemedian.md)
  A filter that applies a median filter in a square region centered around each pixel in the source image.
- [class MPSImageBox](mpsimagebox.md)
  A filter that convolves an image with a given kernel of odd width and height.
- [class MPSImageTent](mpsimagetent.md)
  A filter that convolves an image with a tent filter.
- [class MPSImageGaussianBlur](mpsimagegaussianblur.md)
  A filter that convolves an image with a Gaussian blur of a given sigma in both the x and y directions.
- [class MPSImageGaussianPyramid](mpsimagegaussianpyramid.md)
  A filter that convolves an image with a Gaussian pyramid.
- [class MPSImageLaplacian](mpsimagelaplacian.md)
  An optimized Laplacian filter, provided for ease of use.
- [class MPSImageLaplacianPyramid](mpsimagelaplacianpyramid.md)
  A filter that convolves an image with a Laplacian filter.
- [class MPSImageLaplacianPyramidAdd](mpsimagelaplacianpyramidadd.md)
  A filter that convolves an image with an additive Laplacian pyramid.
- [class MPSImageLaplacianPyramidSubtract](mpsimagelaplacianpyramidsubtract.md)
  A filter that convolves an image with a subtractive Laplacian pyramid.
- [class MPSImagePyramid](mpsimagepyramid.md)
  A base class for creating different kinds of pyramid images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagesobel)*