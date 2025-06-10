# Calculating and transforming histograms

**Framework**: Accelerate

Enhance and adjust the contrast of an image with histogram equalization, contrast stretching, and specification.

## Topics

### Contrast stretching
- [func contrastStretch(destination: vImage.PixelBuffer<vImage.Planar8>)](vimage/pixelbuffer/contraststretch(destination:)-6usbh.md)
  Stretches the histogram of an 8-bit planar pixel buffer.
- [func contrastStretch(binCount: Int, destination: vImage.PixelBuffer<vImage.PlanarF>)](vimage/pixelbuffer/contraststretch(bincount:destination:)-3bo13.md)
  Stretches the histogram of a 32-bit planar pixel buffer.
- [func contrastStretch(destination: vImage.PixelBuffer<vImage.Interleaved8x4>)](vimage/pixelbuffer/contraststretch(destination:)-7zo9.md)
  Stretches the histogram of an 8-bit-per-channel, 4-channel interleaved pixel buffer.
- [func contrastStretch(binCount: Int, destination: vImage.PixelBuffer<vImage.InterleavedFx4>)](vimage/pixelbuffer/contraststretch(bincount:destination:)-704t6.md)
  Stretches the histogram of a 32-bit-per-channel, 4-channel interleaved pixel buffer.
