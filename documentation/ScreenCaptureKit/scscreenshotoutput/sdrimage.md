# sdrImage

**Framework**: ScreenCaptureKit  
**Kind**: property  
**Role**: Instance Property

An output property that specifies the standard dynamic range version of the screenshot.

**Availability**:
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
var sdrImage: CGImage? { get set }
```

```objc
@property (nonatomic, strong, nullable) CGImageRef sdrImage;
```

#### Discussion

The output [`CGImage`](../../CoreGraphics/cgimage.md) uses the same color space as the content capture display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scscreenshotoutput/sdrimage)*