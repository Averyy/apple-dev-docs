# MPSImageLanczosScale

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

A filter that resizes and changes the aspect ratio of an image using Lanczos resampling.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class MPSImageLanczosScale
```

```objc
@interface MPSImageLanczosScale : MPSImageScale
```

#### Overview

You can use this filter to enlarge or reduce the size of an image, or to change the aspect ratio of an image. The filter uses a Lanczos resampling algorithm, that typically produces better quality for photographs, but is slower than linear sampling that uses GPU texture units. Lanczos downsampling does not require a low pass filter to be applied before it is used. Because the resampling function has negative lobes, Lanczos can result in ringing artifacts near sharp edges, making it less suitable for vector art.

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](./mpsimagelanczosscale/init%28coder,device%29.md)
- [init(device: any MTLDevice)](./mpsimagelanczosscale/init%28device%29.md)
### Properties
- [struct MPSScaleTransform](./mpsscaletransform.md)
  A transform matrix for explicit resampling control with a Lanczos kernel.

## Relationships

### Inherits From
- [MPSImageScale](./mpsimagescale.md)
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

### Image Manipulation Filters
- [class MPSImageConversion](./mpsimageconversion.md)
  A filter that performs a conversion of color space, alpha, or pixel format.
- [class MPSImageScale](./mpsimagescale.md)
  A filter that resizes and changes the aspect ratio of an image.
- [class MPSImageBilinearScale](./mpsimagebilinearscale.md)
  A filter that resizes and changes the aspect ratio of an image using Bilinear resampling.
- [class MPSImageTranspose](./mpsimagetranspose.md)
  A filter that transposes an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagelanczosscale)*