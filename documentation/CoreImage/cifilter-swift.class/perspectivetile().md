# perspectiveTile()

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Tiles an image by adjusting the perspective of the image.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func perspectiveTile() -> any CIFilter & CIPerspectiveTile
```

```objc
+ (CIFilter<CIPerspectiveTile> *) perspectiveTileFilter;
```

#### Return Value

The tiled image.

#### Discussion

This method applies the perspective tile filter to an image. The effect adjusts the perspective of the image and then tiles the result.

The perspective tile filter uses the following properties:

- **`inputImage`**: An image with the type [`CIImage`](../ciimage.md).
- **`topLeft`**: A [`CGPoint`](../../CoreFoundation/cgpoint.md) of the input image mapped to the top-left corner of the tile.
- **`topRight`**: A [`CGPoint`](../../CoreFoundation/cgpoint.md) of the input image mapped to the top-right corner of the tile.
- **`bottomLeft`**: A [`CGPoint`](../../CoreFoundation/cgpoint.md) of the input image mapped to the bottom-left corner of the tile.
- **`bottomRight`**: A [`CGPoint`](../../CoreFoundation/cgpoint.md) of the input image mapped to the bottom-right corner of the tile.

The following code creates a filter that tiles the image and adjusts the perspective to add depth:

```swift
func perspective(inputImage: CIImage) -> CIImage {
    let perspectiveTile = CIFilter.perspectiveTile()
    perspectiveTile.inputImage = inputImage
    perspectiveTile.topLeft = CGPoint(x: 118, y: 484)
    perspectiveTile.topRight = CGPoint(x: 646, y: 507)
    perspectiveTile.bottomLeft = CGPoint(x: 548, y: 140)
    perspectiveTile.bottomRight = CGPoint(x: 155, y: 153)
    return perspectiveTile.outputImage!
}
```

![Two photographs. The photo on the left is of a bouquet of colorful flowers up close with good lighting and focus. In the photo on the right, a perspective tile filter is applied, resulting in the entire image becoming tiled and distorted.](https://developer.apple.com/tutorials/images/com.apple.coreimage/media-3599879@2x.png)

## See Also

### Filters
- [class func affineClamp() -> any CIFilter & CIAffineClamp](./affineclamp%28%29.md)
  Performs a transform on the image and extends the image edges to infinity.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/perspectivetile())*