# viewportBounds

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Returns the visible bounds of the view, plus the overdraw area.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var viewportBounds: CGRect { get }
```

```objc
@property (readonly) CGRect viewportBounds;
```

## See Also

### Accessing the viewport characteristics
- [var viewportRange: NSTextRange?](./viewportrange.md)
  Returns the text range of the current viewport layout.
- [func adjustViewport(byVerticalOffset: CGFloat)](./adjustviewport%28byverticaloffset%29.md)
  Adjusts the viewport rect by the specified offset if needed.
- [func layoutViewport()](./layoutviewport%28%29.md)
  Performs layout in the viewport.
- [func relocateViewport(to: any NSTextLocation) -> CGFloat](./relocateviewport%28to%29.md)
  Relocates the viewport to the location you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextviewportlayoutcontroller/viewportbounds)*