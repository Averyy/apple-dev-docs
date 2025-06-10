# vImage.MorphologyOperation

**Framework**: Accelerate  
**Kind**: enum

Describes which morphology operation to perform.

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
enum MorphologyOperation<ComponentType>
```

## Topics

### Enumeration Cases
- [case dilate(structuringElement: vImage.ConvolutionKernel2D<ComponentType>)](vimage/morphologyoperation/dilate(structuringelement:).md)
  Applies dilation using a structuring element.
- [case erode(structuringElement: vImage.ConvolutionKernel2D<ComponentType>)](vimage/morphologyoperation/erode(structuringelement:).md)
  Applies erosion using a structuring element.
- [vImage.MorphologyOperation.maximize(kernelSize:)](vimage/morphologyoperation/maximize(kernelsize:).md)
  Maximizes using an implicit kernel of a specified size.
- [vImage.MorphologyOperation.minimize(kernelSize:)](vimage/morphologyoperation/minimize(kernelsize:).md)
  Minimizes using an implicit kernel of a specified size.
### Instance Properties
- [var structuringElement: vImage.ConvolutionKernel2D<ComponentType>?](vimage/morphologyoperation/structuringelement.md)
  The dilation or erosion structuring element.
- [var height: vImagePixelCount](vimage/morphologyoperation/height.md)
  The height of the morphology kernel.
- [var width: vImagePixelCount](vimage/morphologyoperation/width.md)
  The width of the morphology kernel.

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
- [vImage.Gamma](vimage/gamma.md)
  Describes either a used-defined or constant gamma.
- [vImage.ReflectionAxis](vimage/reflectionaxis.md)
  The axis to reflect an image.
- [vImage.Rotation](vimage/rotation.md)
  The angle to rotate an image.
- [vImage.ShearDirection](vimage/sheardirection.md)
  The shear direction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/morphologyoperation)*