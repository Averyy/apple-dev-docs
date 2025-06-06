# adjustViewport(byVerticalOffset:)

**Framework**: UIKit  
**Kind**: method

Adjusts the viewport rect by the specified offset if needed.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func adjustViewport(byVerticalOffset verticalOffset: CGFloat)
```

## Parameters

- `verticalOffset`: A   that represents the offset amount to apply to the viewport.

## See Also

- [var viewportBounds: CGRect](nstextviewportlayoutcontroller/viewportbounds.md)
  Returns the visible bounds of the view, plus the overdraw area.
- [var viewportRange: NSTextRange?](nstextviewportlayoutcontroller/viewportrange.md)
  Returns the text range of the current viewport layout.
- [func layoutViewport()](nstextviewportlayoutcontroller/layoutviewport.md)
  Performs layout in the viewport.
- [func relocateViewport(to: any NSTextLocation) -> CGFloat](nstextviewportlayoutcontroller/relocateviewport(to:).md)
  Relocates the viewport to the location you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextviewportlayoutcontroller/adjustviewport(byverticaloffset:))*