# relocateViewport(to:)

**Framework**: UIKit  
**Kind**: method

Relocates the viewport to the location you specify.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func relocateViewport(to textLocation: any NSTextLocation) -> CGFloat
```

## Parameters

- `textLocation`: An  .

## See Also

- [var viewportBounds: CGRect](nstextviewportlayoutcontroller/viewportbounds.md)
  Returns the visible bounds of the view, plus the overdraw area.
- [var viewportRange: NSTextRange?](nstextviewportlayoutcontroller/viewportrange.md)
  Returns the text range of the current viewport layout.
- [func adjustViewport(byVerticalOffset: CGFloat)](nstextviewportlayoutcontroller/adjustviewport(byverticaloffset:).md)
  Adjusts the viewport rect by the specified offset if needed.
- [func layoutViewport()](nstextviewportlayoutcontroller/layoutviewport.md)
  Performs layout in the viewport.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextviewportlayoutcontroller/relocateviewport(to:))*