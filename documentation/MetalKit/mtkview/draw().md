# draw()

**Framework**: MetalKit  
**Kind**: method  
**Role**: Instance Method

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
func draw()
```

```objc
- (void) draw;
```

#### Discussion

This method manually tells the view to redraw its contents. Calling this method causes the view to call either the [`draw(in:)`](../mtkviewdelegate/draw%28in%29.md) method of the view’s [`delegate`](./delegate.md), or the [`draw(_:)`](../../UIKit/uiview/draw%28_%29.md) method of the [`MTKView`](../mtkview.md) subclass. Never call this method inside either drawing function.

## See Also

### Configuring Drawing Behavior
- [var preferredFramesPerSecond: Int](./preferredframespersecond.md)
  The rate at which the view redraws its contents.
- [var isPaused: Bool](./ispaused.md)
  A Boolean value that indicates whether the draw loop is paused.
- [var enableSetNeedsDisplay: Bool](./enablesetneedsdisplay.md)
  A Boolean value that indicates whether the view responds to [`setNeedsDisplay()`](../../UIKit/uiview/setneedsdisplay%28%29.md).
- [var presentsWithTransaction: Bool](./presentswithtransaction.md)
  A Boolean value that determines whether the view presents its content using a Core Animation transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtkview/draw())*