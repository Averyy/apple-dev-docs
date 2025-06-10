# MXUnitAveragePixelLuminance

**Framework**: MetricKit  
**Kind**: class

A unit of measure of pixel luminosity on an OLED display.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
class MXUnitAveragePixelLuminance
```

#### Overview

Luminosity represents the brightness of each red, green, and blue component pixel. Unlike LCD displays, each pixel requires power to display a color, and white draws the most power per pixel.

`MXUnitAveragePixelLuminance` defines the base unit as the average luminance of all the pixels on the screen for some period of time. Reducing the average luminance of the display reduces the amount of power consumed by the app.

## Topics

### Measuring Average Pixel Luminance
- [class var apl: MXUnitAveragePixelLuminance](mxunitaveragepixelluminance/apl.md)
  The average number of powered pixels on a OLED display.

## Relationships

### Inherits From
- [Dimension](../Foundation/Dimension.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var averagePixelLuminance: MXAverage<MXUnitAveragePixelLuminance>?](mxdisplaymetric/averagepixelluminance.md)
  The average amount of luminosity of the pixels on an OLED display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxunitaveragepixelluminance)*