# apl

**Framework**: MetricKit  
**Kind**: property

The average number of powered pixels on a OLED display.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
class var apl: MXUnitAveragePixelLuminance { get }
```

#### Discussion

The value of `apl` is a whole number ranging from 0 to 100. 0 means the display is black with no illuminated pixels. A value of 100 means the display is white with all red, green, and blue components of all pixels illuminated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxunitaveragepixelluminance/apl)*