# layoutViewport()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Performs layout in the viewport.

**Availability**:
- macOS 12.0+

## Declaration

```swift
func layoutViewport()
```

```objc
- (void) layoutViewport;
```

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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextviewportlayoutcontroller/layoutviewport())*