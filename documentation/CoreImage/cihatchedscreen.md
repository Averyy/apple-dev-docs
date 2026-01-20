# CIHatchedScreen

**Framework**: Core Image  
**Kind**: protocol

The properties you use to configure a hatched screen filter.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
protocol CIHatchedScreen : CIFilterProtocol
```

## Topics

### Instance Properties
- [var angle: Float](cihatchedscreen/angle.md)
  The angle of the pattern.
- [var center: CGPoint](cihatchedscreen/center.md)
  The x and y position to use as the center of the hatched screen pattern.
- [var inputImage: CIImage?](cihatchedscreen/inputimage.md)
  The image to use as an input image.
- [var sharpness: Float](cihatchedscreen/sharpness.md)
  The amount of sharpening to apply.
- [var width: Float](cihatchedscreen/width.md)
  The distance between lines in the pattern.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func hatchedScreen() -> any CIFilter & CIHatchedScreen](cifilter-swift.class/hatchedscreen.md)
  Creates a monochrome image with a series of lines to add detail.
- [protocol CICircularScreen](cicircularscreen.md)
  The properties you use to configure a circular screen filter.
- [protocol CICMYKHalftone](cicmykhalftone.md)
  The properties you use to configure a CMYK halftone filter.
- [protocol CIDotScreen](cidotscreen.md)
  The properties you use to configure a dot screen filter.
- [protocol CILineScreen](cilinescreen.md)
  The properties you use to configure a line screen filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cihatchedscreen)*