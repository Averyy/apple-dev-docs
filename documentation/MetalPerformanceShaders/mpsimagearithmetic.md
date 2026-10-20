# MPSImageArithmetic

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

Base class for basic arithmetic nodes

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSImageArithmetic
```

```objc
@interface MPSImageArithmetic : MPSBinaryImageKernel
```

## Topics

### Instance Properties
- [var bias: Float](./mpsimagearithmetic/bias.md)
- [var primaryScale: Float](./mpsimagearithmetic/primaryscale.md)
- [var primaryStrideInPixels: MTLSize](./mpsimagearithmetic/primarystrideinpixels.md)
- [var secondaryScale: Float](./mpsimagearithmetic/secondaryscale.md)
- [var secondaryStrideInPixels: MTLSize](./mpsimagearithmetic/secondarystrideinpixels.md)
- [var maximumValue: Float](./mpsimagearithmetic/maximumvalue.md)
- [var minimumValue: Float](./mpsimagearithmetic/minimumvalue.md)

## Relationships

### Inherits From
- [MPSBinaryImageKernel](./mpsbinaryimagekernel.md)
### Inherited By
- [MPSImageAdd](./mpsimageadd.md)
- [MPSImageDivide](./mpsimagedivide.md)
- [MPSImageMultiply](./mpsimagemultiply.md)
- [MPSImageSubtract](./mpsimagesubtract.md)
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

### Image Arithmetic Filters
- [class MPSImageAdd](./mpsimageadd.md)
  A filter that returns the element-wise sum of its two input images.
- [class MPSImageSubtract](./mpsimagesubtract.md)
  A filter that returns the element-wise difference of its two input images.
- [class MPSImageMultiply](./mpsimagemultiply.md)
  A filter that returns the element-wise product of its two input images.
- [class MPSImageDivide](./mpsimagedivide.md)
  A filter that returns the element-wise quotient of its two input images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagearithmetic)*