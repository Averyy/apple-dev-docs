# Building a Basic Image-Processing Workflow

**Framework**: Accelerate

Resize an image with vImage.

#### Overview

vImage provides fast and accurate high-level functions for image manipulation; for example, compositing, convolution, and histogram operations. It operates on common image formats through [`vImage_Buffer`](vimage_buffer.md) structures. vImage buffers describe the size of an image and the number of bytes in each row, and point to the image pixel data. Buffers are initialized from Core Graphics images, Core Video pixel buffers, or raw pixel data. The pixel data a buffer points to can be used to create a new Core Graphics image or can be copied into a Core Video pixel buffer.

In the simplest workflow, you convert an image to a vImage buffer, apply an operation to the buffer, and convert the buffer back to an image. In this example, the width and height of the result are one-third of the original:

![Photos showing the original image and the resized image.](https://docs-assets.developer.apple.com/published/af8011e648b6c8c2084e3a2e1d828ec0/media-2953430%402x.png)

##### Initialize an Image Format and Vimage Buffers

To learn about initializing the buffers you’ll need to perform a scaling operation, see [`Converting bitmap data between Core Graphics images and vImage buffers`](converting-bitmap-data-between-core-graphics-images-and-vimage-buffers.md) and [`Creating and Populating Buffers from Core Graphics Images`](creating-and-populating-buffers-from-core-graphics-images.md). In this example, you’ll need the image format and buffers discussed in [`Creating and Populating Buffers from Core Graphics Images`](creating-and-populating-buffers-from-core-graphics-images.md). However, you’ll use the following code to initialize a destination buffer with a height and width that are a quarter of the source dimensions.

```swift
let destinationHeight = Int(CGFloat(sourceBuffer.height) * 0.25)
let destinationWidth = Int(CGFloat(sourceBuffer.width) * 0.25)

guard var destinationBuffer = try? vImage_Buffer(width: destinationWidth,
                                                 height: destinationHeight,
                                                 bitsPerPixel: format.bitsPerPixel) else {
                                                    return nil
}

defer {
    destinationBuffer.free()
}
```

##### Apply the Scale Operation

If you’re rescaling an image with premultiplied alpha (that is, with a [`bitmapInfo`](vimage_cgimageformat/bitmapinfo.md) value with [`CGImageAlphaInfo.premultipliedFirst`](https://developer.apple.com/documentation/CoreGraphics/CGImageAlphaInfo/premultipliedFirst) or [`CGImageAlphaInfo.premultipliedLast`](https://developer.apple.com/documentation/CoreGraphics/CGImageAlphaInfo/premultipliedLast)), before you apply the scale operation, see [`Building a Basic Image-Processing Workflow`](building-a-basic-image-processing-workflow.md).

Otherwise, with the source and destination buffers properly initialized, you’re ready to perform the scaling operation. Because your format contains four 8-bit channels, you use the [`vImageScale_ARGB8888(_:_:_:_:)`](vimagescale_argb8888(_:_:_:_:).md) function. This function works equally well on all channel orderings; for example, RGBA or BGRA.

```swift
error = vImageScale_ARGB8888(&sourceBuffer,
                             &destinationBuffer,
                             nil,
                             vImage_Flags(kvImageHighQualityResampling))
        
guard error == kvImageNoError else {
    fatalError("Error in vImageScale_ARGB8888: \(error)")
}
```

The [`kvImageHighQualityResampling`](kvimagehighqualityresampling.md) flag uses a high-quality Lanczos 5 x 5 resampling filter. If you require faster scaling, pass [`kvImageNoFlags`](kvimagenoflags.md).

`destinationBuffer` now contains the scaled version of `sourceBuffer`. To learn how to display the scaled result to your user, see [`Creating a Core Graphics Image from a vImage Buffer`](creating-a-core-graphics-image-from-a-vimage-buffer.md).

After you’ve finished with the source and destination buffers, it’s important that you free the memory allocated to them:

```swift
sourceBuffer.free()
destinationBuffer.free()
```

##### Avoid Artifacts By Unpremultiplying

If you’re rescaling an image with premultiplied alpha, you may see artifacts in high-frequency regions of the image. To avoid this situation, unpremultiply the image data — that is, remove the premultiplied alpha value from the image data — before the scaling operation, and premultiply the scaled result.

This code shows the additional operations required, with error handling removed for brevity:

```swift
error = vImageUnpremultiplyData_ARGB8888(&sourceBuffer,
                                         &sourceBuffer,
                                         vImage_Flags(kvImageNoFlags))
 
error = vImageScale_ARGB8888(&sourceBuffer,
                             &destinationBuffer,
                             nil,
                             vImage_Flags(kvImageHighQualityResampling))
 
error = vImagePremultiplyData_ARGB8888(&destinationBuffer,
                                       &destinationBuffer,
                                       vImage_Flags(kvImageNoFlags))
```

## See Also

- [Converting bitmap data between Core Graphics images and vImage buffers](converting-bitmap-data-between-core-graphics-images-and-vimage-buffers.md)
  Pass image data between Core Graphics and vImage to create and manipulate images.
- [Creating and Populating Buffers from Core Graphics Images](creating-and-populating-buffers-from-core-graphics-images.md)
  Initialize vImage buffers from Core Graphics images.
- [Creating a Core Graphics Image from a vImage Buffer](creating-a-core-graphics-image-from-a-vimage-buffer.md)
  Create displayable representations of vImage buffers.
- [Applying geometric transforms to images](applying-geometric-transforms-to-images.md)
  Reflect, shear, rotate, and scale image buffers using vImage.
- [Compositing images with alpha blending](compositing-images-with-alpha-blending.md)
  Combine two images by using alpha blending to create a single output.
- [Compositing images with vImage blend modes](compositing-images-with-vimage-blend-modes.md)
  Combine two images by using blend modes to create a single output.
- [Applying vImage operations to regions of interest](applying-vimage-operations-to-regions-of-interest.md)
  Limit the effect of vImage operations to rectangular regions of interest.
- [Optimizing image-processing performance](optimizing-image-processing-performance.md)
  Improve your app’s performance by converting image buffer formats from interleaved to planar.
- [vImage](vimage-library.md)
  Manipulate large images using the CPU’s vector processor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/building-a-basic-image-processing-workflow)*