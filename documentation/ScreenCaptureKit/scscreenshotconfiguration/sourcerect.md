# sourceRect

**Framework**: ScreenCaptureKit  
**Kind**: property  
**Role**: Instance Property

A rectangle that specifies that the screenshot only samples a subset of the frame input.

**Availability**:
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
var sourceRect: CGRect { get set }
```

```objc
@property (nonatomic, assign) CGRect sourceRect;
```

## Discussion

If not set, the screenshot captures the entire frame. Specify the rectangle in points in the display’s logical coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scscreenshotconfiguration/sourcerect)*