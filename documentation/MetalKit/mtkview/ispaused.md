# isPaused

**Framework**: MetalKit  
**Kind**: property

A Boolean value that indicates whether the draw loop is paused.

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
var isPaused: Bool { get set }
```

#### Discussion

If the value is [`false`](https://developer.apple.com/documentation/swift/false), the view periodically redraws the contents, at a frame rate set by the value of [`preferredFramesPerSecond`](mtkview/preferredframespersecond.md).

The default value is [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var preferredFramesPerSecond: Int](mtkview/preferredframespersecond.md)
  The rate at which the view redraws its contents.
- [var enableSetNeedsDisplay: Bool](mtkview/enablesetneedsdisplay.md)
  A Boolean value that indicates whether the view responds to [`setNeedsDisplay()`](https://developer.apple.com/documentation/UIKit/UIView/setNeedsDisplay()).
- [func draw()](mtkview/draw.md)
  Redraws the view’s contents immediately.
- [var presentsWithTransaction: Bool](mtkview/presentswithtransaction.md)
  A Boolean value that determines whether the view presents its content using a Core Animation transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtkview/ispaused)*