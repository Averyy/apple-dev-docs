# relocateViewport(to:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (CGFloat) relocateViewportToTextLocation:(id<NSTextLocation>) textLocation;
```

## Parameters

- `textLocation`: An `NSTextLocation`.

## See Also

### Accessing the viewport characteristics
- [var viewportBounds: CGRect](./viewportbounds.md)
  Returns the visible bounds of the view, plus the overdraw area.
- [var viewportRange: NSTextRange?](./viewportrange.md)
  Returns the text range of the current viewport layout.
- [func adjustViewport(byVerticalOffset: CGFloat)](./adjustviewport%28byverticaloffset%29.md)
  Adjusts the viewport rect by the specified offset if needed.
- [func layoutViewport()](./layoutviewport%28%29.md)
  Performs layout in the viewport.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextviewportlayoutcontroller/relocateviewport(to:))*