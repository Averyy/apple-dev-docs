# maximumLinearExposure

**Framework**: AppKit  
**Kind**: property

The maximum linear exposure that can be set on a color picked in the color panel. Defaults to 1 and ignores any value less than 1. If set to a value >= 2, the color picked by the panel may have a linear exposure applied to it.

**Availability**:
- macOS 26.0+

## Declaration

```swift
@MainActor
var maximumLinearExposure: CGFloat { get set }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorpanel/maximumlinearexposure)*