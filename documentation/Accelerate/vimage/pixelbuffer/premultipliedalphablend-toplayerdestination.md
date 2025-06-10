# premultipliedAlphaBlend(_:topLayer:destination:)

**Framework**: Accelerate  
**Kind**: method

Performs alpha compositing of two 4-channel interleaved RGBA 8-bit pixel buffers using the specified blend mode to produce a premultiplied result.

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
func premultipliedAlphaBlend(_ blendMode: vImage.BlendMode, topLayer: vImage.PixelBuffer<Format>, destination: vImage.PixelBuffer<Format>)
```

#### Discussion

This function treats `self` as the bottom layer and both pixel buffers must have alpha as their last channel.

## Parameters

- `blendMode`: The blend mode.
- `topLayer`: The blend top layer.
- `destination`: The destination pixel buffer.

## See Also

- [Compositing images with alpha blending](compositing-images-with-alpha-blending.md)
  Combine two images by using alpha blending to create a single output.
- [vImage.BlendMode](vimage/blendmode.md)
  Constants that specify an alpha blending mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/premultipliedalphablend(_:toplayer:destination:))*