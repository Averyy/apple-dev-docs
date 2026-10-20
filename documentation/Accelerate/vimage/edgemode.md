# vImage.EdgeMode

**Framework**: Accelerate  
**Kind**: enum  
**Role**: Enumeration

Constants that specify edge modes for convolution operations.

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
enum EdgeMode<PixelType>
```

## Topics

### Enumeration Cases
- [vImage.EdgeMode.copyInPlace](./edgemode/copyinplace.md)
  An edge mode that copies the value of the edge pixel in the source to the destination.
- [vImage.EdgeMode.extend](./edgemode/extend.md)
  An edge mode that extends the edges of the image infinitely.
- [vImage.EdgeMode.fill(backgroundColor:)](./edgemode/fill%28backgroundcolor%29.md)
  An edge mode that uses the background color for missing pixels.
- [vImage.EdgeMode.truncateKernel](./edgemode/truncatekernel.md)
  An edge mode that uses only the part of the kernel that overlaps the image.

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

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/edgemode)*