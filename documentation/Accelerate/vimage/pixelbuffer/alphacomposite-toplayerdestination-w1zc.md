# alphaComposite(_:topLayer:destination:)

**Framework**: Accelerate  
**Kind**: method

Performs alpha compositing of two 4-channel interleaved ARGB 32-bit pixel buffers using the specified composite mode.

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
func alphaComposite(_ compositeMode: vImage.CompositeMode<Pixel_F>, topLayer: vImage.PixelBuffer<Format>, destination: vImage.PixelBuffer<Format>)
```

#### Discussion

This function treats `self` as the bottom layer and both pixel buffers must have alpha as their first channel.

## Parameters

- `compositeMode`: The composite mode.
- `topLayer`: The composite top layer.
- `destination`: The destination pixel buffer.

## See Also

- [Compositing images with alpha blending](compositing-images-with-alpha-blending.md)
  Combine two images by using alpha blending to create a single output.
- [func alphaComposite(vImage.CompositeMode<Pixel_8>, topLayer: vImage.PixelBuffer<Format>, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/alphacomposite(_:toplayer:destination:)-fybo.md)
  Performs alpha compositing of two 4-channel interleaved ARGB 8-bit pixel buffers using the specified composite mode.
- [vImage.CompositeMode](vimage/compositemode.md)
  Constants that specify whether the format of layers is premultiplied or nonpremultiplied.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/alphacomposite(_:toplayer:destination:)-w1zc)*