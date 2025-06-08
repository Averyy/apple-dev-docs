# Creating a Core Graphics Image from a vImage Buffer

**Framework**: Accelerate

Create displayable representations of vImage buffers.

#### Overview

vImage provides a function for creating Core Graphics images from vImage buffers. This function allows you to display the results of a vImage operation to your user.

##### Create the Image

You create a Core Graphics image from the buffer, and initialize a [`UIImage`](https://developer.apple.com/documentation/UIKit/UIImage) instance from that. The [`createCGImage(format:flags:)`](vimage_buffer/createcgimage(format:flags:).md) function returns a [`CGImage`](https://developer.apple.com/documentation/CoreGraphics/CGImage) instance based on the supplied Core Graphics image format (for more information, see [`Converting bitmap data between Core Graphics images and vImage buffers`](converting-bitmap-data-between-core-graphics-images-and-vimage-buffers.md)).

The following example shows how to create a Core Graphics image from a vImage buffer:

```swift
let result = try? destinationBuffer.createCGImage(format: format)

if let result = result {
    // Assumes `imageView` is a `UIImageView`
    imageView.image = UIImage(cgImage: result)
}
```

## See Also

- [Converting bitmap data between Core Graphics images and vImage buffers](converting-bitmap-data-between-core-graphics-images-and-vimage-buffers.md)
  Pass image data between Core Graphics and vImage to create and manipulate images.
- [Creating and Populating Buffers from Core Graphics Images](creating-and-populating-buffers-from-core-graphics-images.md)
  Initialize vImage buffers from Core Graphics images.
- [Building a Basic Image-Processing Workflow](building-a-basic-image-processing-workflow.md)
  Resize an image with vImage.
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

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/creating-a-core-graphics-image-from-a-vimage-buffer)*