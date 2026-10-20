# vImage.BufferType

**Framework**: Accelerate  
**Kind**: enum  
**Role**: Enumeration

Codes that represent vImage buffer types.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS
- watchOS 6.0+

## Declaration

```swift
enum BufferType
```

## Topics

### Initializers
- [init?(bufferTypeCode: Int, model: CGColorSpaceModel?)](./buffertype/init%28buffertypecode,model%29.md)
  Creates a buffer type enumeration from the specified code and color space model.
### Enumeration Cases
- [vImage.BufferType.Cb](./buffertype/cb.md)
  The buffer contains the blue chrominance channel.
- [vImage.BufferType.Cr](./buffertype/cr.md)
  The buffer contains the red chrominance channel.
- [vImage.BufferType.YCbCr](./buffertype/ycbcr.md)
  The buffer contains interleaved luminance and both chroma channels.
- [vImage.BufferType.alpha](./buffertype/alpha.md)
  The buffer contains the alpha channel or coverage component.
- [vImage.BufferType.chroma](./buffertype/chroma.md)
  The buffer contains the interleaved chrominance channels.
- [vImage.BufferType.chunky](./buffertype/chunky.md)
  The buffer contains chunky data.
- [vImage.BufferType.cmykBlack](./buffertype/cmykblack.md)
  The buffer contains the black channel.
- [vImage.BufferType.cmykCyan](./buffertype/cmykcyan.md)
  The buffer contains the cyan channel.
- [vImage.BufferType.cmykMagenta](./buffertype/cmykmagenta.md)
  The buffer contains the magenta channel.
- [vImage.BufferType.cmykYellow](./buffertype/cmykyellow.md)
  The buffer contains the yellow channel.
- [vImage.BufferType.coreGraphics](./buffertype/coregraphics.md)
  The buffer contains a Core Graphics image.
- [vImage.BufferType.indexed](./buffertype/indexed.md)
  The buffer contains data in an indexed colorspace.
- [vImage.BufferType.labA](./buffertype/laba.md)
  The buffer contains the `a*` channel.
- [vImage.BufferType.labB](./buffertype/labb.md)
  The buffer contains the `b*` channel.
- [vImage.BufferType.labL](./buffertype/labl.md)
  The buffer contains the `L*` channel.
- [vImage.BufferType.luminance](./buffertype/luminance.md)
  The buffer contains only luminance data.
- [vImage.BufferType.monochrome](./buffertype/monochrome.md)
  The buffer contains monochrome data.
- [vImage.BufferType.rgbBlue](./buffertype/rgbblue.md)
  The buffer contains the blue channel.
- [vImage.BufferType.rgbGreen](./buffertype/rgbgreen.md)
  The buffer contains the green channel.
- [vImage.BufferType.rgbRed](./buffertype/rgbred.md)
  The buffer contains the red channel.
- [vImage.BufferType.xyzX](./buffertype/xyzx.md)
  The buffer contains the `X` channel.
- [vImage.BufferType.xyzY](./buffertype/xyzy.md)
  The buffer contains the `Y` channel.
- [vImage.BufferType.xyzZ](./buffertype/xyzz.md)
  The buffer contains the `Z` channel.
### Buffer Type Properties
- [var bufferTypeCode: vImageBufferTypeCode](./buffertype/buffertypecode.md)
  The type code of the buffer type.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)

## See Also

### Enumerations
- [vImage.BlendMode](./blendmode.md)
  Constants that specify an alpha blending mode.
- [vImage.ChannelOrdering](./channelordering.md)
  Constants that specify the channel ordering of a pixel buffer.
- [vImage.CompositeMode](./compositemode.md)
  Constants that specify whether the format of layers is premultiplied or nonpremultiplied.
- [vImage.EdgeMode](./edgemode.md)
  Constants that specify edge modes for convolution operations.
- [vImage.Error](./error.md)
  An error that occurs during a vImage operation.
- [vImage.FloodFillConnectivity](./floodfillconnectivity.md)
- [vImage.Gamma](./gamma.md)
  Describes either a used-defined or constant gamma.
- [vImage.MorphologyOperation](./morphologyoperation.md)
  Describes which morphology operation to perform.
- [vImage.ReflectionAxis](./reflectionaxis.md)
  The axis to reflect an image.
- [vImage.Rotation](./rotation.md)
  The angle to rotate an image.
- [vImage.ShearDirection](./sheardirection.md)
  The shear direction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/buffertype)*