# Enhancing image contrast with histogram manipulation

**Framework**: Accelerate

Enhance and adjust the contrast of an image with histogram equalization and contrast stretching.

#### Overview

An image histogram is a representation of an image that describes its color tones distribution. The histogram contains a series of bins that represent the possible values for each color channel. For example, each channel of an 8-bit image contains 256 histogram bins. Each bin contains the image’s pixel count of the corresponding value.

The histogram of the following low-contrast image shows that almost all of its pixel values are clustered around the mid values. There are no pixels on the left side — corresponding to low values — indicating the image doesn’t contain any very dark colors. Similarly, there are no pixels on the right side — corresponding to high values — indicating the images doesn’t contain any very bright colors. The thin, gray line shows the cumulative histogram, that is, a running sum of pixel counts at each intensity.

![Two side-by-side images showing a low-contrast photograph of a landscape and a chart that represents the photograph’s histogram. The vertical peaks in the chart are clustered around the horizontal center. The continous line that represents the cumulative histogram is flat at either side and sloped in the center.](https://docs-assets.developer.apple.com/published/026ed33c3a890553662e0f2c19e72dc2/media-3702117%402x.png)

vImage provides functions that can either equalize or stretch an image’s histogram to enhance the contrast of an image.

##### Apply Histogram Equalization to an Image

Histogram equalization transforms an image so that its histogram is more uniformly distributed across the entire range of values. The operation stretches dense parts of the histogram, where contrast is low, and condenses sparse parts of the histogram, where contrast is high. A truly uniform histogram is one in which each histogram bin contains the same value, that is, its cumulative histogram is a diagonal line. The vImage histogram equalization functions approximate that truly uniform histogram.

The following code shows how to perform histogram equalization for [`vImage_Buffer`](vimage_buffer.md) and [`vImage.PixelBuffer`](vimage/pixelbuffer.md) structures:

```swift
// vImage buffer histogram equalization.
do {
    var sourceBuffer: vImage_Buffer = ...
    var destinationBuffer: vImage_Buffer = ...
    
    vImageEqualization_ARGB8888(&sourceBuffer,
                                &destinationBuffer,
                                vImage_Flags(kvImageNoFlags))
}

// vImage pixel buffer histogram equalization.
do {
    let sourceBuffer: vImage.PixelBuffer<vImage.Interleaved8x4> = ...
    let destinationBuffer: vImage.PixelBuffer<vImage.Interleaved8x4> = ...
    
    sourceBuffer.equalizeHistogram(destination: destinationBuffer)
}
```

On return, `destinationBuffer` contains the transformed image. The picture below shows the low-contrast image after histogram equalization. The operation distributed the nonzero histogram bins across the entire range of values, and the result has a lot more contrast. The cumulative histogram is nearly a straight diagonal line, indicating an almost uniform distribution of values.

![Two side-by-side images showing a very high-contrast photograph of a landscape and a chart that represents the photograph’s histogram. The vertical peaks in the chart are unevenly distributed across the length of the chart. The continous line that represents the cumulative histogram follows the diagonal line from the bottom left to the top right of the chart.](https://docs-assets.developer.apple.com/published/0c3cc43be6656d5a56b6f83810e34685/media-3702119%402x.png)

Note that the histogram bins aren’t evenly distributed throughout the resulting histogram. The amount of stretching correlates to the number of pixels in each bin.

##### Apply Contrast Stretching to an Image

Contrast stretching evenly distributes a histogram’s pixel values across the full range of available pixel values. This technique is ideal for enhancing the contrast of an image with pixel values concentrated in one area of the intensity spectrum, such as the original low-contrast image above.

The following code shows how to perform contrast stretching for [`vImage_Buffer`](vimage_buffer.md) and [`vImage.PixelBuffer`](vimage/pixelbuffer.md) structures:

```swift
// vImage buffer contrast stretching.
do {
    var sourceBuffer: vImage_Buffer = ...
    var destinationBuffer: vImage_Buffer = ...
    
    vImageContrastStretch_ARGB8888(&sourceBuffer,
                                   &destinationBuffer,
                                   vImage_Flags(kvImageNoFlags))
}

// vImage pixel buffer contrast stretching.
do {
    let sourceBuffer: vImage.PixelBuffer<vImage.Interleaved8x4> = ...
    let destinationBuffer: vImage.PixelBuffer<vImage.Interleaved8x4> = ...
    
    sourceBuffer.contrastStretch(destination: destinationBuffer)
}
```

On return, `destinationBuffer` contains the transformed image. The picture below shows the low-contrast image after histogram stretching. The result has a lot more contrast, and its histogram shows that values are evenly distributed throughout the entire range. The shape of the contrast stretched image’s cumulative histogram is very similar to the original image’s cumulative histogram.

![Two side-by-side images show a high-contrast photograph of a landscape and a chart that represents the photograph’s histogram. The vertical peaks in the chart are evenly distributed across the length of the chart. The continous line that represents the cumulative histogram rises where the histogram values are high and is flat where the histogram values are low. ](https://docs-assets.developer.apple.com/published/6100f359911acdd9850bf018f7a3e2b3/media-3702118%402x.png)

##### Apply Ends in Contrast Stretching to an Image

The vImage ends-in contrast stretching functions accept parameters that allow you to control which part of the histogram the operation stretches. Use ends-in contrast stretching for images with the majority of their pixels clustered in a single area and a small number of pixels at either end of their histogram. In these situations, standard contrast stretching may not yield your desired result.

The following figure illustrates how ends-in contrast stretching discards elements from a histogram and stretches the remaining values. The operation maps the 25% low values and 25% high values to 0 and 255 (for an 8-bit image), respectively. The result contains the central 50% of the source histogram stretched to fill the remaining 254 bins.

![Two stacked graphics representing histograms before and after applying ends-in contrast stretching. The original histogram that’s displayed in the top graphic is split 25% - 50% - 25%. The transformed original histogram that’s displayed in the bottom graphic contains the middle 50% of the original  but stretched to its full width.](https://docs-assets.developer.apple.com/published/5fcdfcdc0cf73c12cbc05b7c75d4a7bf/media-3723432%402x.png)

Note that this illustration isn’t to scale; the operation uses percentages based on the number of pixels for each intensity.

Set the `percent_low` parameter of the [`vImageEndsInContrastStretch_ARGB8888(_:_:_:_:_:)`](vimageendsincontraststretch_argb8888(_:_:_:_:_:).md) function to define the percentage of pixels that the operation maps to the lowest end of the transformed image’s histogram. The following code shows how to perform ends-in contrast stretching for [`vImage_Buffer`](vimage_buffer.md) and [`vImage.PixelBuffer`](vimage/pixelbuffer.md) structures with `percent_low` set to 25% for all channels:

```swift
// vImage buffer ends-in contrast stretching.
do {
    var sourceBuffer: vImage_Buffer = ...
    var destinationBuffer: vImage_Buffer = ...
    
    vImageEndsInContrastStretch_ARGB8888(&sourceBuffer,
                                         &destinationBuffer,
                                         [25, 25, 25, 25],
                                         [0, 0, 0, 0],
                                         vImage_Flags(kvImageNoFlags))
}

// vImage pixel buffer ends-in contrast stretching.
do {
    let sourceBuffer: vImage.PixelBuffer<vImage.Interleaved8x4> = ...
    let destinationBuffer: vImage.PixelBuffer<vImage.Interleaved8x4> = ...
    
    _ = sourceBuffer.withUnsafePointerToVImageBuffer { src in
        destinationBuffer.withUnsafePointerToVImageBuffer { dst in
            vImageEndsInContrastStretch_ARGB8888(src,
                                                 dst,
                                                 [25, 25, 25, 25],
                                                 [0, 0, 0, 0],
                                                 vImage_Flags(kvImageNoFlags))
        }
    }
}
 
```

On return, `destinationBuffer` contains the transformed image. The picture below shows the low-contrast image after ends-in contrast stretching. This result is much darker overall with the histogram shifted to the left.

![Two side-by-side images show a dark photograph of a landscape and a chart that represents the photograph’s histogram. The vertical peaks in the chart are clustered at the left side of the chart. The continous line that represents the cumulative histogram rises rapidly and flattens out where the histogram values are low.](https://docs-assets.developer.apple.com/published/4ddaf851a626d3fde67133153b8d16f3/media-3702115%402x.png)

Set the `percent_high` parameter of the [`vImageEndsInContrastStretch_ARGB8888(_:_:_:_:_:)`](vimageendsincontraststretch_argb8888(_:_:_:_:_:).md) function to define the percentage of pixels that the operation maps to the high end of the transformed image’s histogram. The following code shows how to perform ends-in contrast stretching for [`vImage_Buffer`](vimage_buffer.md) and [`vImage.PixelBuffer`](vimage/pixelbuffer.md) structures with `percent_high` set to 25% for all channels:

```swift
// vImage buffer ends-in contrast stretching.
do {
    var sourceBuffer: vImage_Buffer = ...
    var destinationBuffer: vImage_Buffer = ...
    
    vImageEndsInContrastStretch_ARGB8888(&sourceBuffer,
                                         &destinationBuffer,
                                         [0, 0, 0, 0],
                                         [25, 25, 25, 25],
                                         vImage_Flags(kvImageNoFlags))
}

// vImage pixel buffer ends-in contrast stretching.
do {
    let sourceBuffer: vImage.PixelBuffer<vImage.Interleaved8x4> = ...
    let destinationBuffer: vImage.PixelBuffer<vImage.Interleaved8x4> = ...
    
    _ = sourceBuffer.withUnsafePointerToVImageBuffer { src in
        destinationBuffer.withUnsafePointerToVImageBuffer { dst in
            vImageEndsInContrastStretch_ARGB8888(src,
                                                 dst,
                                                 [0, 0, 0, 0],
                                                 [25, 25, 25, 25],
                                                 vImage_Flags(kvImageNoFlags))
        }
    }
}
```

On return, `destinationBuffer` contains the transformed image. The picture below shows the low-contrast image after ends-in contrast stretching. This result is much brighter overall with the histogram shifted to the right.

![Two side-by-side images show a bright photograph of a landscape and a chart that represents the photograph’s histogram. The vertical peaks in the chart are clustered at the right side of the chart. The continous line that represents the cumulative histogram is mostly flat and rises where the histogram values are high.](https://docs-assets.developer.apple.com/published/a4740fd347ae650188fd01e1c0a56d16/media-3702116%402x.png)

## See Also

- [func equalizeHistogram(destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/equalizehistogram(destination:)-939xn.md)
  Equalizes the histogram of a multiple-plane 8-bit pixel buffer.
- [func contrastStretch(destination: vImage.PixelBuffer<vImage.Interleaved8x4>)](vimage/pixelbuffer/contraststretch(destination:)-7zo9.md)
  Stretches the histogram of an 8-bit-per-channel, 4-channel interleaved pixel buffer.
- [func vImageEqualization_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageequalization_argb8888(_:_:_:).md)
  Performs histogram equalization on an 8-bit-per-channel, 4-channel interleaved buffer.
- [func vImageContrastStretch_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagecontraststretch_argb8888(_:_:_:).md)
  Performs contrast stretching on an 8-bit-per-channel, 4-channel interleaved buffer.
- [func vImageEndsInContrastStretch_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<UInt32>, UnsafePointer<UInt32>, vImage_Flags) -> vImage_Error](vimageendsincontraststretch_argb8888(_:_:_:_:_:).md)
  Performs ends-in contrast stretching on an 8-bit-per-channel, 4-channel interleaved buffer.
- [Adjusting the brightness and contrast of an image](adjusting-the-brightness-and-contrast-of-an-image.md)
  Use a gamma function to apply a linear or exponential curve.
- [Adjusting saturation and applying tone mapping](adjusting-saturation-and-applying-tone-mapping.md)
  Convert an RGB image to discrete luminance and chrominance channels, and apply color and contrast treatments.
- [Applying tone curve adjustments to images](applying-tone-curve-adjustments-to-images.md)
  Use the vImage library’s polynomial transform to apply tone curve adjustments to images.
- [Adjusting the hue of an image](adjusting-the-hue-of-an-image.md)
  Convert an image to L*a*b* color space and apply hue adjustment.
- [Specifying histograms with vImage](specifying-histograms-with-vimage.md)
  Calculate the histogram of one image, and apply it to a second image.
- [Histogram](histogram.md)
  Calculate or manipulate an image’s histogram.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/enhancing-image-contrast-with-histogram-manipulation)*