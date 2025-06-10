# vImage.BlendMode.darken

**Framework**: Accelerate  
**Kind**: case

Sets each channel of the destination pixel as the darkest value for the corresponding channel of the two source layers.

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
case darken
```

#### Discussion

The following image shows the result of compositing using the darken blend mode:

![Graphic showing the darken blend mode composite operation.](https://docs-assets.developer.apple.com/published/676ec6eca727e59096f9b76c7971ecea/media-3958272%402x.png)

The bottom-right quadrant in the result is black because no pixels in the bottom layer are darker than the corresponding pixels in the top layer.

The bottom-left quadrant in the result looks darker than the corresponding quadrant in the bottom layer. This is because the operation selects gray pixels from the top layer over corresponding light pixels from the bottom layer.

## See Also

- [Compositing images with alpha blending](compositing-images-with-alpha-blending.md)
  Combine two images by using alpha blending to create a single output.
- [vImage.BlendMode.lighten](vimage/blendmode/lighten.md)
  Sets each channel of the destination pixel as the lightest value for the corresponding channel of the two source layers
- [vImage.BlendMode.multiply](vimage/blendmode/multiply.md)
  Sets the destination pixel as the product of the corresponding source pixels.
- [vImage.BlendMode.screen](vimage/blendmode/screen.md)
  Sets the destination pixel as the inverted product of the inverted corresponding source pixels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/blendmode/darken)*