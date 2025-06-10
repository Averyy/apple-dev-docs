# vImage.Gamma

**Framework**: Accelerate  
**Kind**: enum

Describes either a used-defined or constant gamma.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
enum Gamma
```

## Topics

### User Defined Gamma
- [vImage.Gamma.fullPrecision(_:)](vimage/gamma/fullprecision(_:).md)
  A user-defined gamma value with full-precision calculation.
- [vImage.Gamma.halfPrecision(_:)](vimage/gamma/halfprecision(_:).md)
  A user-defined gamma value with half-precision calculation.
### Constant Gamma
- [vImage.Gamma.bt709ForwardHalfPrecision](vimage/gamma/bt709forwardhalfprecision.md)
  ITU-R BT.709 standard.
- [vImage.Gamma.bt709ReverseHalfPrecision](vimage/gamma/bt709reversehalfprecision.md)
  ITU-R BT.709 standard reverse.
- [vImage.Gamma.elevenOverFiveHalfPrecision](vimage/gamma/elevenoverfivehalfprecision.md)
  Half-precision calculation using a gamma value of `11/5` or `2.2`.
- [vImage.Gamma.elevenOverNineHalfPrecision](vimage/gamma/elevenoverninehalfprecision.md)
  Half-precision calculation using a gamma value of `11/9` or `(11/5)/(9/5)`.
- [vImage.Gamma.fiveOverElevenHalfPrecision](vimage/gamma/fiveoverelevenhalfprecision.md)
  Half-precision calculation using a gamma value of `5/11` or `1/2.2`.
- [vImage.Gamma.fiveOverNineHalfPrecision](vimage/gamma/fiveoverninehalfprecision.md)
  Half-precision calculation using a gamma value of `5/9` or `1/1.8`.
- [vImage.Gamma.nineOverElevenHalfPrecision](vimage/gamma/nineoverelevenhalfprecision.md)
  Half-precision calculation using a gamma value of `9/11` or `(9/5)/(11/5)`.
- [vImage.Gamma.nineOverFiveHalfPrecision](vimage/gamma/nineoverfivehalfprecision.md)
  Half-precision calculation using a gamma value of `9/5` or `1.8`.
- [vImage.Gamma.sRGBForwardHalfPrecision](vimage/gamma/srgbforwardhalfprecision.md)
  Half-precision calculation using the sRGB standard gamma value of `2.2`.
- [vImage.Gamma.sRGBReverseHalfPrecision](vimage/gamma/srgbreversehalfprecision.md)
  Half-precision calculation using the sRGB standard gamma value of `1/2.2`.

## See Also

- [vImage.BlendMode](vimage/blendmode.md)
  Constants that specify an alpha blending mode.
- [vImage.BufferType](vimage/buffertype.md)
  Codes that represent vImage buffer types.
- [vImage.ChannelOrdering](vimage/channelordering.md)
  Constants that specify the channel ordering of a pixel buffer.
- [vImage.CompositeMode](vimage/compositemode.md)
  Constants that specify whether the format of layers is premultiplied or nonpremultiplied.
- [vImage.EdgeMode](vimage/edgemode.md)
  Constants that specify edge modes for convolution operations.
- [vImage.Error](vimage/error.md)
  An error that occurs during a vImage operation.
- [vImage.FloodFillConnectivity](vimage/floodfillconnectivity.md)
- [vImage.MorphologyOperation](vimage/morphologyoperation.md)
  Describes which morphology operation to perform.
- [vImage.ReflectionAxis](vimage/reflectionaxis.md)
  The axis to reflect an image.
- [vImage.Rotation](vimage/rotation.md)
  The angle to rotate an image.
- [vImage.ShearDirection](vimage/sheardirection.md)
  The shear direction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/gamma)*