# layoutViewport()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Performs layout in the viewport.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func layoutViewport()
```

```objc
- (void) layoutViewport;
```

## Mentions

- [Managing viewport layout and attachment reuse in text views](../managing-viewport-layout-and-attachment-reuse-in-a-text-view-subclass.md)

## See Also

### Accessing the viewport characteristics
- [var viewportBounds: CGRect](./viewportbounds.md)
  Returns the visible bounds of the view, plus the overdraw area.
- [var viewportRange: NSTextRange?](./viewportrange.md)
  Returns the text range of the current viewport layout.
- [func adjustViewport(byVerticalOffset: CGFloat)](./adjustviewport%28byverticaloffset%29.md)
  Adjusts the viewport rect by the specified offset if needed.
- [func relocateViewport(to: any NSTextLocation) -> CGFloat](./relocateviewport%28to%29.md)
  Relocates the viewport to the location you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextviewportlayoutcontroller/layoutviewport())*