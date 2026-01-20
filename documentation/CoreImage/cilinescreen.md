# CILineScreen

**Framework**: Core Image  
**Kind**: protocol

The properties you use to configure a line screen filter.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
protocol CILineScreen : CIFilterProtocol
```

## Topics

### Instance Properties
- [var angle: Float](cilinescreen/angle.md)
  The angle of the pattern.
- [var center: CGPoint](cilinescreen/center.md)
  The x and y position to use as the center of the line screen pattern.
- [var inputImage: CIImage?](cilinescreen/inputimage.md)
  The image to use as an input image.
- [var sharpness: Float](cilinescreen/sharpness.md)
  The sharpness of the pattern.
- [var width: Float](cilinescreen/width.md)
  The distance between lines in the pattern.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func lineScreen() -> any CIFilter & CILineScreen](cifilter-swift.class/linescreen.md)
  Creates a monochrome image with a series of small lines to add detail.
- [protocol CICircularScreen](cicircularscreen.md)
  The properties you use to configure a circular screen filter.
- [protocol CICMYKHalftone](cicmykhalftone.md)
  The properties you use to configure a CMYK halftone filter.
- [protocol CIDotScreen](cidotscreen.md)
  The properties you use to configure a dot screen filter.
- [protocol CIHatchedScreen](cihatchedscreen.md)
  The properties you use to configure a hatched screen filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cilinescreen)*