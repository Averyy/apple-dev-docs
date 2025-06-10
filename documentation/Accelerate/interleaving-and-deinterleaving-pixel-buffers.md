# Interleaving and deinterleaving pixel buffers

**Framework**: Accelerate

Convert pixel buffer data between interleaved and planar formats.

## Topics

### Deinterleaving pixel buffers
- [func deinterleave(destination: vImage.PixelBuffer<vImage.Planar8x3>)](vimage/pixelbuffer/deinterleave(destination:)-hrhz.md)
  Deinterleaves the 8-bit-per-channel, three-channel interleaved buffer and writes the result to a multiple-plane pixel buffer.
- [func deinterleave(destination: vImage.PixelBuffer<vImage.Planar8x4>)](vimage/pixelbuffer/deinterleave(destination:)-4bj4f.md)
  Deinterleaves the 8-bit-per-channel, four-channel interleaved buffer and writes the result to a multiple-plane pixel buffer.
- [func deinterleave(destination: vImage.PixelBuffer<vImage.PlanarFx3>)](vimage/pixelbuffer/deinterleave(destination:)-9gkke.md)
  Deinterleaves the 32-bit-per-channel, three-channel interleaved buffer and writes the result to a multiple-plane pixel buffer.
- [func deinterleave(destination: vImage.PixelBuffer<vImage.PlanarFx4>)](vimage/pixelbuffer/deinterleave(destination:)-7hep3.md)
  Deinterleaves the 32-bit-per-channel, four-channel interleaved buffer and writes the result to a multiple-plane pixel buffer.
- [func deinterleave(planarDestinationBuffers: [vImage.PixelBuffer<vImage.Planar8>])](vimage/pixelbuffer/deinterleave(planardestinationbuffers:)-72108.md)
  Deinterleaves the 8-bit-per-channel, three-channel interleaved buffer and writes the result to an array that contains three planar buffers.
- [func deinterleave(planarDestinationBuffers: [vImage.PixelBuffer<vImage.Planar8>])](vimage/pixelbuffer/deinterleave(planardestinationbuffers:)-3u4kn.md)
  Deinterleaves the 8-bit-per-channel, four-channel interleaved buffer and writes the result to an array that contains four planar buffers.
- [func deinterleave(planarDestinationBuffers: [vImage.PixelBuffer<vImage.Planar16F>])](vimage/pixelbuffer/deinterleave(planardestinationbuffers:)-75uki.md)
  Deinterleaves the 16-bit-per-channel, four-channel interleaved buffer and writes the result to an array that contains four planar buffers.
- [func deinterleave(planarDestinationBuffers: [vImage.PixelBuffer<vImage.Planar16U>])](vimage/pixelbuffer/deinterleave(planardestinationbuffers:)-3irjf.md)
  Deinterleaves the unsigned 16-bit-per-channel, four-channel interleaved buffer and writes the result to an array that contains four planar buffers.
- [func deinterleave(planarDestinationBuffers: [vImage.PixelBuffer<vImage.PlanarF>])](vimage/pixelbuffer/deinterleave(planardestinationbuffers:)-2gt2g.md)
  Deinterleaves the 32-bit-per-channel, three-channel interleaved buffer and writes the result to an array that contains three planar buffers.
- [func deinterleave(planarDestinationBuffers: [vImage.PixelBuffer<vImage.PlanarF>])](vimage/pixelbuffer/deinterleave(planardestinationbuffers:)-iag8.md)
  Deinterleaves the 32-bit-per-channel, four-channel interleaved buffer and writes the result to an array that contains four planar buffers.
### Interleaving pixel buffers
- [func interleave(destination: vImage.PixelBuffer<vImage.Interleaved8x3>)](vimage/pixelbuffer/interleave(destination:)-46cgi.md)
  Interleaves the 8-bit-per-channel, three-channel multiple-plane buffer and writes the result to an interleaved pixel buffer.
- [func interleave(destination: vImage.PixelBuffer<vImage.Interleaved8x4>)](vimage/pixelbuffer/interleave(destination:)-6r7se.md)
  Interleaves the 8-bit-per-channel, four-channel multiple-plane buffer and writes the result to an interleaved pixel buffer.
- [func interleave(destination: vImage.PixelBuffer<vImage.InterleavedFx3>)](vimage/pixelbuffer/interleave(destination:)-5ewup.md)
  Interleaves the 32-bit-per-channel, three-channel multiple-plane buffer and writes the result to an interleaved pixel buffer.
- [func interleave(destination: vImage.PixelBuffer<vImage.InterleavedFx4>)](vimage/pixelbuffer/interleave(destination:)-6ib0t.md)
  Interleaves the 32-bit-per-channel, four-channel multiple-plane buffer and writes the result to an interleaved pixel buffer.
- [func interleave(planarSourceBuffers: [vImage.PixelBuffer<vImage.Planar8>])](vimage/pixelbuffer/interleave(planarsourcebuffers:)-10yj5.md)
  Interleaves the specified planar source buffers and writes the result to the 8-bit-per-channel, three-channel interleaved buffer.
- [func interleave(planarSourceBuffers: [vImage.PixelBuffer<vImage.Planar8>])](vimage/pixelbuffer/interleave(planarsourcebuffers:)-67l5.md)
  Interleaves the specified planar source buffers and writes the result to the 8-bit-per-channel, four-channel interleaved buffer.
