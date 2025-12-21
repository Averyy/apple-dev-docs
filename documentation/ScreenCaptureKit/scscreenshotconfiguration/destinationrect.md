# destinationRect

**Framework**: ScreenCaptureKit  
**Kind**: property

A rectangle that specifies whether to output screenshots in a subset of the output image.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
var destinationRect: CGRect { get set }
```

#### Discussion

If you don’t specify a destination rectangle, the system uses the full dimensions of the output surface. The rectangle is specified in pixels in the display’s coordinate system.

> **Note**: The system doesn’t reference this value when capturing a single window because it draws the window into the output’s full bounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scscreenshotconfiguration/destinationrect)*