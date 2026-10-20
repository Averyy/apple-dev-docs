# vImage.MorphologyOperation

**Framework**: Accelerate  
**Kind**: enum  
**Role**: Enumeration

Describes which morphology operation to perform.

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
enum MorphologyOperation<ComponentType>
```

## Topics

### Enumeration Cases
- [case dilate(structuringElement: vImage.ConvolutionKernel2D<ComponentType>)](./morphologyoperation/dilate%28structuringelement%29.md)
  Applies dilation using a structuring element.
- [case erode(structuringElement: vImage.ConvolutionKernel2D<ComponentType>)](./morphologyoperation/erode%28structuringelement%29.md)
  Applies erosion using a structuring element.
- [vImage.MorphologyOperation.maximize(kernelSize:)](./morphologyoperation/maximize%28kernelsize%29.md)
  Maximizes using an implicit kernel of a specified size.
- [vImage.MorphologyOperation.minimize(kernelSize:)](./morphologyoperation/minimize%28kernelsize%29.md)
  Minimizes using an implicit kernel of a specified size.
### Instance Properties
- [var structuringElement: vImage.ConvolutionKernel2D<ComponentType>?](./morphologyoperation/structuringelement.md)
  The dilation or erosion structuring element.
- [var height: vImagePixelCount](./morphologyoperation/height.md)
  The height of the morphology kernel.
- [var width: vImagePixelCount](./morphologyoperation/width.md)
  The width of the morphology kernel.

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
- [vImage.Gamma](./gamma.md)
  Describes either a used-defined or constant gamma.
- [vImage.ReflectionAxis](./reflectionaxis.md)
  The axis to reflect an image.
- [vImage.Rotation](./rotation.md)
  The angle to rotate an image.
- [vImage.ShearDirection](./sheardirection.md)
  The shear direction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/morphologyoperation)*