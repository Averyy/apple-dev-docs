# vImage.BlendMode.multiply

**Framework**: Accelerate  
**Kind**: case

Sets the destination pixel as the product of the corresponding source pixels.

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
case multiply
```

#### Discussion

The following image shows the result of compositing using the multiply blend mode:

![Graphic showing the multiply blend mode composite operation.](https://docs-assets.developer.apple.com/published/621f96b00e4e06cb86e86045ac707912/media-3958278%402x.png)

The bottom-right quadrant in the result is black because the operation multiplies each bottom-layer pixel value by `0.0` from the top layer.

The top-left quadrant in the result is identical to the corresponding quadrant in the bottom layer because the operation multiplies each bottom-layer pixel value by `1.0`.

The top-right quadrant in the result is darker than the corresponding quadrant in the bottom layer. In this quadrant, the top-layer and bottom-layer pixel values are identical. For example, if the source pixel value is 0.5, the destination pixel value is `0.25`:

```swift
dest = 0.5 * 0.5 // dest = 0.25
```

## See Also

- [Compositing images with alpha blending](compositing-images-with-alpha-blending.md)
  Combine two images by using alpha blending to create a single output.
- [vImage.BlendMode.darken](vimage/blendmode/darken.md)
  Sets each channel of the destination pixel as the darkest value for the corresponding channel of the two source layers.
- [vImage.BlendMode.lighten](vimage/blendmode/lighten.md)
  Sets each channel of the destination pixel as the lightest value for the corresponding channel of the two source layers
- [vImage.BlendMode.screen](vimage/blendmode/screen.md)
  Sets the destination pixel as the inverted product of the inverted corresponding source pixels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/blendmode/multiply)*