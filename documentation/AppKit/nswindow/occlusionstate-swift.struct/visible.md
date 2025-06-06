# visible

**Framework**: AppKit  
**Kind**: property

If set, at least part of the window is visible; if not set, the entire window is occluded. A window that has a nonrectangular shape can be entirely occluded onscreen, but if its bounding box falls into a visible region, the window is considered to be visible. Note that a completely transparent window may also be considered visible.

**Availability**:
- macOS 10.9+

## Declaration

```swift
static var visible: NSWindow.OcclusionState { get }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/occlusionstate-swift.struct/visible)*