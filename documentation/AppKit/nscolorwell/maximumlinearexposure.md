# maximumLinearExposure

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The maximum linear exposure a color in this color well can be set to. Defaults to 1 and ignores any value less than 1. If set to a value >= 2, the color picked for this well may have a linear exposure applied to it.

**Availability**:
- macOS 26.0+

## Declaration

```swift
var maximumLinearExposure: CGFloat { get set }
```

```objc
@property CGFloat maximumLinearExposure;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorwell/maximumlinearexposure)*