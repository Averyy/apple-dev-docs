# isPaused

**Framework**: MetalKit  
**Kind**: property  
**Role**: Instance Property

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
var isPaused: Bool { get set }
```

```objc
@property (nonatomic, getter=isPaused) BOOL paused;
```

#### Discussion

If the value is [`false`](../../Swift/false.md), the view periodically redraws the contents, at a frame rate set by the value of [`preferredFramesPerSecond`](./preferredframespersecond.md).

The default value is [`false`](../../Swift/false.md).

## See Also

### Configuring Drawing Behavior
- [var preferredFramesPerSecond: Int](./preferredframespersecond.md)
  The rate at which the view redraws its contents.
- [var enableSetNeedsDisplay: Bool](./enablesetneedsdisplay.md)
  A Boolean value that indicates whether the view responds to [`setNeedsDisplay()`](../../UIKit/uiview/setneedsdisplay%28%29.md).
- [func draw()](./draw%28%29.md)
  Redraws the view’s contents immediately.
- [var presentsWithTransaction: Bool](./presentswithtransaction.md)
  A Boolean value that determines whether the view presents its content using a Core Animation transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtkview/ispaused)*