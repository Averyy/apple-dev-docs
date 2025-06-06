# hitPart

**Framework**: AppKit  
**Kind**: property

A part code indicating the manner in which the scrolling should be performed.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var hitPart: NSScroller.Part { get }
```

#### Discussion

This method is typically invoked by an [`NSScrollView`](nsscrollview.md) object to determine how to scroll its document view when it receives an action message from the scroller.

See [`NSScroller.Part`](nsscroller/part.md) for a list of part codes. In macOS 10.7 and later, this method no longer returns [`NSScroller.Part.incrementLine`](nsscroller/part/incrementline.md) or [`NSScroller.Part.decrementLine`](nsscroller/part/decrementline.md).

## See Also

- [func trackKnob(with: NSEvent)](nsscroller/trackknob(with:).md)
  Tracks the knob and sends action messages to the receiver’s target.
- [func trackScrollButtons(with: NSEvent)](nsscroller/trackscrollbuttons(with:).md)
  Tracks the scroll buttons and sends action messages to the receiver’s target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscroller/hitpart)*