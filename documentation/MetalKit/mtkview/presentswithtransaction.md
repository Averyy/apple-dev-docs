# presentsWithTransaction

**Framework**: MetalKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the view presents its content using a Core Animation transaction.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var presentsWithTransaction: Bool { get set }
```

```objc
@property (nonatomic) BOOL presentsWithTransaction;
```

## Discussion

This property mirrors the value on the underlying [`CAMetalLayer`](../../QuartzCore/cametallayer.md) object, and determines whether the view synchronizes updates to its own contents with other content changes in Core Animation. For more information about how this property affects your rendering code, see [`presentsWithTransaction`](../../QuartzCore/cametallayer/presentswithtransaction.md).

## See Also

### Configuring Drawing Behavior
- [var preferredFramesPerSecond: Int](./preferredframespersecond.md)
  The rate at which the view redraws its contents.
- [var isPaused: Bool](./ispaused.md)
  A Boolean value that indicates whether the draw loop is paused.
- [var enableSetNeedsDisplay: Bool](./enablesetneedsdisplay.md)
  A Boolean value that indicates whether the view responds to [`setNeedsDisplay()`](../../UIKit/uiview/setneedsdisplay%28%29.md).
- [func draw()](./draw%28%29.md)
  Redraws the view’s contents immediately.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtkview/presentswithtransaction)*