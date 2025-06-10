# Applying color transforms to pixel buffers

**Framework**: Accelerate

Adjust the colors of an image by applying gamma, polynomials, or multidimensional lookup.

## Topics

### Applying gamma
- [func applyGamma(vImage.Gamma, intermediateBuffer: vImage.PixelBuffer<vImage.PlanarF>?, destination: vImage.PixelBuffer<vImage.Planar8>)](vimage/pixelbuffer/applygamma(_:intermediatebuffer:destination:)-1fif9.md)
  Applies a gamma function to an 8-bit planar pixel buffer.
- [func applyGamma(vImage.Gamma, intermediateBuffer: vImage.PixelBuffer<vImage.InterleavedFx2>?, destination: vImage.PixelBuffer<vImage.Interleaved8x2>)](vimage/pixelbuffer/applygamma(_:intermediatebuffer:destination:)-390k5.md)
  Applies a gamma function to an 8-bit-per-channel, 2-channel interleaved pixel buffer.
- [func applyGamma(vImage.Gamma, intermediateBuffer: vImage.PixelBuffer<vImage.InterleavedFx3>?, destination: vImage.PixelBuffer<vImage.Interleaved8x3>)](vimage/pixelbuffer/applygamma(_:intermediatebuffer:destination:)-3yu0w.md)
  Applies a gamma function to an 8-bit-per-channel, 3-channel interleaved pixel buffer.
- [func applyGamma(vImage.Gamma, intermediateBuffer: vImage.PixelBuffer<vImage.InterleavedFx4>?, destination: vImage.PixelBuffer<vImage.Interleaved8x4>)](vimage/pixelbuffer/applygamma(_:intermediatebuffer:destination:)-wsww.md)
  Applies a gamma function to an 8-bit-per-channel, 4-channel interleaved pixel buffer.
