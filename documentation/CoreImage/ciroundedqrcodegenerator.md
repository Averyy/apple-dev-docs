# CIRoundedQRCodeGenerator

**Framework**: Core Image  
**Kind**: protocol

The protocol for the Rounded QR Code Generator filter.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
protocol CIRoundedQRCodeGenerator : CIFilterProtocol
```

#### Overview

Generate a QR Code image for message data.

## Topics

### Instance Properties
- [var centerSpaceSize: Float](ciroundedqrcodegenerator/centerspacesize.md)
  The fraction of the center space of the QRCode to fill with Color 1. If the size is 0.0 or the Correction Level is L or M, the center of the QRCode will be unaltered. The size will be limited to 0.25 if the Correction Level is Q. The size will be limited to 0.33 if the Correction Level is H.
- [var color0: CIColor](ciroundedqrcodegenerator/color0.md)
  The background color for the QRCode
- [var color1: CIColor](ciroundedqrcodegenerator/color1.md)
  The foreground color for the QRCode
- [var correctionLevel: String](ciroundedqrcodegenerator/correctionlevel.md)
  QR Code correction level L, M, Q, or H.
- [var message: Data](ciroundedqrcodegenerator/message.md)
  The message to encode in the QR Code
- [var roundedData: Bool](ciroundedqrcodegenerator/roundeddata.md)
  If true then the data points in the QRCode should have a rounded appearance.
- [var roundedMarkers: Int](ciroundedqrcodegenerator/roundedmarkers.md)
  If 1, then the Finder Patterns in the QRCode should have a rounded appearance. If 2, then the Alignment Patterns will also be rounded
- [var scale: Float](ciroundedqrcodegenerator/scale.md)
  The scale factor to enlarge the QRCode by.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciroundedqrcodegenerator)*