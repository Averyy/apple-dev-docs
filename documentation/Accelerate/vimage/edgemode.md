# vImage.EdgeMode

**Framework**: Accelerate  
**Kind**: enum

Constants that specify edge modes for convolution operations.

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
enum EdgeMode<PixelType>
```

## Topics

### Enumeration Cases
- [vImage.EdgeMode.copyInPlace](vimage/edgemode/copyinplace.md)
  An edge mode that copies the value of the edge pixel in the source to the destination.
- [vImage.EdgeMode.extend](vimage/edgemode/extend.md)
  An edge mode that extends the edges of the image infinitely.
- [vImage.EdgeMode.fill(backgroundColor:)](vimage/edgemode/fill(backgroundcolor:).md)
  An edge mode that uses the background color for missing pixels.
- [vImage.EdgeMode.truncateKernel](vimage/edgemode/truncatekernel.md)
  An edge mode that uses only the part of the kernel that overlaps the image.

## See Also

- [vImage.BlendMode](vimage/blendmode.md)
  Constants that specify an alpha blending mode.
- [vImage.BufferType](vimage/buffertype.md)
  Codes that represent vImage buffer types.
- [vImage.ChannelOrdering](vimage/channelordering.md)
  Constants that specify the channel ordering of a pixel buffer.
- [vImage.CompositeMode](vimage/compositemode.md)
  Constants that specify whether the format of layers is premultiplied or nonpremultiplied.
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

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/edgemode)*