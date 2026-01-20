# CIDotScreen

**Framework**: Core Image  
**Kind**: protocol

The properties you use to configure a dot screen filter.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
protocol CIDotScreen : CIFilterProtocol
```

## Topics

### Instance Properties
- [var angle: Float](cidotscreen/angle.md)
  The angle of the pattern.
- [var center: CGPoint](cidotscreen/center.md)
  The x and y position to use as the center of the dot screen pattern.
- [var inputImage: CIImage?](cidotscreen/inputimage.md)
  The image to use as an input image.
- [var sharpness: Float](cidotscreen/sharpness.md)
  The sharpness of the pattern.
- [var width: Float](cidotscreen/width.md)
  The distance between dots in the pattern.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func dotScreen() -> any CIFilter & CIDotScreen](cifilter-swift.class/dotscreen.md)
  Creates a monochrome image with a series of dots to add detail.
- [protocol CICircularScreen](cicircularscreen.md)
  The properties you use to configure a circular screen filter.
- [protocol CICMYKHalftone](cicmykhalftone.md)
  The properties you use to configure a CMYK halftone filter.
- [protocol CIHatchedScreen](cihatchedscreen.md)
  The properties you use to configure a hatched screen filter.
- [protocol CILineScreen](cilinescreen.md)
  The properties you use to configure a line screen filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cidotscreen)*