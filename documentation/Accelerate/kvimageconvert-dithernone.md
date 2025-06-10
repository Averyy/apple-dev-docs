# kvImageConvert_DitherNone

**Framework**: Accelerate  
**Kind**: var

A constant that indicates the conversion will not apply dithering.

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
var kvImageConvert_DitherNone: UInt32 { get }
```

#### Discussion

The following shows an 8-bit RGB image converted to a 1-bit planar image with [`vImageConvert_Planar8toPlanar1(_:_:_:_:_:)`](vimageconvert_planar8toplanar1(_:_:_:_:_:).md) using [`kvImageConvert_DitherNone`](kvimageconvert_dithernone.md):

![Photos showing the original image and the dithered image.](https://docs-assets.developer.apple.com/published/cabd3837466ead94279da64b329ca789/media-3358017%402x.png)

To learn about converting an RGB image to grayscale, see [`Converting color images to grayscale`](converting-color-images-to-grayscale.md).

## See Also

- [var kvImageConvert_DitherOrdered: UInt32](kvimageconvert_ditherordered.md)
  A constant that indicates the conversion will add randomized, pre-computed blue noise to the image.
- [var kvImageConvert_DitherOrderedReproducible: UInt32](kvimageconvert_ditherorderedreproducible.md)
  A constant that indicates the conversion will add reproducible, pre-computed blue noise to the image.
- [var kvImageConvert_DitherFloydSteinberg: UInt32](kvimageconvert_ditherfloydsteinberg.md)
  A constant that indicates the conversion will add Floyd-Steinberg dithering to the image.
- [var kvImageConvert_DitherAtkinson: UInt32](kvimageconvert_ditheratkinson.md)
  A constant that indicates the conversion will add Atkinson dithering to the image.
- [var kvImageConvert_OrderedGaussianBlue: UInt32](kvimageconvert_orderedgaussianblue.md)
  A constant that indicates the conversion will distribute the noise according to a Gaussian distribution.
- [var kvImageConvert_OrderedUniformBlue: UInt32](kvimageconvert_ordereduniformblue.md)
  A constant that indicates the conversion will distribute the noise uniformly.
- [var kvImageConvert_OrderedNoiseShapeMask: UInt32](kvimageconvert_orderednoiseshapemask.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/kvimageconvert_dithernone)*