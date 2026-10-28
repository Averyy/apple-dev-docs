# MPSAlphaType

**Framework**: Metal Performance Shaders  
**Kind**: enum  
**Role**: Enumeration

Premultiplication description for the color channels of an image.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
enum MPSAlphaType
```

```c
enum MPSAlphaType : NSUInteger;
```

## Overview

Some image data is premultiplied. That is to say that the color channels are stored instead as `color*alpha`. This is an optimization for image compositing (alpha blending), but it can get in the way of most other image filters, especially those that apply non-linear effects like the color conversion filters and functions like convolution or resampling filters that look at adjacent pixels, where the alpha may not be the same. The following are some basic conversion cases:

| Source | Destination | Operation |
| --- | --- | --- |
| `NonPremultiplied` | `NonPremultiplied` | None. |
| `NonPremultiplied` | `AlphaIsOne` | Composite with opaque background color. |
| `NonPremultiplied` | `Premultiplied` | Multiply color channels by alpha. |
| `AlphaIsOne` | `NonPremultiplied` | Set alpha to 1. |
| `AlphaIsOne` | `AlphaIsOne` | Set alpha to 1. |
| `AlphaIsOne` | `Premultiplied` | Set alpha to 1. |
| `Premultiplied` | `NonPremultiplied` | Divide color channels by alpha. |
| `Premultiplied` | `AlphaIsOne` | Composite with opaque background color. |
| `Premultiplied` | `Premultiplied` | None. |

Most [`MPSKernel`](./mpskernel.md) objects require non-premultiplied or completely opaque colors to work correctly. They implictly assume that alpha is equal to 1 and do not provide functions for the user to specify alpha channel types. Currently, the only filters that can handle premultiplied data are the color conversion filters provided by [`MPSImageConversion`](./mpsimageconversion.md) kernels and they insert extra operations to ensure a correct conversion. Fully opaque images should use `MPSAlphaTypeAlphaIsOne`

## Topics

### Constants
- [MPSAlphaType.nonPremultiplied](./mpsalphatype/nonpremultiplied.md)
  The image is not premultiplied by alpha.
- [MPSAlphaType.alphaIsOne](./mpsalphatype/alphaisone.md)
  Alpha is guaranteed to be 1.
- [MPSAlphaType.premultiplied](./mpsalphatype/premultiplied.md)
  The image is premultiplied by alpha.
### Initializers
- [init?(rawValue: UInt)](./mpsalphatype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Methods
- [init(device: any MTLDevice, srcAlpha: MPSAlphaType, destAlpha: MPSAlphaType, backgroundColor: UnsafeMutablePointer<CGFloat>?, conversionInfo: CGColorConversionInfo?)](./mpsimageconversion/init%28device,srcalpha,destalpha,backgroundcolor,conversioninfo%29.md)
  Initializes a filter that can convert texture color space, alpha, and pixel format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsalphatype)*