# eightfoldReflectedTile()

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

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

```objc
+ (CIFilter<CIEightfoldReflectedTile> *) eightfoldReflectedTileFilter;
```

#### Return Value

The tiled image.

#### Discussion

This method applies the eight-fold reflected tile filter to an image. The effect creates an eight-way symmetry from the input image and tiles it to create the output image.

The eight-fold reflected tile filter uses the following properties:

- **`inputImage`**: An image with the type [`CIImage`](../ciimage.md).
- **`center`**: A set of coordinates marking the center of the image as a [`CGPoint`](../../CoreFoundation/cgpoint.md).
- **`angle`**: A `float` representing the direction of distortion, in radians as an [`NSNumber`](../../Foundation/nsnumber.md).
- **`width`**: A `float` representing the set width of each tile as an [`NSNumber`](../../Foundation/nsnumber.md).

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

![A bouquet of multiple colorful flowers photographed up close with good lighting and focus. In the photo on the right, an eight-fold reflected tile filter is applied resulting in a square pattern that is repeated throughout the image.](https://developer.apple.com/tutorials/images/com.apple.coreimage/media-4333630@2x.png)

## See Also

### Filters
- [class func affineClamp() -> any CIFilter & CIAffineClamp](./affineclamp%28%29.md)
  Performs a transform on the image and extends the image edges to infinity.
- [class func affineTile() -> any CIFilter & CIAffineTile](./affinetile%28%29.md)
  Performs a transform on the image and tiles the result.
- [class func fourfoldReflectedTile() -> any CIFilter & CIFourfoldReflectedTile](./fourfoldreflectedtile%28%29.md)
  Creates a four-way reflected pattern.
- [class func fourfoldRotatedTile() -> any CIFilter & CIFourfoldRotatedTile](./fourfoldrotatedtile%28%29.md)
  Creates a tiled image by rotating a tile in increments of 90 degrees.
- [class func fourfoldTranslatedTile() -> any CIFilter & CIFourfoldTranslatedTile](./fourfoldtranslatedtile%28%29.md)
  Creates a tiled image by applying four translation operations.
- [class func glideReflectedTile() -> any CIFilter & CIGlideReflectedTile](./glidereflectedtile%28%29.md)
  Tiles an image by rotating and reflecting a tile from the image.
- [class func kaleidoscope() -> any CIFilter & CIKaleidoscope](./kaleidoscope%28%29.md)
  Creates a 12-way kaleidoscopic image from an image.
- [class func opTile() -> any CIFilter & CIOpTile](./optile%28%29.md)
  Produces an effect that mimics a style of visual art that uses optical illusions.
- [class func parallelogramTile() -> any CIFilter & CIParallelogramTile](./parallelogramtile%28%29.md)
  Warps the image to create a parallelogram and tiles the result.
- [class func perspectiveTile() -> any CIFilter & CIPerspectiveTile](./perspectivetile%28%29.md)
  Tiles an image by adjusting the perspective of the image.
- [class func sixfoldReflectedTile() -> any CIFilter & CISixfoldReflectedTile](./sixfoldreflectedtile%28%29.md)
  Produces a tiled image from a source image by applying a six-way reflected symmetry.
- [class func sixfoldRotatedTile() -> any CIFilter & CISixfoldRotatedTile](./sixfoldrotatedtile%28%29.md)
  Creates a tiled image by rotating in increments of 60 degrees.
- [class func triangleKaleidoscope() -> any CIFilter & CITriangleKaleidoscope](./trianglekaleidoscope%28%29.md)
  Create a triangular kaleidoscope effect and then tiles the result.
- [class func triangleTile() -> any CIFilter & CITriangleTile](./triangletile%28%29.md)
  Tiles a triangular area of an image.
- [class func twelvefoldReflectedTile() -> any CIFilter & CITwelvefoldReflectedTile](./twelvefoldreflectedtile%28%29.md)
  Creates a tiled image by rotating in increments of 30 degrees.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/eightfoldreflectedtile())*