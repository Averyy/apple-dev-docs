# MPSImageTranspose

**Framework**: Metal Performance Shaders  
**Kind**: class

A filter that transposes an image.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class MPSImageTranspose
```

#### Overview

An [`MPSImageTranspose`](mpsimagetranspose.md) filter applies a matrix transposition to the source image by exchanging its rows with its columns.

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

- [class MPSImageConversion](mpsimageconversion.md)
  A filter that performs a conversion of color space, alpha, or pixel format.
- [class MPSImageScale](mpsimagescale.md)
  A filter that resizes and changes the aspect ratio of an image.
- [class MPSImageLanczosScale](mpsimagelanczosscale.md)
  A filter that resizes and changes the aspect ratio of an image using Lanczos resampling.
- [class MPSImageBilinearScale](mpsimagebilinearscale.md)
  A filter that resizes and changes the aspect ratio of an image using Bilinear resampling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagetranspose)*