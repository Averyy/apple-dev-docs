# MPSCNNUpsampling

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

A filter that resamples an existing MPS image.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNUpsampling
```

```objc
@interface MPSCNNUpsampling : MPSCNNKernel
```

#### Overview

This filter can be used to resample an existing [`MPSImage`](./mpsimage.md) using a different sampling frequency for the `x` and `y` dimensions with the purpose of enlarging the size of an image.

The number of output feature channels remains the same as the number of input feature channels.

The `scaleFactor` must be an integer value `>= 1`. The default value is `1`.

Nearest and bilinear variants are supported.

## Topics

### Instance Properties
- [var scaleFactorX: Double](./mpscnnupsampling/scalefactorx.md)
- [var scaleFactorY: Double](./mpscnnupsampling/scalefactory.md)
- [var alignCorners: Bool](./mpscnnupsampling/aligncorners.md)

## Relationships

### Inherits From
- [MPSCNNKernel](./mpscnnkernel.md)
### Inherited By
- [MPSCNNUpsamplingBilinear](./mpscnnupsamplingbilinear.md)
- [MPSCNNUpsamplingNearest](./mpscnnupsamplingnearest.md)
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

### Upsampling Layers
- [class MPSCNNUpsamplingBilinear](./mpscnnupsamplingbilinear.md)
  A bilinear spatial upsampling filter.
- [class MPSCNNUpsamplingNearest](./mpscnnupsamplingnearest.md)
  A nearest spatial upsampling filter.
- [class MPSCNNUpsamplingBilinearGradient](./mpscnnupsamplingbilineargradient.md)
  A gradient bilinear spatial upsampling filter.
- [class MPSCNNUpsamplingGradient](./mpscnnupsamplinggradient.md)
  A gradient filter that upsamples an existing Metal Performance Shaders image.
- [class MPSCNNUpsamplingNearestGradient](./mpscnnupsamplingnearestgradient.md)
  A gradient upsampling filter that samples the pixel nearest to the source when upsampling to the destination pixel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnupsampling)*