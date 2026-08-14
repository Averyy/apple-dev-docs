# MPSImageStatisticsMeanAndVariance

**Framework**: Metal Performance Shaders  
**Kind**: class

A kernel that computes the mean and variance for a given region of an image.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSImageStatisticsMeanAndVariance
```

#### Overview

The mean and variance values are written to the destination image at the following pixel locations:

- Mean value is written at pixel location `(0, 0)`
- Variance value is written at pixel location `(1, 0)`

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpsimagestatisticsmeanandvariance/init(coder:device:).md)
- [init(device: any MTLDevice)](mpsimagestatisticsmeanandvariance/init(device:).md)
### Instance Properties
- [var clipRectSource: MTLRegion](mpsimagestatisticsmeanandvariance/cliprectsource.md)

## Relationships

### Inherits From
- [MPSUnaryImageKernel](mpsunaryimagekernel.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)

## See Also

- [class MPSImageStatisticsMean](mpsimagestatisticsmean.md)
  A kernel that computes the mean for a given region of an image.
- [class MPSImageStatisticsMinAndMax](mpsimagestatisticsminandmax.md)
  A kernel that computes the minimum and maximum pixel values for a given region of an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagestatisticsmeanandvariance)*