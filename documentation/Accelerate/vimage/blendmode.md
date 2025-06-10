# vImage.BlendMode

**Framework**: Accelerate  
**Kind**: enum

Constants that specify an alpha blending mode.

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
enum BlendMode
```

## Topics

### Enumeration Cases
- [vImage.BlendMode.darken](vimage/blendmode/darken.md)
  Sets each channel of the destination pixel as the darkest value for the corresponding channel of the two source layers.
- [vImage.BlendMode.lighten](vimage/blendmode/lighten.md)
  Sets each channel of the destination pixel as the lightest value for the corresponding channel of the two source layers
- [vImage.BlendMode.multiply](vimage/blendmode/multiply.md)
  Sets the destination pixel as the product of the corresponding source pixels.
- [vImage.BlendMode.screen](vimage/blendmode/screen.md)
  Sets the destination pixel as the inverted product of the inverted corresponding source pixels.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [Compositing images with alpha blending](compositing-images-with-alpha-blending.md)
  Combine two images by using alpha blending to create a single output.
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

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/blendmode)*