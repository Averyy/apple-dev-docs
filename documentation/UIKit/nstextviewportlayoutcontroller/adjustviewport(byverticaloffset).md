# adjustViewport(byVerticalOffset:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) adjustViewportByVerticalOffset:(CGFloat) verticalOffset;
```

## Parameters

- `verticalOffset`: A `CGFloat` that represents the offset amount to apply to the viewport.

## See Also

### Accessing the viewport characteristics
- [var viewportBounds: CGRect](./viewportbounds.md)
  Returns the visible bounds of the view, plus the overdraw area.
- [var viewportRange: NSTextRange?](./viewportrange.md)
  Returns the text range of the current viewport layout.
- [func layoutViewport()](./layoutviewport%28%29.md)
  Performs layout in the viewport.
- [func relocateViewport(to: any NSTextLocation) -> CGFloat](./relocateviewport%28to%29.md)
  Relocates the viewport to the location you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextviewportlayoutcontroller/adjustviewport(byverticaloffset:))*