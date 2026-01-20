# MPSImageThresholdTruncate

**Framework**: Metal Performance Shaders  
**Kind**: class

A filter that clamps the return value to an upper specified value.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class MPSImageThresholdTruncate
```

#### Overview

An [`MPSImageThresholdTruncate`](mpsimagethresholdtruncate.md) filter converts a single channel image to a binary image. If the input image is not a single channel image, the function first converts the input image into a single channel luminance image using the linear gray color transform, and then it applies the threshold.

The following listing shows the threshold truncate function.

Listing 1. Threshold truncate function

```other
destinationPixelValue = sourcePixelValue > thresholdValue ? thresholdValue : sourcePixelValue
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpsimagethresholdtruncate/init(coder:device:).md)
### Methods
- [init(device: any MTLDevice, thresholdValue: Float, linearGrayColorTransform: UnsafePointer<Float>?)](mpsimagethresholdtruncate/init(device:thresholdvalue:lineargraycolortransform:).md)
  Initializes the kernel.
### Properties
- [var thresholdValue: Float](mpsimagethresholdtruncate/thresholdvalue.md)
  The threshold value used to initialize the threshold filter.
- [var transform: UnsafePointer<Float>](mpsimagethresholdtruncate/transform.md)
  The color transform used to initialize the threshold filter.

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

- [class MPSImageThresholdBinary](mpsimagethresholdbinary.md)
  A filter that returns a specified value for each pixel with a value greater than a specified threshold or 0 otherwise.
- [class MPSImageThresholdBinaryInverse](mpsimagethresholdbinaryinverse.md)
  A filter that returns 0 for each pixel with a value greater than a specified threshold or a specified value otherwise.
- [class MPSImageThresholdToZero](mpsimagethresholdtozero.md)
  A filter that returns the original value for each pixel with a value greater than a specified threshold or 0 otherwise.
- [class MPSImageThresholdToZeroInverse](mpsimagethresholdtozeroinverse.md)
  A filter that returns 0 for each pixel with a value greater than a specified threshold or the original value otherwise.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagethresholdtruncate)*