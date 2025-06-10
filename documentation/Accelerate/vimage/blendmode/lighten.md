# vImage.BlendMode.lighten

**Framework**: Accelerate  
**Kind**: case

Sets each channel of the destination pixel as the lightest value for the corresponding channel of the two source layers

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
case lighten
```

#### Discussion

The following image shows the result of compositing using the lighten blend mode:

![Graphic showing the lighten blend mode composite operation.](https://docs-assets.developer.apple.com/published/2eb6c157289d94e6fc5c6b2f023df06e/media-3958276%402x.png)

The top-left quadrant in the result is white because no pixels in the bottom layer are brighter than the corresponding pixels in the top layer.

The bottom-left quadrant in the result looks washed out because the operation selects gray pixels from the top layer over corresponding dark pixels from the bottom layer.

## See Also

- [Compositing images with alpha blending](compositing-images-with-alpha-blending.md)
  Combine two images by using alpha blending to create a single output.
- [vImage.BlendMode.darken](vimage/blendmode/darken.md)
  Sets each channel of the destination pixel as the darkest value for the corresponding channel of the two source layers.
- [vImage.BlendMode.multiply](vimage/blendmode/multiply.md)
  Sets the destination pixel as the product of the corresponding source pixels.
- [vImage.BlendMode.screen](vimage/blendmode/screen.md)
  Sets the destination pixel as the inverted product of the inverted corresponding source pixels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/blendmode/lighten)*