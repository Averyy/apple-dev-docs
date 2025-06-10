# vImage.BufferType

**Framework**: Accelerate  
**Kind**: enum

Codes that represent vImage buffer types.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS ?+
- watchOS 6.0+

## Declaration

```swift
enum BufferType
```

## Topics

### Initializers
- [init?(bufferTypeCode: Int, model: CGColorSpaceModel?)](vimage/buffertype/init(buffertypecode:model:).md)
  Creates a buffer type enumeration from the specified code and color space model.
### Enumeration Cases
- [vImage.BufferType.Cb](vimage/buffertype/cb.md)
  The buffer contains the blue chrominance channel.
- [vImage.BufferType.Cr](vimage/buffertype/cr.md)
  The buffer contains the red chrominance channel.
- [vImage.BufferType.YCbCr](vimage/buffertype/ycbcr.md)
  The buffer contains interleaved luminance and both chroma channels.
- [vImage.BufferType.alpha](vimage/buffertype/alpha.md)
  The buffer contains the alpha channel or coverage component.
- [vImage.BufferType.chroma](vimage/buffertype/chroma.md)
  The buffer contains the interleaved chrominance channels.
- [vImage.BufferType.chunky](vimage/buffertype/chunky.md)
  The buffer contains chunky data.
- [vImage.BufferType.cmykBlack](vimage/buffertype/cmykblack.md)
  The buffer contains the black channel.
- [vImage.BufferType.cmykCyan](vimage/buffertype/cmykcyan.md)
  The buffer contains the cyan channel.
- [vImage.BufferType.cmykMagenta](vimage/buffertype/cmykmagenta.md)
  The buffer contains the magenta channel.
- [vImage.BufferType.cmykYellow](vimage/buffertype/cmykyellow.md)
  The buffer contains the yellow channel.
- [vImage.BufferType.coreGraphics](vimage/buffertype/coregraphics.md)
  The buffer contains a Core Graphics image.
- [vImage.BufferType.indexed](vimage/buffertype/indexed.md)
  The buffer contains data in an indexed colorspace.
- [vImage.BufferType.labA](vimage/buffertype/laba.md)
  The buffer contains the `a*` channel.
- [vImage.BufferType.labB](vimage/buffertype/labb.md)
  The buffer contains the `b*` channel.
- [vImage.BufferType.labL](vimage/buffertype/labl.md)
  The buffer contains the `L*` channel.
- [vImage.BufferType.luminance](vimage/buffertype/luminance.md)
  The buffer contains only luminance data.
- [vImage.BufferType.monochrome](vimage/buffertype/monochrome.md)
  The buffer contains monochrome data.
- [vImage.BufferType.rgbBlue](vimage/buffertype/rgbblue.md)
  The buffer contains the blue channel.
- [vImage.BufferType.rgbGreen](vimage/buffertype/rgbgreen.md)
  The buffer contains the green channel.
- [vImage.BufferType.rgbRed](vimage/buffertype/rgbred.md)
  The buffer contains the red channel.
- [vImage.BufferType.xyzX](vimage/buffertype/xyzx.md)
  The buffer contains the `X` channel.
- [vImage.BufferType.xyzY](vimage/buffertype/xyzy.md)
  The buffer contains the `Y` channel.
- [vImage.BufferType.xyzZ](vimage/buffertype/xyzz.md)
  The buffer contains the `Z` channel.
### Buffer Type Properties
- [var bufferTypeCode: vImageBufferTypeCode](vimage/buffertype/buffertypecode.md)
  The type code of the buffer type.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)

## See Also

- [vImage.BlendMode](vimage/blendmode.md)
  Constants that specify an alpha blending mode.
- [vImage.ChannelOrdering](vimage/channelordering.md)
  Constants that specify the channel ordering of a pixel buffer.
- [vImage.CompositeMode](vimage/compositemode.md)
  Constants that specify whether the format of layers is premultiplied or nonpremultiplied.
- [vImage.EdgeMode](vimage/edgemode.md)
  Constants that specify edge modes for convolution operations.
- [vImage.Error](vimage/error.md)
  An error that occurs during a vImage operation.
- [vImage.FloodFillConnectivity](vimage/floodfillconnectivity.md)
- [vImage.Gamma](vimage/gamma.md)
  Describes either a used-defined or constant gamma.
- [vImage.MorphologyOperation](vimage/morphologyoperation.md)
  Describes which morphology operation to perform.
- [vImage.ReflectionAxis](vimage/reflectionaxis.md)
  The axis to reflect an image.
- [vImage.Rotation](vimage/rotation.md)
  The angle to rotate an image.
- [vImage.ShearDirection](vimage/sheardirection.md)
  The shear direction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/buffertype)*