- [func contrastStretch(destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/contraststretch(destination:)-2nsx9.md)
  Stretches the histogram of a multiple-plane 8-bit pixel buffer.
- [func contrastStretch(binCount: Int, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/contraststretch(bincount:destination:)-81vq2.md)
  Stretches the histogram of a multiple-plane 32-bit pixel buffer.
### Equalization
- [func equalizeHistogram(destination: vImage.PixelBuffer<vImage.Planar8>)](vimage/pixelbuffer/equalizehistogram(destination:)-7temg.md)
  Equalizes the histogram of an 8-bit planar pixel buffer.
- [func equalizeHistogram(binCount: Int, destination: vImage.PixelBuffer<vImage.PlanarF>)](vimage/pixelbuffer/equalizehistogram(bincount:destination:)-5iv0q.md)
  Equalizes the histogram of a 32-bit planar pixel buffer.
- [func equalizeHistogram(destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/equalizehistogram(destination:)-2gbmf.md)
  Equalizes the histogram of an 8-bit-per-channel, 4-channel interleaved pixel buffer.
- [func equalizeHistogram(binCount: Int, destination: vImage.PixelBuffer<vImage.InterleavedFx4>)](vimage/pixelbuffer/equalizehistogram(bincount:destination:)-6on8w.md)
  Equalizes the histogram of a 32-bit-per-channel, 4-channel interleaved pixel buffer.
- [func equalizeHistogram(destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/equalizehistogram(destination:)-939xn.md)
  Equalizes the histogram of a multiple-plane 8-bit pixel buffer.
- [func equalizeHistogram(binCount: Int, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/equalizehistogram(bincount:destination:)-59li2.md)
  Equalizes the histogram of a multiple-plane 32-bit pixel buffer.
### Histogram calculation
- [func histogram() -> vImage.PixelBuffer<Format>.Histogram8888](vimage/pixelbuffer/histogram-14a38.md)
  Calculates the histogram of an 8-bit-per-channel, 4-channel interleaved pixel buffer.
- [func histogram(binCount: Int) -> vImage.PixelBuffer<Format>.HistogramFFFF](vimage/pixelbuffer/histogram(bincount:)-6pkfv.md)
  Calculates the histogram of a 32-bit-per-channel, 4-channel interleaved pixel buffer.
- [func histogram() -> vImage.PixelBuffer<Format>.Histogram888](vimage/pixelbuffer/histogram-30tsp.md)
  Calculates the histogram of an 8-bit-per-channel, 3-channel multiple-plane pixel buffer.
- [func histogram(binCount: Int) -> vImage.PixelBuffer<Format>.HistogramFFF](vimage/pixelbuffer/histogram(bincount:)-8wymg.md)
  Calculates the histogram of a 32-bit-per-channel, 3-channel multiple-plane pixel buffer.
- [func histogram() -> vImage.PixelBuffer<Format>.Histogram8888](vimage/pixelbuffer/histogram-6wxl5.md)
  Calculates the histogram of an 8-bit-per-channel, 4-channel multiple-plane pixel buffer.
- [func histogram(binCount: Int) -> vImage.PixelBuffer<Format>.HistogramFFFF](vimage/pixelbuffer/histogram(bincount:)-5bqka.md)
  Calculates the histogram of a 32-bit-per-channel, 4-channel multiple-plane pixel buffer.
### Histogram specification
- [func specifyHistogram(vImage.PixelBuffer<Format>.Histogram8888, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/specifyhistogram(_:destination:)-7xiz4.md)
  Performs a histogram specification operation on an 8-bit-per-channel, 4-channel interleaved pixel buffer.
- [func specifyHistogram(vImage.PixelBuffer<Format>.HistogramFFFF, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/specifyhistogram(_:destination:)-1x46n.md)
  Performs a histogram specification operation on a 32-bit-per-channel, 4-channel interleaved pixel buffer.
- [func specifyHistogram(vImage.PixelBuffer<Format>.Histogram888, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/specifyhistogram(_:destination:)-qeqr.md)
  Performs a histogram specification operation on an 8-bit-per-channel, 3-channel multiple-plane pixel buffer.
- [func specifyHistogram(vImage.PixelBuffer<Format>.HistogramFFF, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/specifyhistogram(_:destination:)-28844.md)
  Performs a histogram specification operation on a 32-bit-per-channel, 3-channel multiple-plane pixel buffer.
- [func specifyHistogram(vImage.PixelBuffer<Format>.Histogram8888, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/specifyhistogram(_:destination:)-73dpr.md)
  Performs a histogram specification operation on an 8-bit-per-channel, 4-channel multiple-plane pixel buffer.
- [func specifyHistogram(vImage.PixelBuffer<Format>.HistogramFFFF, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/specifyhistogram(_:destination:)-7cvk1.md)
  Performs a histogram specification operation on a 32-bit-per-channel, 3-channel multiple-plane pixel buffer.
### Type aliases
- [vImage.PixelBuffer.Histogram888](vimage/pixelbuffer/histogram888.md)
  The histogram for three channel 8-bit pixel buffers.
- [vImage.PixelBuffer.Histogram8888](vimage/pixelbuffer/histogram8888.md)
  The histogram for four channel 8-bit pixel buffers.
- [vImage.PixelBuffer.HistogramFFF](vimage/pixelbuffer/histogramfff.md)
  The histogram for three channel 32-bit pixel buffers.
- [vImage.PixelBuffer.HistogramFFFF](vimage/pixelbuffer/histogramffff.md)
  The histogram for four channel 32-bit pixel buffers.

## See Also

- [Applying geometric operations to pixel buffers](applying-geometric-operations-to-pixel-buffers.md)
  Reflect, shear, rotate, scale, and apply affine transforms to image data.
- [Applying color transforms to pixel buffers](applying-color-transforms-to-pixel-buffers.md)
  Adjust the colors of an image by applying gamma, polynomials, or multidimensional lookup.
- [Blending and compositing pixel buffers](blending-and-compositing-pixel-buffers.md)
  Composite two pixel buffers to create a single image.
- [Convolving and applying morphology](convolving-and-applying-morphology.md)
  Apply convolution, dilation, or erosion to a pixel buffer.
- [Thresholding and clipping pixel buffer values](thresholding-and-clipping-pixel-buffer-values.md)
  Limit the values in a pixel buffer to a threshold or a range.
- [Converting pixel buffers](converting-pixel-buffers.md)
  Convert pixel buffer data between different bit-depths.
- [Interleaving and deinterleaving pixel buffers](interleaving-and-deinterleaving-pixel-buffers.md)
  Convert pixel buffer data between interleaved and planar formats.
- [Cropping and working with regions of interest](cropping-and-working-with-regions-of-interest.md)
  Crop images and apply operations to regions of interest.
- [Applying channel operations](applying-channel-operations.md)
  Extract, flatten, permute, and overwrite the individual color channels of a pixel buffer.
- [Applying arithmetic operations](applying-arithmetic-operations.md)
  Multiply the pixel values of a buffer by scalar values or matrices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/calculating-and-transforming-histograms)*