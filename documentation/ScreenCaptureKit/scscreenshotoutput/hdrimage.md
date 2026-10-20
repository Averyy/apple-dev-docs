# hdrImage

**Framework**: ScreenCaptureKit  
**Kind**: property  
**Role**: Instance Property

An output property that specifies the high dynamic range version of the screenshot.

**Availability**:
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
var hdrImage: CGImage? { get set }
```

```objc
@property (nonatomic, strong, nullable) CGImageRef hdrImage;
```

#### Discussion

The output [`CGImage`](../../CoreGraphics/cgimage.md) uses the extended sRGB color space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scscreenshotoutput/hdrimage)*