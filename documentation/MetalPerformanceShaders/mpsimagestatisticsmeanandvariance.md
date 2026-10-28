# MPSImageStatisticsMeanAndVariance

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

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

```objc
@interface MPSImageStatisticsMeanAndVariance : MPSUnaryImageKernel
```

## Overview

The mean and variance values are written to the destination image at the following pixel locations:

- Mean value is written at pixel location `(0, 0)`
- Variance value is written at pixel location `(1, 0)`

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](./mpsimagestatisticsmeanandvariance/init%28coder,device%29.md)
- [init(device: any MTLDevice)](./mpsimagestatisticsmeanandvariance/init%28device%29.md)
### Instance Properties
- [var clipRectSource: MTLRegion](./mpsimagestatisticsmeanandvariance/cliprectsource.md)

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

### Image Statistics Filters
- [class MPSImageStatisticsMean](./mpsimagestatisticsmean.md)
  A kernel that computes the mean for a given region of an image.
- [class MPSImageStatisticsMinAndMax](./mpsimagestatisticsminandmax.md)
  A kernel that computes the minimum and maximum pixel values for a given region of an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagestatisticsmeanandvariance)*