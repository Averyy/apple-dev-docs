# occlusionState

**Framework**: AppKit  
**Kind**: property

The occlusion state of the window.

**Availability**:
- macOS 10.9+

## Declaration

```swift
@MainActor
var occlusionState: NSWindow.OcclusionState { get }
```

#### Discussion

When the value of this property is [`visible`](nswindow/occlusionstate-swift.struct/visible.md), at least part of the window is visible; otherwise, the window is fully occluded.

## See Also

- [var isVisible: Bool](nswindow/isvisible.md)
  A Boolean value that indicates whether the window is visible onscreen (even when it’s obscured by other windows).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/occlusionstate-swift.property)*