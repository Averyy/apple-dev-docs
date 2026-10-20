# vImage.Gamma

**Framework**: Accelerate  
**Kind**: enum  
**Role**: Enumeration

Describes either a used-defined or constant gamma.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
enum Gamma
```

## Topics

### User Defined Gamma
- [vImage.Gamma.fullPrecision(_:)](./gamma/fullprecision%28_%29.md)
  A user-defined gamma value with full-precision calculation.
- [vImage.Gamma.halfPrecision(_:)](./gamma/halfprecision%28_%29.md)
  A user-defined gamma value with half-precision calculation.
### Constant Gamma
- [vImage.Gamma.bt709ForwardHalfPrecision](./gamma/bt709forwardhalfprecision.md)
  ITU-R BT.709 standard.
- [vImage.Gamma.bt709ReverseHalfPrecision](./gamma/bt709reversehalfprecision.md)
  ITU-R BT.709 standard reverse.
- [vImage.Gamma.elevenOverFiveHalfPrecision](./gamma/elevenoverfivehalfprecision.md)
  Half-precision calculation using a gamma value of `11/5` or `2.2`.
- [vImage.Gamma.elevenOverNineHalfPrecision](./gamma/elevenoverninehalfprecision.md)
  Half-precision calculation using a gamma value of `11/9` or `(11/5)/(9/5)`.
- [vImage.Gamma.fiveOverElevenHalfPrecision](./gamma/fiveoverelevenhalfprecision.md)
  Half-precision calculation using a gamma value of `5/11` or `1/2.2`.
- [vImage.Gamma.fiveOverNineHalfPrecision](./gamma/fiveoverninehalfprecision.md)
  Half-precision calculation using a gamma value of `5/9` or `1/1.8`.
- [vImage.Gamma.nineOverElevenHalfPrecision](./gamma/nineoverelevenhalfprecision.md)
  Half-precision calculation using a gamma value of `9/11` or `(9/5)/(11/5)`.
- [vImage.Gamma.nineOverFiveHalfPrecision](./gamma/nineoverfivehalfprecision.md)
  Half-precision calculation using a gamma value of `9/5` or `1.8`.
- [vImage.Gamma.sRGBForwardHalfPrecision](./gamma/srgbforwardhalfprecision.md)
  Half-precision calculation using the sRGB standard gamma value of `2.2`.
- [vImage.Gamma.sRGBReverseHalfPrecision](./gamma/srgbreversehalfprecision.md)
  Half-precision calculation using the sRGB standard gamma value of `1/2.2`.

## See Also

### Enumerations
- [vImage.BlendMode](./blendmode.md)
  Constants that specify an alpha blending mode.
- [vImage.BufferType](./buffertype.md)
  Codes that represent vImage buffer types.
- [vImage.ChannelOrdering](./channelordering.md)
  Constants that specify the channel ordering of a pixel buffer.
- [vImage.CompositeMode](./compositemode.md)
  Constants that specify whether the format of layers is premultiplied or nonpremultiplied.
- [vImage.EdgeMode](./edgemode.md)
  Constants that specify edge modes for convolution operations.
- [vImage.Error](./error.md)
  An error that occurs during a vImage operation.
- [vImage.FloodFillConnectivity](./floodfillconnectivity.md)
- [vImage.MorphologyOperation](./morphologyoperation.md)
  Describes which morphology operation to perform.
- [vImage.ReflectionAxis](./reflectionaxis.md)
  The axis to reflect an image.
- [vImage.Rotation](./rotation.md)
  The angle to rotate an image.
- [vImage.ShearDirection](./sheardirection.md)
  The shear direction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/gamma)*