# Compositing images with vImage blend modes

**Framework**: Accelerate

Combine two images by using blend modes to create a single output.

#### Overview

vImage provides a suite of functions for compositing two source images into one output. These  functions implement different algorithms to determine the output color. For example, the multiply blend mode sets each output pixel as the product of the two corresponding input pixels.

The blend mode functions work on 8-bit RGBA source images in a premultiplied format. You can convert a nonpremultiplied buffer to a premultiplied format by using [`vImagePremultiplyData_RGBA8888(_:_:_:)`](vimagepremultiplydata_rgba8888(_:_:_:).md).

The blend mode functions accept two [`vImage_Buffer`](vimage_buffer.md) structures as the bottom and top layers of the compositing operation. The examples that follow use the image below on the left as the bottom layer and the image below on the right as the top layer.

![Two photographs. The photograph on the left is of a flower. The photograph on the right is separated into four quadrants containing white in the top left, gray in the bottom left, black in the bottom right, and content from the left photograph in the top right.](https://docs-assets.developer.apple.com/published/2d8955f150b7c31402869edb09e4c2aa/media-3685982%402x.png)

The top-layer source image consists of four sections:

- The top-left quadrant is solid white (`[255, 255, 255]`).
- The top-right quadrant is identical to the corresponding quadrant of the bottom image.
- The bottom-left quadrant is solid mid-gray (`[127, 127, 127]`).
- The bottom-right quadrant is solid black (`[0, 0, 0]`).

Both images are fully opaque.

##### Composite Images Using the Lighten Blend Mode

Use the [`vImagePremultipliedAlphaBlendLighten_RGBA8888(_:_:_:_:)`](vimagepremultipliedalphablendlighten_rgba8888(_:_:_:_:).md) function to composite two layers using the lighten blend mode. You can use the lighten blend mode to apply an overall lightening effect to images.

The lighten blend mode sets each channel of the destination pixel as the lightest value for the corresponding channel of the two source layers. The image below shows the result of compositing using the lighten blend mode:

![Three photographs. Two smaller photos are stacked on the left and an arrow points to a larger photograph on the right. The photograph on the bottom left is of a flower. The photograph on the top left is separated into four quadrants containing white in the top left, gray in the bottom left, black in the bottom right, and content from the bottom photograph in the top right. The photograph on the right is separated into four quadrants. The top-left quadrant is white, the bottom-left is a lighter version of the content from the smaller photograph on the bottom left, and the two right quadrants are the same as the corresponding quadrants of the smaller photograph on the bottom left.](https://docs-assets.developer.apple.com/published/2eb6c157289d94e6fc5c6b2f023df06e/media-3685983%402x.png)

The top-left quadrant in the result is white because no pixels in the bottom layer are brighter than the corresponding pixels in the top layer.

The bottom-left quadrant in the result looks washed out because the operation selects gray pixels from the top layer over corresponding dark pixels from the bottom layer.

##### Composite Images Using the Darken Blend Mode

Use the [`vImagePremultipliedAlphaBlendDarken_RGBA8888(_:_:_:_:)`](vimagepremultipliedalphablenddarken_rgba8888(_:_:_:_:).md) function to composite two layers using the darken blend mode. You can use the darken blend mode to apply an overall darkening effect to images.

The darken blend mode sets each channel of the destination pixel as the darkest value for the corresponding channel of the two source layers. The image below shows the result of compositing using the darken blend mode:

![Three photographs. Two smaller photos are stacked on the left and an arrow points to a larger photograph on the right. The photograph on the bottom left is of a flower. The photograph on the top left is separated into four quadrants containing white in the top left, gray in the bottom left, black in the bottom right, and content from the bottom photograph in the top right. The photograph on the right is separated into four quadrants. The bottom-right quadrant is black, the bottom-left is a darker version of the content from the smaller photograph on the bottom left, and the two top quadrants are the same as the corresponding quadrants of the smaller photograph on the bottom left.](https://docs-assets.developer.apple.com/published/676ec6eca727e59096f9b76c7971ecea/media-3685980%402x.png)

The bottom-right quadrant in the result is black because no pixels in the bottom layer are darker than the corresponding pixels in the top layer.

The bottom-left quadrant in the result looks darker than the corresponding quadrant in the bottom layer. This is because the operation selects gray pixels from the top layer over corresponding light pixels from the bottom layer.

##### Composite Images Using the Screen Blend Mode

Use the [`vImagePremultipliedAlphaBlendScreen_RGBA8888(_:_:_:_:)`](vimagepremultipliedalphablendscreen_rgba8888(_:_:_:_:).md) function to composite two layers using the screen blend mode. You can use the screen blend mode to lighten images without affecting the darkest areas.

The screen blend mode sets the destination pixel as the inverted product of the inverted corresponding source pixels. The image below shows the result of compositing using the screen blend mode:

![Three photographs. Two smaller photos are stacked on the left and an arrow points to a larger photo on the right. The photograph on the bottom left is of a flower. The photograph on the top left is separated into four quadrants containing white in the top left, gray in the bottom left, black in the bottom right, and content from the bottom photograph in the top right. The photograph on the right is separated into four quadrants. The top-left quadrant is white, the top-right is a brighter version of the content from the smaller photograph on the bottom left, the bottom-left is a lighter version of that photograph, and the bottom-right is the same as the corresponding quadrant of that photograph.](https://docs-assets.developer.apple.com/published/2fd6a53808292a212809da13ad8b8786/media-3685981%402x.png)

The bottom-right quadrant in the result is identical to the corresponding quadrant in the bottom layer because the operation multiplies each bottom-layer pixel value by `1.0`. For example, if the source pixel value is `0.5`, the destination pixel value is `0.5`.

```swift
dest = 1 - (1 - 0.5) * (1 - 0.0) // dest = 0.5
```

The top-right quadrant in the result is brighter than the corresponding quadrant in the bottom layer. In this quadrant, the top-layer and bottom-layer pixel values are identical. For example, if the source pixel value is `0.5`, the destination pixel value is `0.75`.

```swift
dest = 1 - (1 - 0.5) * (1 - 0.5) // dest = 0.75
```

##### Composite Images Using the Multiply Blend Mode

Use the [`vImagePremultipliedAlphaBlendMultiply_RGBA8888(_:_:_:_:)`](vimagepremultipliedalphablendmultiply_rgba8888(_:_:_:_:).md) function to composite two layers using the multiply blend mode. You can the use multiply blend mode to darken images without affecting the lightest areas.

The multiply blend mode sets the destination pixel as the product of the corresponding source pixels. The image below shows the result of compositing using the multiply blend mode:

![Three photographs. Two smaller photos are stacked on the left and an arrow points to a larger photo on the right. The photograph on the bottom left is of a flower. The photograph on the top left is separated into four quadrants containing white in the top left, gray in the bottom left, black in the bottom right, and content from the bottom photograph in the top right. The photograph on the right is separated into four quadrants. The bottom-right quadrant is black, the top-right and bottom-left are darker versions of the content from the smaller photograph on the bottom left, and the top-left is the same as the corresponding quadrant of that photograph.](https://docs-assets.developer.apple.com/published/621f96b00e4e06cb86e86045ac707912/media-3685984%402x.png)

The bottom-right quadrant in the result is black because the operation multiplies each bottom-layer pixel value by `0.0` from the top layer.

The top-left quadrant in the result is identical to the corresponding quadrant in the bottom layer because the operation multiplies each bottom-layer pixel value by `1.0`.

The top-right quadrant in the result is darker than the corresponding quadrant in the bottom layer. In this quadrant, the top-layer and bottom-layer pixel values are identical. For example, if the source pixel value is `0.5`, the destination pixel value is `0.25`.

```swift
dest = 0.5 * 0.5 // dest = 0.25
```

## See Also

- [Alpha compositing](alpha-compositing.md)
  Composite images together.
- [Converting bitmap data between Core Graphics images and vImage buffers](converting-bitmap-data-between-core-graphics-images-and-vimage-buffers.md)
  Pass image data between Core Graphics and vImage to create and manipulate images.
- [Creating and Populating Buffers from Core Graphics Images](creating-and-populating-buffers-from-core-graphics-images.md)
  Initialize vImage buffers from Core Graphics images.
- [Creating a Core Graphics Image from a vImage Buffer](creating-a-core-graphics-image-from-a-vimage-buffer.md)
  Create displayable representations of vImage buffers.
- [Building a Basic Image-Processing Workflow](building-a-basic-image-processing-workflow.md)
  Resize an image with vImage.
- [Applying geometric transforms to images](applying-geometric-transforms-to-images.md)
  Reflect, shear, rotate, and scale image buffers using vImage.
- [Compositing images with alpha blending](compositing-images-with-alpha-blending.md)
  Combine two images by using alpha blending to create a single output.
- [Applying vImage operations to regions of interest](applying-vimage-operations-to-regions-of-interest.md)
  Limit the effect of vImage operations to rectangular regions of interest.
- [Optimizing image-processing performance](optimizing-image-processing-performance.md)
  Improve your app’s performance by converting image buffer formats from interleaved to planar.
- [vImage](vimage-library.md)
  Manipulate large images using the CPU’s vector processor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/compositing-images-with-vimage-blend-modes)*