# enableSetNeedsDisplay

**Framework**: MetalKit  
**Kind**: property

A Boolean value that indicates whether the view responds to [`setNeedsDisplay()`](https://developer.apple.com/documentation/UIKit/UIView/setNeedsDisplay()).

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
var enableSetNeedsDisplay: Bool { get set }
```

#### Discussion

If this value and the value of [`isPaused`](mtkview/ispaused.md) are [`true`](https://developer.apple.com/documentation/Swift/true), the view behaves similarly to a [`UIView`](https://developer.apple.com/documentation/UIKit/UIView) object, responding to calls to [`setNeedsDisplay()`](https://developer.apple.com/documentation/UIKit/UIView/setNeedsDisplay()). In this case, the view’s internal draw loop is paused and updates are event-driven instead.

The default value is [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [var preferredFramesPerSecond: Int](mtkview/preferredframespersecond.md)
  The rate at which the view redraws its contents.
- [var isPaused: Bool](mtkview/ispaused.md)
  A Boolean value that indicates whether the draw loop is paused.
- [func draw()](mtkview/draw.md)
  Redraws the view’s contents immediately.
- [var presentsWithTransaction: Bool](mtkview/presentswithtransaction.md)
  A Boolean value that determines whether the view presents its content using a Core Animation transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtkview/enablesetneedsdisplay)*