# viewportRange

**Framework**: UIKit  
**Kind**: property

Returns the text range of the current viewport layout.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var viewportRange: NSTextRange? { get }
```

## See Also

- [var viewportBounds: CGRect](nstextviewportlayoutcontroller/viewportbounds.md)
  Returns the visible bounds of the view, plus the overdraw area.
- [func adjustViewport(byVerticalOffset: CGFloat)](nstextviewportlayoutcontroller/adjustviewport(byverticaloffset:).md)
  Adjusts the viewport rect by the specified offset if needed.
- [func layoutViewport()](nstextviewportlayoutcontroller/layoutviewport.md)
  Performs layout in the viewport.
- [func relocateViewport(to: any NSTextLocation) -> CGFloat](nstextviewportlayoutcontroller/relocateviewport(to:).md)
  Relocates the viewport to the location you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextviewportlayoutcontroller/viewportrange)*