- [func applyGamma(vImage.Gamma, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/applygamma(_:destination:).md)
  Applies a gamma function to a 32-bit pixel buffer.
- [vImage.Gamma](vimage/gamma.md)
  Describes either a used-defined or constant gamma.
### Applying piecewise gamma
- [func applyGamma(linearParameters: (scale: Float, bias: Float), exponentialParameters: (scale: Float, preBias: Float, gamma: Float, postBias: Float), boundary: Pixel_8, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/applygamma(linearparameters:exponentialparameters:boundary:destination:)-249w5.md)
  Applies a piecewise gamma calculation to an 8-bit pixel buffer.
- [func applyGamma(linearParameters: (scale: Float, bias: Float), exponentialParameters: (scale: Float, preBias: Float, gamma: Float, postBias: Float), boundary: Float, destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/applygamma(linearparameters:exponentialparameters:boundary:destination:)-8r0ro.md)
  Applies a piecewise gamma calculation to a 32-bit pixel buffer.
### Appying polynomial (32-bit source, 8-bit destination)
- [func applyPolynomial(coefficientSegments: [[Float]], boundaries: [Float], destination: vImage.PixelBuffer<vImage.Planar8>)](vimage/pixelbuffer/applypolynomial(coefficientsegments:boundaries:destination:)-3b0d0.md)
  Applies a set of piecewise polynomials to a 32-bit planar buffer and writes the result to an 8-bit planar buffer.
- [func applyPolynomial(coefficientSegments: [[Float]], boundaries: [Float], destination: vImage.PixelBuffer<vImage.Interleaved8x2>)](vimage/pixelbuffer/applypolynomial(coefficientsegments:boundaries:destination:)-6uls3.md)
  Applies a set of piecewise polynomials to a 2-channel, 32-bit interleaved buffer and writes the result to a 2-channel, 8-bit interleaved buffer.
- [func applyPolynomial(coefficientSegments: [[Float]], boundaries: [Float], destination: vImage.PixelBuffer<vImage.Interleaved8x3>)](vimage/pixelbuffer/applypolynomial(coefficientsegments:boundaries:destination:)-4r6nf.md)
  Applies a set of piecewise polynomials to a 3-channel, 32-bit interleaved buffer and writes the result to a 3-channel, 8-bit interleaved buffer.
- [func applyPolynomial(coefficientSegments: [[Float]], boundaries: [Float], destination: vImage.PixelBuffer<vImage.Interleaved8x4>)](vimage/pixelbuffer/applypolynomial(coefficientsegments:boundaries:destination:)-1b2nu.md)
  Applies a set of piecewise polynomials to a 4-channel, 32-bit interleaved buffer and writes the result to a 4-channel, 8-bit interleaved buffer.
### Appying polynomial (8-bit source, 32-bit destination)
- [func applyPolynomial(coefficientSegments: [[Float]], boundaries: [Float], destination: vImage.PixelBuffer<vImage.PlanarF>)](vimage/pixelbuffer/applypolynomial(coefficientsegments:boundaries:destination:)-7sy2t.md)
  Applies a set of piecewise polynomials to an 8-bit planar buffer and writes the result to a 32-bit planar buffer.
- [func applyPolynomial(coefficientSegments: [[Float]], boundaries: [Float], destination: vImage.PixelBuffer<vImage.InterleavedFx2>)](vimage/pixelbuffer/applypolynomial(coefficientsegments:boundaries:destination:)-3sxxv.md)
  Applies a set of piecewise polynomials to a 2-channel, 8-bit interleaved buffer and writes the result to a 2-channel, 32-bit interleaved buffer.
- [func applyPolynomial(coefficientSegments: [[Float]], boundaries: [Float], destination: vImage.PixelBuffer<vImage.InterleavedFx3>)](vimage/pixelbuffer/applypolynomial(coefficientsegments:boundaries:destination:)-4o5ju.md)
  Applies a set of piecewise polynomials to a 3-channel, 8-bit interleaved buffer and writes the result to a 3-channel, 32-bit interleaved buffer.
- [func applyPolynomial(coefficientSegments: [[Float]], boundaries: [Float], destination: vImage.PixelBuffer<vImage.InterleavedFx4>)](vimage/pixelbuffer/applypolynomial(coefficientsegments:boundaries:destination:)-6ohrj.md)
  Applies a set of piecewise polynomials to a 4-channel, 8-bit interleaved buffer and writes the result to a 4-channel, 32-bit interleaved buffer.
### Appying polynomial (32-bit)
- [func applyPolynomial(coefficientSegments: [[Float]], boundaries: [Float], destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/applypolynomial(coefficientsegments:boundaries:destination:)-3c46t.md)
  Applies a set of piecewise polynomials to a 32-bit planar buffer.
- [func applyPolynomial(coefficientSegments: [[Float]], boundaries: [Float], destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/applypolynomial(coefficientsegments:boundaries:destination:)-8f5i9.md)
  Applies a set of piecewise polynomials to a 2-channel, 32-bit interleaved buffer.
- [func applyPolynomial(coefficientSegments: [[Float]], boundaries: [Float], destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/applypolynomial(coefficientsegments:boundaries:destination:)-26zom.md)
  Applies a set of piecewise polynomials to a 3-channel, 32-bit interleaved buffer.
- [func applyPolynomial(coefficientSegments: [[Float]], boundaries: [Float], destination: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/applypolynomial(coefficientsegments:boundaries:destination:)-8uesn.md)
  Applies a set of piecewise polynomials to a 4-channel, 32-bit interleaved buffer.
### Transforming with a lookup table
- [func applyLookup([Pixel_8], destination: vImage.PixelBuffer<vImage.Planar8>)](vimage/pixelbuffer/applylookup(_:destination:)-5r7bq.md)
  Applies a lookup table to transform an 8-bit planar image.
- [func applyLookup([Pixel_F], destination: vImage.PixelBuffer<vImage.PlanarF>)](vimage/pixelbuffer/applylookup(_:destination:)-14pjo.md)
  Applies a lookup table to transform an 8-bit planar image to a 32-bit planar image.
- [func applyLookup([Pixel_16U], destination: vImage.PixelBuffer<vImage.Planar16U>)](vimage/pixelbuffer/applylookup(_:destination:)-5oi4o.md)
  Applies a lookup table to transform an 8-bit planar image to a 16-bit planar image.
- [func applyLookup([Pixel_8888], destination: vImage.PixelBuffer<vImage.Interleaved8x3>)](vimage/pixelbuffer/applylookup(_:destination:)-3ruls.md)
  Applies a lookup table to transform an 8-bit planar image to an 8-bit-per-channel, three-channel interleaved image.
- [func applyLookup([Pixel_FFFF], destination: vImage.PixelBuffer<vImage.InterleavedFx3>)](vimage/pixelbuffer/applylookup(_:destination:)-1tsb5.md)
  Applies a lookup table to transform an 8-bit planar image to a 32-bit-per-channel, three-channel interleaved image.
- [func applyLookup(alphaTable: [Pixel_8]?, redTable: [Pixel_8]?, greenTable: [Pixel_8]?, blueTable: [Pixel_8]?, destination: vImage.PixelBuffer<vImage.Interleaved8x4>)](vimage/pixelbuffer/applylookup(alphatable:redtable:greentable:bluetable:destination:).md)
  Applies a set of four lookup tables to transform an interleaved, four-channel 8-bit image.
### Transforming with a multidimensional lookup table
- [vImage.MultidimensionalLookupTable](vimage/multidimensionallookuptable.md)
  A multidimensional lookup table.
### Applying a flood fill to an image
- [func floodFill(from: CGPoint, newColor: Pixel_8, connectivity: vImage.FloodFillConnectivity)](vimage/pixelbuffer/floodfill(from:newcolor:connectivity:)-44z7t.md)
  Applies an in-place flood-fill operation to the 8-bit planar image.
- [func floodFill(from: CGPoint, newColor: Pixel_8888, connectivity: vImage.FloodFillConnectivity)](vimage/pixelbuffer/floodfill(from:newcolor:connectivity:)-56w4b.md)
  Applies an in-place flood-fill operation to the interleaved 4-channel, 8-bit-per-pixel image.
- [func floodFill(from: CGPoint, newColor: Pixel_16U, connectivity: vImage.FloodFillConnectivity)](vimage/pixelbuffer/floodfill(from:newcolor:connectivity:)-219lg.md)
  Applies an in-place flood-fill operation to the unsigned 16-bit planar image.
- [func floodFill(from: CGPoint, newColor: Pixel_ARGB_16U, connectivity: vImage.FloodFillConnectivity)](vimage/pixelbuffer/floodfill(from:newcolor:connectivity:)-6hsrg.md)
  Applies an in-place flood-fill operation to the interleaved 4-channel, unsigned16-bit-per-pixel image.

## See Also

- [Applying geometric operations to pixel buffers](applying-geometric-operations-to-pixel-buffers.md)
  Reflect, shear, rotate, scale, and apply affine transforms to image data.
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
- [Interleaving and deinterleaving pixel buffers](interleaving-and-deinterleaving-pixel-buffers.md)
  Convert pixel buffer data between interleaved and planar formats.
- [Cropping and working with regions of interest](cropping-and-working-with-regions-of-interest.md)
  Crop images and apply operations to regions of interest.
- [Applying channel operations](applying-channel-operations.md)
  Extract, flatten, permute, and overwrite the individual color channels of a pixel buffer.
- [Applying arithmetic operations](applying-arithmetic-operations.md)
  Multiply the pixel values of a buffer by scalar values or matrices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/applying-color-transforms-to-pixel-buffers)*