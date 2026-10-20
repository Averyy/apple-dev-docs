# affineClamp()

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Performs a transform on the image and extends the image edges to infinity.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func affineClamp() -> any CIFilter & CIAffineClamp
```

```objc
+ (CIFilter<CIAffineClamp> *) affineClampFilter;
```

#### Return Value

The tiled image.

#### Discussion

This method applies the affine clamp filter to an image. This effect performs similarly to the affine transform filter except that it produces an infinite image. You can use this filter when you need to blur an image but you want to avoid a soft, black fringe along the edges.

The affine clamp filter uses the following properties:

- **`inputImage`**: An image with the type [`CIImage`](../ciimage.md).
- **`transform`**: A [`CGAffineTransform`](../../CoreFoundation/cgaffinetransform.md) to constrain to the image.

The following code creates a filter that produces a cropped image with colored edges to fill the rest of the image:

```swift
func affineClamp(inputImage: CIImage) -> CIImage {
    let affineClamp = CIFilter.affineClamp()
    affineClamp.inputImage = inputImage
    affineClamp.transform = CGAffineTransform(a: 1.0, b: 0.0, c: 0.0, d: 1.0, tx: 0.0, ty: 0.0)
    return affineClamp.outputImage!
}
```

![Two photographs of a bouquet of multiple colorful flowers. The photo on the left is up close with good lighting and focus. In the photo on the right, an affine clamp filter is applied, resulting in the edges of the image colors stretching to the edge of the photo.](https://developer.apple.com/tutorials/images/com.apple.coreimage/media-3624745@2x.png)

## See Also

### Filters
- [class func affineTile() -> any CIFilter & CIAffineTile](./affinetile%28%29.md)
  Performs a transform on the image and tiles the result.
- [class func eightfoldReflectedTile() -> any CIFilter & CIEightfoldReflectedTile](./eightfoldreflectedtile%28%29.md)
  Creates an eight-way reflected pattern.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/affineclamp())*