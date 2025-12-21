# sourceRect

**Framework**: ScreenCaptureKit  
**Kind**: property

A rectangle that specifies that the screenshot only samples a subset of the frame input.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
var sourceRect: CGRect { get set }
```

#### Discussion

If not set, the screenshot captures the entire frame. Specify the rectangle in points in the display’s logical coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scscreenshotconfiguration/sourcerect)*