- [func interleave(planarSourceBuffers: [vImage.PixelBuffer<vImage.Planar16F>])](vimage/pixelbuffer/interleave(planarsourcebuffers:)-7qcri.md)
  Interleaves the specified planar source buffers and writes the result to the 16-bit-per-channel, four-channel interleaved buffer.
- [func interleave(planarSourceBuffers: [vImage.PixelBuffer<vImage.Planar16U>])](vimage/pixelbuffer/interleave(planarsourcebuffers:)-1i8we.md)
  Interleaves the specified planar source buffers and writes the result to the unsigned 16-bit-per-channel, four-channel interleaved buffer.
- [func interleave(planarSourceBuffers: [vImage.PixelBuffer<vImage.PlanarF>])](vimage/pixelbuffer/interleave(planarsourcebuffers:)-4qotd.md)
  Interleaves the specified planar source buffers and writes the result to the 32-bit-per-channel, three-channel interleaved buffer.
- [func interleave(planarSourceBuffers: [vImage.PixelBuffer<vImage.PlanarF>])](vimage/pixelbuffer/interleave(planarsourcebuffers:)-7e6cy.md)
  Interleaves the specified planar source buffers and writes the result to the 32-bit-per-channel, four-channel interleaved buffer.
### Generating planar buffers from interleaved buffers
- [func planarBuffers() -> [vImage.PixelBuffer<vImage.Planar8>]](vimage/pixelbuffer/planarbuffers-462ja.md)
  Returns two 8-bit planar pixel buffers that contain the deinterleaved channels of the buffer.
- [func planarBuffers() -> [vImage.PixelBuffer<vImage.Planar8>]](vimage/pixelbuffer/planarbuffers-5r3ds.md)
  Returns three 8-bit planar pixel buffers that contain the deinterleaved channels of the buffer.
- [func planarBuffers() -> [vImage.PixelBuffer<vImage.Planar8>]](vimage/pixelbuffer/planarbuffers-5rx2w.md)
  Returns four 8-bit planar pixel buffers that contain the deinterleaved channels of the buffer.
- [func planarBuffers() -> [vImage.PixelBuffer<vImage.PlanarF>]](vimage/pixelbuffer/planarbuffers-4qws5.md)
  Returns four 32-bit planar pixel buffers that contain the deinterleaved channels of the 8-bit buffer.
- [func planarBuffers() -> [vImage.PixelBuffer<vImage.Planar16U>]](vimage/pixelbuffer/planarbuffers-49gf9.md)
  Returns four unsigned 16-bit planar pixel buffers that contain the deinterleaved channels of the buffer.
- [func planarBuffers() -> [vImage.PixelBuffer<vImage.PlanarF>]](vimage/pixelbuffer/planarbuffers-1rj01.md)
  Returns two 32-bit planar pixel buffers that contain the deinterleaved channels of the buffer.
- [func planarBuffers() -> [vImage.PixelBuffer<vImage.PlanarF>]](vimage/pixelbuffer/planarbuffers-82ook.md)
  Returns three 32-bit planar pixel buffers that contain the deinterleaved channels of the buffer.
- [func planarBuffers() -> [vImage.PixelBuffer<vImage.Planar8>]](vimage/pixelbuffer/planarbuffers-l33r.md)
  Returns four 8-bit planar pixel buffers that contain the deinterleaved channels of the 32-bit buffer.
- [func planarBuffers() -> [vImage.PixelBuffer<vImage.PlanarF>]](vimage/pixelbuffer/planarbuffers-35dnv.md)
  Returns four 32-bit planar pixel buffers that contain the deinterleaved channels of the buffer.
### Converting from 8-bit multiple plane to 8-bit interleaved
- [func convert(to: vImage.PixelBuffer<vImage.Interleaved8x3>)](vimage/pixelbuffer/convert(to:)-7xv7.md)
  Converts the contents of an 8-bit, three-plane pixel buffer to a three-channel interleaved pixel buffer.
- [func convert(to: vImage.PixelBuffer<vImage.Interleaved8x4>)](vimage/pixelbuffer/convert(to:)-1jtfh.md)
  Converts the contents of an 8-bit, four-plane pixel buffer to a four-channel interleaved pixel buffer.
### Converting from 32-bit multiple plane to 32-bit interleaved
- [func convert(to: vImage.PixelBuffer<vImage.InterleavedFx3>)](vimage/pixelbuffer/convert(to:)-8bqjc.md)
  Converts the contents of a 32-bit, three-plane pixel buffer to a three-channel interleaved pixel buffer.
- [func convert(to: vImage.PixelBuffer<vImage.InterleavedFx4>)](vimage/pixelbuffer/convert(to:)-26s6v.md)
  Converts the contents of a 32-bit, four-plane pixel buffer to a four-channel interleaved pixel buffer.

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
- [Calculating and transforming histograms](calculating-and-transforming-histograms.md)
  Enhance and adjust the contrast of an image with histogram equalization, contrast stretching, and specification.
- [Converting pixel buffers](converting-pixel-buffers.md)
  Convert pixel buffer data between different bit-depths.
- [Cropping and working with regions of interest](cropping-and-working-with-regions-of-interest.md)
  Crop images and apply operations to regions of interest.
- [Applying channel operations](applying-channel-operations.md)
  Extract, flatten, permute, and overwrite the individual color channels of a pixel buffer.
- [Applying arithmetic operations](applying-arithmetic-operations.md)
  Multiply the pixel values of a buffer by scalar values or matrices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/interleaving-and-deinterleaving-pixel-buffers)*