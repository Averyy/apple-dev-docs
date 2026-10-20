# averagePixelLuminance

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

The average amount of luminosity of the pixels on an OLED display.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.15+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`PixelLuminanceMetric`](../pixelluminancemetric.md) instead.

## Declaration

```swift
var averagePixelLuminance: MXAverage<MXUnitAveragePixelLuminance>? { get }
```

```objc
@property (strong, readonly, nullable) MXAverage<MXUnitAveragePixelLuminance *> * averagePixelLuminance;
```

## See Also

### Reading average active pixel use
- [class MXUnitAveragePixelLuminance](../mxunitaveragepixelluminance.md)
  A unit of measure of pixel luminosity on an OLED display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxdisplaymetric/averagepixelluminance)*