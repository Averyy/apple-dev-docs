# triangleKaleidoscope()

**Framework**: Core Image  
**Kind**: method

Create a triangular kaleidoscope effect and then tiles the result.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func triangleKaleidoscope() -> any CIFilter & CITriangleKaleidoscope
```

#### Return Value

The tiled image.

#### Discussion

This method applies the triangle kaleidoscope filter to an image. The effect produces a complex tiled pattern from a triangular area input image.

The triangle kaleidoscope tile filter uses the following properties:

- **`inputImage`**: An image with the type [`CIImage`](ciimage.md).
- **`decay`**: A `float` representing the intensity of the color fade from the center of the triangle as an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber).
- **`point`**: A set of coordinates marking the center of the triangular area of the input image as a [`CIVector`](civector.md).
- **`rotation`**: A `float` representing the angle of rotation of the triangle as an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber).
- **`size`**: A `float` representing the size in pixels of the triangle as an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber).

The following code creates a filter that produces a triangle tile of the input image, creating an optical illusion:

```swift
func triangleKaleidoscope(inputImage: CIImage) -> CIImage {
    let triangleKaleidoscopeTile = CIFilter.triangleKaleidoscope()
    triangleKaleidoscopeTile.inputImage = inputImage
    triangleKaleidoscopeTile.point = CGPoint(x: 150, y: 150)
    triangleKaleidoscopeTile.size = 700
    triangleKaleidoscopeTile.rotation = -0.36
    triangleKaleidoscopeTile.decay = 0.85
    return triangleKaleidoscopeTile.outputImage!
}
```

![Two photographs of a bouquet of multiple colorful flowers. The photo on the left is up close with good lighting and focus. In the photo on the right, a triangle kaleidoscope filter is applied, resulting in a triangular portion of the image being angled and repeated throughout the entire image.](https://docs-assets.developer.apple.com/published/f00ec66d6be96e93b06365f384ff0dfb/media-3599889%402x.png)

## See Also

- [class func affineClamp() -> any CIFilter & CIAffineClamp](cifilter-swift.class/affineclamp.md)
  Performs a transform on the image and extends the image edges to infinity.
- [class func affineTile() -> any CIFilter & CIAffineTile](cifilter-swift.class/affinetile.md)
  Performs a transform on the image and tiles the result.
- [class func eightfoldReflectedTile() -> any CIFilter & CIEightfoldReflectedTile](cifilter-swift.class/eightfoldreflectedtile.md)
  Creates an eight-way reflected pattern.
- [class func fourfoldReflectedTile() -> any CIFilter & CIFourfoldReflectedTile](cifilter-swift.class/fourfoldreflectedtile.md)
  Creates a four-way reflected pattern.
- [class func fourfoldRotatedTile() -> any CIFilter & CIFourfoldRotatedTile](cifilter-swift.class/fourfoldrotatedtile.md)
  Creates a tiled image by rotating a tile in increments of 90 degrees.
- [class func fourfoldTranslatedTile() -> any CIFilter & CIFourfoldTranslatedTile](cifilter-swift.class/fourfoldtranslatedtile.md)
  Creates a tiled image by applying four translation operations.
- [class func glideReflectedTile() -> any CIFilter & CIGlideReflectedTile](cifilter-swift.class/glidereflectedtile.md)
  Tiles an image by rotating and reflecting a tile from the image.
- [class func kaleidoscope() -> any CIFilter & CIKaleidoscope](cifilter-swift.class/kaleidoscope.md)
  Creates a 12-way kaleidoscopic image from an image.
- [class func opTile() -> any CIFilter & CIOpTile](cifilter-swift.class/optile.md)
  Produces an effect that mimics a style of visual art that uses optical illusions.
- [class func parallelogramTile() -> any CIFilter & CIParallelogramTile](cifilter-swift.class/parallelogramtile.md)
  Warps the image to create a parallelogram and tiles the result.
- [class func perspectiveTile() -> any CIFilter & CIPerspectiveTile](cifilter-swift.class/perspectivetile.md)
  Tiles an image by adjusting the perspective of the image.
- [class func sixfoldReflectedTile() -> any CIFilter & CISixfoldReflectedTile](cifilter-swift.class/sixfoldreflectedtile.md)
  Produces a tiled image from a source image by applying a six-way reflected symmetry.
- [class func sixfoldRotatedTile() -> any CIFilter & CISixfoldRotatedTile](cifilter-swift.class/sixfoldrotatedtile.md)
  Creates a tiled image by rotating in increments of 60 degrees.
- [class func triangleTile() -> any CIFilter & CITriangleTile](cifilter-swift.class/triangletile.md)
  Tiles a triangular area of an image.
- [class func twelvefoldReflectedTile() -> any CIFilter & CITwelvefoldReflectedTile](cifilter-swift.class/twelvefoldreflectedtile.md)
  Creates a tiled image by rotating in increments of 30 degrees.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/trianglekaleidoscope())*