# CIBlurredRoundedRectangleGenerator

**Framework**: Core Image  
**Kind**: protocol

The protocol for the Blurred Rounded Rectangle Generator filter.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
protocol CIBlurredRoundedRectangleGenerator : CIFilterProtocol
```

#### Overview

Generates a blurred rounded rectangle image with the specified extent, corner radius, blur sigma, and color.

## Topics

### Instance Properties
- [var color: CIColor](ciblurredroundedrectanglegenerator/color.md)
  A color.
- [var extent: CGRect](ciblurredroundedrectanglegenerator/extent.md)
  A rectangle that defines the extent of the effect.
- [var radius: Float](ciblurredroundedrectanglegenerator/radius.md)
  The distance from the center of the effect.
- [var sigma: Float](ciblurredroundedrectanglegenerator/sigma.md)
  The sigma for a gaussian blur.
- [var smoothness: Float](ciblurredroundedrectanglegenerator/smoothness.md)
  A value to control the smoothness of the transition between the curved and linear edges of the shape.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciblurredroundedrectanglegenerator)*