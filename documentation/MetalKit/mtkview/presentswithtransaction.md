# presentsWithTransaction

**Framework**: MetalKit  
**Kind**: property

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

#### Discussion

This property mirrors the value on the underlying [`CAMetalLayer`](https://developer.apple.com/documentation/quartzcore/cametallayer) object, and determines whether the view synchronizes updates to its own contents with other content changes in Core Animation. For more information about how this property affects your rendering code, see [`presentsWithTransaction`](https://developer.apple.com/documentation/quartzcore/cametallayer/presentswithtransaction).

## See Also

- [var preferredFramesPerSecond: Int](mtkview/preferredframespersecond.md)
  The rate at which the view redraws its contents.
- [var isPaused: Bool](mtkview/ispaused.md)
  A Boolean value that indicates whether the draw loop is paused.
- [var enableSetNeedsDisplay: Bool](mtkview/enablesetneedsdisplay.md)
  A Boolean value that indicates whether the view responds to [`setNeedsDisplay()`](https://developer.apple.com/documentation/uikit/uiview/setneedsdisplay()).
- [func draw()](mtkview/draw.md)
  Redraws the view’s contents immediately.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtkview/presentswithtransaction)*