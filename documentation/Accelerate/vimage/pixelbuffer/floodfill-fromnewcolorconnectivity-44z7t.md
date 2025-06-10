# floodFill(from:newColor:connectivity:)

**Framework**: Accelerate  
**Kind**: method

Applies an in-place flood-fill operation to the 8-bit planar image.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
func floodFill(from seed: CGPoint, newColor: Pixel_8, connectivity: vImage.FloodFillConnectivity)
```

#### Discussion

The flood-fill function sets all pixels that are neighboring and identical to the seed pixel to a new color. The operation continues until it reaches the image boundary or until it sets all pixels within the connected component to the new value.

The following code applies a flood fill to an 8-bit planar pixel buffer and uses the image’s center pixel as the seed.

```swift
// `pixelBuffer` is a `vImage.PixelBuffer<vImage.Planar8>`.

pixelBuffer.floodFill(from: CGPoint(x: pixelBuffer.width / 2,
                                    y: pixelBuffer.height / 2),
                      newColor: fillColor,
                      connectivity: .edgesAndCorners)
```

The image below shows the original line-art image on the left, and the flood-filled image on the right:

![Two versions of a line drawing of a star. On the left is the original outline drawing of a star, and on the right is the same star but flood-filled with a solid color.](https://docs-assets.developer.apple.com/published/6d073826e3dc529b753acd82e582c49a/media-4165184%402x.png)

## Parameters

- `seed`: The coordinates that define the position of the seed pixel inside the connected component.
- `newColor`: The new pixel value that overwrites the pixels in the connected component.
- `connectivity`: An enumeration that specifies which pixels the operation includes as neighbors. Pass   to specify a four-connected neighborhood of a pixel that includes the pixels to the left and right, and those above and below. Pass   to specify an eight-connected neighborhood that includes the four-connected neighborhood and the pixels on the four diagonals.

## See Also

- [Applying flood fills to an image](applying-flood-fills-to-an-image.md)
  Fill consistently colored connected parts of an image with a new color.
- [func floodFill(from: CGPoint, newColor: Pixel_8888, connectivity: vImage.FloodFillConnectivity)](vimage/pixelbuffer/floodfill(from:newcolor:connectivity:)-56w4b.md)
  Applies an in-place flood-fill operation to the interleaved 4-channel, 8-bit-per-pixel image.
- [func floodFill(from: CGPoint, newColor: Pixel_16U, connectivity: vImage.FloodFillConnectivity)](vimage/pixelbuffer/floodfill(from:newcolor:connectivity:)-219lg.md)
  Applies an in-place flood-fill operation to the unsigned 16-bit planar image.
- [func floodFill(from: CGPoint, newColor: Pixel_ARGB_16U, connectivity: vImage.FloodFillConnectivity)](vimage/pixelbuffer/floodfill(from:newcolor:connectivity:)-6hsrg.md)
  Applies an in-place flood-fill operation to the interleaved 4-channel, unsigned16-bit-per-pixel image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/floodfill(from:newcolor:connectivity:)-44z7t)*