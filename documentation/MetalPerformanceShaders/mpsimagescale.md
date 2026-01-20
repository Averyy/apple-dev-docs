# MPSImageScale

**Framework**: Metal Performance Shaders  
**Kind**: class

A filter that resizes and changes the aspect ratio of an image.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSImageScale
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpsimagescale/init(coder:device:).md)
- [init(device: any MTLDevice)](mpsimagescale/init(device:).md)
### Instance Properties
- [var scaleTransform: UnsafePointer<MPSScaleTransform>?](mpsimagescale/scaletransform.md)

## Relationships

### Inherits From
- [MPSUnaryImageKernel](mpsunaryimagekernel.md)
### Inherited By
- [MPSImageBilinearScale](mpsimagebilinearscale.md)
- [MPSImageLanczosScale](mpsimagelanczosscale.md)
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

- [class MPSImageConversion](mpsimageconversion.md)
  A filter that performs a conversion of color space, alpha, or pixel format.
- [class MPSImageLanczosScale](mpsimagelanczosscale.md)
  A filter that resizes and changes the aspect ratio of an image using Lanczos resampling.
- [class MPSImageBilinearScale](mpsimagebilinearscale.md)
  A filter that resizes and changes the aspect ratio of an image using Bilinear resampling.
- [class MPSImageTranspose](mpsimagetranspose.md)
  A filter that transposes an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagescale)*