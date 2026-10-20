# apl

**Framework**: MetricKit  
**Kind**: property  
**Role**: Type Property

The average number of powered pixels on a OLED display.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.15+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`AveragePixelLuminance`](../averagepixelluminance.md) instead.

## Declaration

```swift
@NSCopying
class var apl: MXUnitAveragePixelLuminance { get }
```

```objc
@property (class, copy, readonly) MXUnitAveragePixelLuminance * apl;
```

#### Discussion

The value of `apl` is a whole number ranging from 0 to 100. 0 means the display is black with no illuminated pixels. A value of 100 means the display is white with all red, green, and blue components of all pixels illuminated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxunitaveragepixelluminance/apl)*