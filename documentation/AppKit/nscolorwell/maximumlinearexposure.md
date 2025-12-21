# maximumLinearExposure

**Framework**: AppKit  
**Kind**: property

The maximum linear exposure a color in this color well can be set to. Defaults to 1 and ignores any value less than 1. If set to a value >= 2, the color picked for this well may have a linear exposure applied to it.

**Availability**:
- macOS 26.0+

## Declaration

```swift
@MainActor
var maximumLinearExposure: CGFloat { get set }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorwell/maximumlinearexposure)*