# vImage

**Framework**: Accelerate

Manipulate large images using the CPU’s vector processor.

#### Overview

vImage is a high-performance image processing framework. It includes functions for image manipulation—convolutions, geometric transformations, histogram operations, morphological transformations, and alpha compositing—as well as utility functions for format conversions and other operations.

vImage optimizes image processing by using the CPU’s vector processor. If a vector processor is not available, vImage uses the next best available option. This framework allows you to reap the benefits of vector processors without the need to write vectorized code.

vImage is particularly suited for:

- Efficiently processing large images
- Real-time video processing software
- Scientific applications that require high-accuracy numerical calculations

## Topics

### First Steps
- [Converting bitmap data between Core Graphics images and vImage buffers](converting-bitmap-data-between-core-graphics-images-and-vimage-buffers.md)
  Pass image data between Core Graphics and vImage to create and manipulate images.
- [Creating and Populating Buffers from Core Graphics Images](creating-and-populating-buffers-from-core-graphics-images.md)
  Initialize vImage buffers from Core Graphics images.
- [Creating a Core Graphics Image from a vImage Buffer](creating-a-core-graphics-image-from-a-vimage-buffer.md)
  Create displayable representations of vImage buffers.
- [Building a Basic Image-Processing Workflow](building-a-basic-image-processing-workflow.md)
  Resize an image with vImage.
- [Compositing images with alpha blending](compositing-images-with-alpha-blending.md)
  Combine two images by using alpha blending to create a single output.
- [Compositing images with vImage blend modes](compositing-images-with-vimage-blend-modes.md)
  Combine two images by using blend modes to create a single output.
- [Applying geometric transforms to images](applying-geometric-transforms-to-images.md)
  Reflect, shear, rotate, and scale image buffers using vImage.
- [Applying vImage operations to regions of interest](applying-vimage-operations-to-regions-of-interest.md)
  Limit the effect of vImage operations to rectangular regions of interest.
### Swift Overlay
- [enum vImage](vimage.md)
  An enumeration that acts as a namespace for Swift overlays to vImage.
### vImage Pixel Buffers
- [Using vImage pixel buffers to generate video effects](using-vimage-pixel-buffers-to-generate-video-effects.md)
  Render real-time video effects with the vImage Pixel Buffer.
- [Applying tone curve adjustments to images](applying-tone-curve-adjustments-to-images.md)
  Use the vImage library’s polynomial transform to apply tone curve adjustments to images.
- [Adjusting the brightness and contrast of an image](adjusting-the-brightness-and-contrast-of-an-image.md)
  Use a gamma function to apply a linear or exponential curve.
- [Adjusting the hue of an image](adjusting-the-hue-of-an-image.md)
  Convert an image to L*a*b* color space and apply hue adjustment.
- [Sharing texture data between the Model I/O framework and the vImage library](sharing-texture-data-between-the-model-io-framework-and-the-vimage-library.md)
  Use Model I/O and vImage to composite a photograph over a computer-generated sky.
- [Calculating the dominant colors in an image](calculating-the-dominant-colors-in-an-image.md)
  Find the main colors in an image by implementing k-means clustering using the Accelerate framework.
- [vImage.PixelBuffer](vimage/pixelbuffer.md)
  An image buffer that stores an image’s pixel data, dimensions, bit depth, and number of channels.
### vImage Buffers
- [Optimizing image-processing performance](optimizing-image-processing-performance.md)
  Improve your app’s performance by converting image buffer formats from interleaved to planar.
- [vImage buffers](vimage-buffers.md)
  Use buffers to pass image data to and from vImage operations.
### Core Graphics Interoperability
- [Core Graphics interoperability](core-graphics-interoperability.md)
  Pass image data between the Core Graphics framework and the vImage library.
### Core Video Interoperability
- [Integrating vImage pixel buffers into a Core Image workflow](integrating-vimage-pixel-buffers-into-a-core-image-workflow.md)
  Share image data between Core Video pixel buffers and vImage buffers to integrate vImage operations into a Core Image workflow.
- [Applying vImage operations to video sample buffers](applying-vimage-operations-to-video-sample-buffers.md)
  Use the vImage convert-any-to-any functionality to perform real-time image processing of video frames streamed from your device’s camera.
- [Converting luminance and chrominance planes to an ARGB image](converting-luminance-and-chrominance-planes-to-an-argb-image.md)
  Create a displayable ARGB image using the luminance and chrominance information from your device’s camera.
- [Improving the quality of quantized images with dithering](improving-the-quality-of-quantized-images-with-dithering.md)
  Apply dithering to simulate colors that are unavailable in reduced bit depths.
- [Core Video interoperability](core-video-interoperability.md)
  Pass image data between Core Video and vImage.
### vImage Operations
- [Adjusting saturation and applying tone mapping](adjusting-saturation-and-applying-tone-mapping.md)
  Convert an RGB image to discrete luminance and chrominance channels, and apply color and contrast treatments.
- [Blurring an image](blurring-an-image.md)
  Filter an image by convolving it with custom and high-speed kernels.
- [Adding a bokeh effect to images](adding-a-bokeh-effect-to-images.md)
  Simulate a bokeh effect by applying dilation.
- [Converting color images to grayscale](converting-color-images-to-grayscale.md)
  Convert an RGB image to grayscale using matrix multiplication.
- [Building a basic image conversion workflow](building-a-basic-image-conversion-workflow.md)
  Learn the fundamentals of the convert-any-to-any function by converting a CMYK image to an RGB image.
- [Specifying histograms with vImage](specifying-histograms-with-vimage.md)
  Calculate the histogram of one image, and apply it to a second image.
- [Enhancing image contrast with histogram manipulation](enhancing-image-contrast-with-histogram-manipulation.md)
  Enhance and adjust the contrast of an image with histogram equalization and contrast stretching.
- [Reducing artifacts with custom resampling filters](reducing-artifacts-with-custom-resampling-filters.md)
  Implement custom linear interpolation to prevent the ringing effects associated with scaling an image with the default Lanczos algorithm.
- [Finding the sharpest image in a sequence of captured images](finding-the-sharpest-image-in-a-sequence-of-captured-images.md)
  Share image data between vDSP and vImage to compute the sharpest image from a bracketed photo sequence.
- [vImage Operations](vimage-operations.md)
  Apply image manipulation operations to vImage buffers.
### Data Types and Constants
- [Data Types and Constants](data-types-and-constants.md)
  Look up type aliases, data types, and constants the vImage library uses.
### Macros
- [vImage Macros](vimage-macros.md)

## See Also

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
- [Compositing images with vImage blend modes](compositing-images-with-vimage-blend-modes.md)
  Combine two images by using blend modes to create a single output.
- [Applying vImage operations to regions of interest](applying-vimage-operations-to-regions-of-interest.md)
  Limit the effect of vImage operations to rectangular regions of interest.
- [Optimizing image-processing performance](optimizing-image-processing-performance.md)
  Improve your app’s performance by converting image buffer formats from interleaved to planar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage-library)*