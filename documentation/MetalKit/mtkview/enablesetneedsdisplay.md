# enableSetNeedsDisplay

**Framework**: MetalKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the view responds to [`setNeedsDisplay()`](../../UIKit/uiview/setneedsdisplay%28%29.md).

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var enableSetNeedsDisplay: Bool { get set }
```

```objc
@property (nonatomic) BOOL enableSetNeedsDisplay;
```

#### Discussion

If this value and the value of [`isPaused`](./ispaused.md) are [`true`](../../Swift/true.md), the view behaves similarly to a [`UIView`](../../UIKit/uiview.md) object, responding to calls to [`setNeedsDisplay()`](../../UIKit/uiview/setneedsdisplay%28%29.md). In this case, the view’s internal draw loop is paused and updates are event-driven instead.

The default value is [`false`](../../Swift/false.md).

## See Also

### Configuring Drawing Behavior
- [var preferredFramesPerSecond: Int](./preferredframespersecond.md)
  The rate at which the view redraws its contents.
- [var isPaused: Bool](./ispaused.md)
  A Boolean value that indicates whether the draw loop is paused.
- [func draw()](./draw%28%29.md)
  Redraws the view’s contents immediately.
- [var presentsWithTransaction: Bool](./presentswithtransaction.md)
  A Boolean value that determines whether the view presents its content using a Core Animation transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtkview/enablesetneedsdisplay)*