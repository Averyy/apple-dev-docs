# CIOpTile

**Framework**: Core Image  
**Kind**: protocol

The properties you use to configure an optical tile filter.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
protocol CIOpTile : CIFilterProtocol
```

## Topics

### Instance Properties
- [var angle: Float](cioptile/angle.md)
  The angle of a tile.
- [var center: CGPoint](cioptile/center.md)
  The x and y position to use as the center of the effect.
- [var inputImage: CIImage?](cioptile/inputimage.md)
  The image to use as an input image.
- [var scale: Float](cioptile/scale.md)
  A value that determines the number of tiles in the effect.
- [var width: Float](cioptile/width.md)
  The width of a tile.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func opTile() -> any CIFilter & CIOpTile](cifilter-swift.class/optile.md)
  Produces an effect that mimics a style of visual art that uses optical illusions.
- [protocol CIAffineClamp](ciaffineclamp.md)
  The properties you use to configure an affine clamp filter.
- [protocol CIAffineTile](ciaffinetile.md)
  The properties you use to configure an affine tile filter.
- [protocol CIEightfoldReflectedTile](cieightfoldreflectedtile.md)
  The properties you use to configure an eightfold reflected tile filter.
- [protocol CIFourfoldReflectedTile](cifourfoldreflectedtile.md)
  The properties you use to configure a fourfold reflected tile filter.
- [protocol CIFourfoldRotatedTile](cifourfoldrotatedtile.md)
  The properties you use to configure a fourfold rotated tile filter.
- [protocol CIFourfoldTranslatedTile](cifourfoldtranslatedtile.md)
  The properties you use to configure a fourfold translated tile filter.
- [protocol CIGlideReflectedTile](ciglidereflectedtile.md)
  The properties you use to configure a glide reflected tile filter.
- [protocol CIKaleidoscope](cikaleidoscope.md)
  The properties you use to configure a kaleidoscope filter.
- [protocol CIParallelogramTile](ciparallelogramtile.md)
  The properties you use to configure a parallelogram tile filter.
- [protocol CIPerspectiveTile](ciperspectivetile.md)
  The properties you use to configure a perspective tile filter.
- [protocol CISixfoldReflectedTile](cisixfoldreflectedtile.md)
  The properties you use to configure a sixfold reflected tile filter.
- [protocol CISixfoldRotatedTile](cisixfoldrotatedtile.md)
  The properties you use to configure a sixfold rotated tile filter.
- [protocol CITriangleKaleidoscope](citrianglekaleidoscope.md)
  The properties you use to configure a triangle kaleidoscope filter.
- [protocol CITriangleTile](citriangletile.md)
  The properties you use to configure a triangle tile filter.
- [protocol CITwelvefoldReflectedTile](citwelvefoldreflectedtile.md)
  The properties you use to configure a twelvefold reflected tile filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cioptile)*