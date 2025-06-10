# vImage.CompositeMode

**Framework**: Accelerate  
**Kind**: enum

Constants that specify whether the format of layers is premultiplied or nonpremultiplied.

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
enum CompositeMode<ComponentType>
```

## Topics

### Enumeration Cases
- [vImage.CompositeMode.nonpremultiplied](vimage/compositemode/nonpremultiplied.md)
  Composite two non-premultiplied images, to produce a non-premultiplied result.
- [vImage.CompositeMode.nonpremultipliedToPremultiplied](vimage/compositemode/nonpremultipliedtopremultiplied.md)
  Blends a nonpremultiplied top image into a premultiplied bottom image and returns a premultiplied result.
- [vImage.CompositeMode.premultiplied](vimage/compositemode/premultiplied.md)
  Blends two premultiplied images to produce a premultiplied result.
- [vImage.CompositeMode.premultipliedWithConstantAlpha(_:)](vimage/compositemode/premultipliedwithconstantalpha(_:).md)
  Performs premultiplied alpha compositing of two images, using a single alpha value for the entire image.

## See Also

- [Compositing images with alpha blending](compositing-images-with-alpha-blending.md)
  Combine two images by using alpha blending to create a single output.
- [vImage.BlendMode](vimage/blendmode.md)
  Constants that specify an alpha blending mode.
- [vImage.BufferType](vimage/buffertype.md)
  Codes that represent vImage buffer types.
- [vImage.ChannelOrdering](vimage/channelordering.md)
  Constants that specify the channel ordering of a pixel buffer.
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

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/compositemode)*