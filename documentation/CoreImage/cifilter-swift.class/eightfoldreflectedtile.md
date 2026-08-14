# eightfoldReflectedTile()

**Framework**: Core Image  
**Kind**: method

Creates an eight-way reflected pattern.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func eightfoldReflectedTile() -> any CIFilter & CIEightfoldReflectedTile
```

#### Return Value

The tiled image.

#### Discussion

This method applies the eight-fold reflected tile filter to an image. The effect creates an eight-way symmetry from the input image and tiles it to create the output image.

The eight-fold reflected tile filter uses the following properties:

- **`inputImage`**: An image with the type [`CIImage`](ciimage.md).
- **`center`**: A set of coordinates marking the center of the image as a [`CGPoint`](https://developer.apple.com/documentation/corefoundation/cgpoint).
- **`angle`**: A `float` representing the direction of distortion, in radians as an [`NSNumber`](https://developer.apple.com/documentation/foundation/nsnumber).
- **`width`**: A `float` representing the set width of each tile as an [`NSNumber`](https://developer.apple.com/documentation/foundation/nsnumber).

The following code creates a filter that results in small symmetrical repeated tiles:

```swift
func eightFoldReflected(inputImage: CIImage) -> CIImage {
    let eightFoldReflectedTile = CIFilter.eightfoldReflectedTile()
    eightFoldReflectedTile.inputImage = inputImage
    eightFoldReflectedTile.center = CGPoint(x: inputImage.extent.midX, y: inputImage.extent.midY)
    eightFoldReflectedTile.width = 400
    eightFoldReflectedTile.angle = 1
    return eightFoldReflectedTile.outputImage!
}
```

![A bouquet of multiple colorful flowers photographed up close with good lighting and focus. In the photo on the right, an eight-fold reflected tile filter is applied resulting in a square pattern that is repeated throughout the image.](/images/com.apple.coreimage/media-4333630@2x.png)

## See Also

- [class func affineClamp() -> any CIFilter & CIAffineClamp](cifilter-swift.class/affineclamp.md)
  Performs a transform on the image and extends the image edges to infinity.
- [class func affineTile() -> any CIFilter & CIAffineTile](cifilter-swift.class/affinetile.md)
  Performs a transform on the image and tiles the result.
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
- [class func triangleKaleidoscope() -> any CIFilter & CITriangleKaleidoscope](cifilter-swift.class/trianglekaleidoscope.md)
  Create a triangular kaleidoscope effect and then tiles the result.
- [class func triangleTile() -> any CIFilter & CITriangleTile](cifilter-swift.class/triangletile.md)
  Tiles a triangular area of an image.
- [class func twelvefoldReflectedTile() -> any CIFilter & CITwelvefoldReflectedTile](cifilter-swift.class/twelvefoldreflectedtile.md)
  Creates a tiled image by rotating in increments of 30 degrees.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/eightfoldreflectedtile())*