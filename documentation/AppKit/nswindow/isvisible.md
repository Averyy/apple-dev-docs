# isVisible

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the window is visible onscreen (even when it’s obscured by other windows).

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var isVisible: Bool { get }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/swift/true) when the window is onscreen (even if it’s obscured by other windows); otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var visibleRect: NSRect](nsview/visiblerect.md)
  The portion of the view that isn’t clipped by its superviews.
- [var occlusionState: NSWindow.OcclusionState](nswindow/occlusionstate-swift.property.md)
  The occlusion state of the window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/isvisible)*