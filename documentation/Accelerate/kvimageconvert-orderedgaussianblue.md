# kvImageConvert_OrderedGaussianBlue

**Framework**: Accelerate  
**Kind**: var

A constant that indicates the conversion will distribute the noise according to a Gaussian distribution.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var kvImageConvert_OrderedGaussianBlue: UInt32 { get }
```

#### Discussion

The following shows an 8-bit RGB image converted to a 1-bit planar image with [`vImageConvert_Planar8toPlanar1(_:_:_:_:_:)`](vimageconvert_planar8toplanar1(_:_:_:_:_:).md) using [`kvImageConvert_DitherOrderedReproducible`](kvimageconvert_ditherorderedreproducible.md). The image on the left uses [`kvImageConvert_OrderedGaussianBlue`](kvimageconvert_orderedgaussianblue.md), and the image on the right uses [`kvImageConvert_OrderedUniformBlue`](kvimageconvert_ordereduniformblue.md):

![Photos showing images with different noise distributions applied during dithering.](https://docs-assets.developer.apple.com/published/beda0d003a2257d21f39a3c03cb147aa/media-3358020%402x.png)

To learn about converting an RGB image to grayscale, see [`Converting color images to grayscale`](converting-color-images-to-grayscale.md).

## See Also

- [var kvImageConvert_DitherNone: UInt32](kvimageconvert_dithernone.md)
  A constant that indicates the conversion will not apply dithering.
- [var kvImageConvert_DitherOrdered: UInt32](kvimageconvert_ditherordered.md)
  A constant that indicates the conversion will add randomized, pre-computed blue noise to the image.
- [var kvImageConvert_DitherOrderedReproducible: UInt32](kvimageconvert_ditherorderedreproducible.md)
  A constant that indicates the conversion will add reproducible, pre-computed blue noise to the image.
- [var kvImageConvert_DitherFloydSteinberg: UInt32](kvimageconvert_ditherfloydsteinberg.md)
  A constant that indicates the conversion will add Floyd-Steinberg dithering to the image.
- [var kvImageConvert_DitherAtkinson: UInt32](kvimageconvert_ditheratkinson.md)
  A constant that indicates the conversion will add Atkinson dithering to the image.
- [var kvImageConvert_OrderedUniformBlue: UInt32](kvimageconvert_ordereduniformblue.md)
  A constant that indicates the conversion will distribute the noise uniformly.
- [var kvImageConvert_OrderedNoiseShapeMask: UInt32](kvimageconvert_orderednoiseshapemask.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/kvimageconvert_orderedgaussianblue)*