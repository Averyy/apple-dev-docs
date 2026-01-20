# MPSImageThresholdBinary

**Framework**: Metal Performance Shaders  
**Kind**: class

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

#### Overview

An [`MPSImageThresholdBinary`](mpsimagethresholdbinary.md) filter converts a single channel image to a binary image. If the input image is not a single channel image, the function first converts the input image into a single channel luminance image using the linear gray color transform, and then it applies the threshold.

The following listing shows the threshold binary function.

Listing 1. Threshold binary function

```other
destinationPixelValue = sourcePixelValue > thresholdValue ? maximumValue : 0
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpsimagethresholdbinary/init(coder:device:).md)
### Methods
- [init(device: any MTLDevice, thresholdValue: Float, maximumValue: Float, linearGrayColorTransform: UnsafePointer<Float>?)](mpsimagethresholdbinary/init(device:thresholdvalue:maximumvalue:lineargraycolortransform:).md)
  Initializes the kernel.
### Properties
- [var thresholdValue: Float](mpsimagethresholdbinary/thresholdvalue.md)
  The threshold value used to initialize the threshold filter.
- [var maximumValue: Float](mpsimagethresholdbinary/maximumvalue.md)
  The maximum value used to initialize the threshold filter.
- [var transform: UnsafePointer<Float>](mpsimagethresholdbinary/transform.md)
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

- [class MPSImageThresholdBinaryInverse](mpsimagethresholdbinaryinverse.md)
  A filter that returns 0 for each pixel with a value greater than a specified threshold or a specified value otherwise.
- [class MPSImageThresholdToZero](mpsimagethresholdtozero.md)
  A filter that returns the original value for each pixel with a value greater than a specified threshold or 0 otherwise.
- [class MPSImageThresholdToZeroInverse](mpsimagethresholdtozeroinverse.md)
  A filter that returns 0 for each pixel with a value greater than a specified threshold or the original value otherwise.
- [class MPSImageThresholdTruncate](mpsimagethresholdtruncate.md)
  A filter that clamps the return value to an upper specified value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagethresholdbinary)*