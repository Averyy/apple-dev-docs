# MPSImageThresholdBinary

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

A filter that returns a specified value for each pixel with a value greater than a specified threshold or 0 otherwise.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class MPSImageThresholdBinary
```

```objc
@interface MPSImageThresholdBinary : MPSUnaryImageKernel
```

#### Overview

An [`MPSImageThresholdBinary`](./mpsimagethresholdbinary.md) filter converts a single channel image to a binary image. If the input image is not a single channel image, the function first converts the input image into a single channel luminance image using the linear gray color transform, and then it applies the threshold.

The following listing shows the threshold binary function.

Listing 1. Threshold binary function

```other
destinationPixelValue = sourcePixelValue > thresholdValue ? maximumValue : 0
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](./mpsimagethresholdbinary/init%28coder,device%29.md)
### Methods
- [init(device: any MTLDevice, thresholdValue: Float, maximumValue: Float, linearGrayColorTransform: UnsafePointer<Float>?)](./mpsimagethresholdbinary/init%28device,thresholdvalue,maximumvalue,lineargraycolortransform%29.md)
  Initializes the kernel.
### Properties
- [var thresholdValue: Float](./mpsimagethresholdbinary/thresholdvalue.md)
  The threshold value used to initialize the threshold filter.
- [var maximumValue: Float](./mpsimagethresholdbinary/maximumvalue.md)
  The maximum value used to initialize the threshold filter.
- [var transform: UnsafePointer<Float>](./mpsimagethresholdbinary/transform.md)
  The color transform used to initialize the threshold filter.

## Relationships

### Inherits From
- [MPSUnaryImageKernel](./mpsunaryimagekernel.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Image Threshold Filters
- [class MPSImageThresholdBinaryInverse](./mpsimagethresholdbinaryinverse.md)
  A filter that returns 0 for each pixel with a value greater than a specified threshold or a specified value otherwise.
- [class MPSImageThresholdToZero](./mpsimagethresholdtozero.md)
  A filter that returns the original value for each pixel with a value greater than a specified threshold or 0 otherwise.
- [class MPSImageThresholdToZeroInverse](./mpsimagethresholdtozeroinverse.md)
  A filter that returns 0 for each pixel with a value greater than a specified threshold or the original value otherwise.
- [class MPSImageThresholdTruncate](./mpsimagethresholdtruncate.md)
  A filter that clamps the return value to an upper specified value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagethresholdbinary)*