# Creating and Populating Buffers from Core Graphics Images

**Framework**: Accelerate

Initialize vImage buffers from Core Graphics images.

#### Overview

[`vImage_Buffer`](vimage_buffer.md) structures are the basic data structures that vImage uses for working with images. They describe an image’s dimensions and contain the pixel data that vImage routines operate on.

Typically, you’ll initialize a source buffer from an image and initialize and allocate a destination buffer to receive the result of a vImage operation.

##### Initialize a Source Buffer From a Core Graphics Image

The vImage functions that initialize a buffer’s size and data require an instantiated [`vImage_Buffer`](vimage_buffer.md) structure. Typically, you declare a buffer as a variable because these functions mutate the buffer.

You can initialize a vImage buffer from a [`CGImage`](https://developer.apple.com/documentation/CoreGraphics/CGImage) instance that’s acquired from the [`cgImage`](https://developer.apple.com/documentation/UIKit/UIImage/cgImage) property of an image. In the following example, the image is named `Flowers_2.jpg`. The [`init(cgImage:format:flags:)`](vimage_buffer/init(cgimage:format:flags:).md) function initializes a [`vImage_Buffer`](vimage_buffer.md) structure with the image data using the format discussed in [`Converting bitmap data between Core Graphics images and vImage buffers`](converting-bitmap-data-between-core-graphics-images-and-vimage-buffers.md).

```swift
guard
    let cgImage = UIImage(named: "Flowers_2.jpg")?.cgImage,
    var sourceBuffer = try? vImage_Buffer(cgImage: cgImage,
                                          format: format) else {
                                            return nil
}
```

##### Initialize and Allocate a Destination Buffer

Typically, in addition to creating a buffer to represent your source image, you create a destination buffer to receive the result of the vImage operation. In this case, you use the [`init(width:height:bitsPerPixel:)`](vimage_buffer/init(width:height:bitsperpixel:).md) function to initialize a buffer of a specified size and the correct memory allocation for the bit-depth of the image:

```swift
guard var destinationBuffer = try? vImage_Buffer(width: Int(sourceBuffer.width),
                                                 height: Int(sourceBuffer.height),
                                                 bitsPerPixel: format.bitsPerPixel) else {
                                                    return nil
}
```

##### Free the Buffer Memory

After you’re finished with buffers that have have their own memory allocation, it’s important that you free the memory allocated to them:

```swift
sourceBuffer.free()
destinationBuffer.free()
```

## See Also

- [Converting bitmap data between Core Graphics images and vImage buffers](converting-bitmap-data-between-core-graphics-images-and-vimage-buffers.md)
  Pass image data between Core Graphics and vImage to create and manipulate images.
- [Creating a Core Graphics Image from a vImage Buffer](creating-a-core-graphics-image-from-a-vimage-buffer.md)
  Create displayable representations of vImage buffers.
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

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/creating-and-populating-buffers-from-core-graphics-images)*