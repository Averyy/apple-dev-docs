# draw()

**Framework**: MetalKit  
**Kind**: method

Redraws the view’s contents immediately.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func draw()
```

#### Discussion

This method manually tells the view to redraw its contents. Calling this method causes the view to call either the [`draw(in:)`](mtkviewdelegate/draw(in:).md) method of the view’s [`delegate`](mtkview/delegate.md), or the [`draw(_:)`](https://developer.apple.com/documentation/UIKit/UIView/draw(_:)) method of the [`MTKView`](mtkview.md) subclass. Never call this method inside either drawing function.

## See Also

- [var preferredFramesPerSecond: Int](mtkview/preferredframespersecond.md)
  The rate at which the view redraws its contents.
- [var isPaused: Bool](mtkview/ispaused.md)
  A Boolean value that indicates whether the draw loop is paused.
- [var enableSetNeedsDisplay: Bool](mtkview/enablesetneedsdisplay.md)
  A Boolean value that indicates whether the view responds to [`setNeedsDisplay()`](https://developer.apple.com/documentation/UIKit/UIView/setNeedsDisplay()).
- [var presentsWithTransaction: Bool](mtkview/presentswithtransaction.md)
  A Boolean value that determines whether the view presents its content using a Core Animation transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtkview/draw())*