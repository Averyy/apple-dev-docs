# hitPart

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A part code indicating the manner in which the scrolling should be performed.

**Availability**:
- macOS

## Declaration

```swift
var hitPart: NSScroller.Part { get }
```

```objc
@property (readonly) NSScrollerPart hitPart;
```

## Discussion

This method is typically invoked by an [`NSScrollView`](../nsscrollview.md) object to determine how to scroll its document view when it receives an action message from the scroller.

See [`NSScroller.Part`](./part.md) for a list of part codes. In macOS 10.7 and later, this method no longer returns [`NSScroller.Part.incrementLine`](./part/incrementline.md) or [`NSScroller.Part.decrementLine`](./part/decrementline.md).

## See Also

### Event Handling
- [func trackKnob(with: NSEvent)](./trackknob%28with%29.md)
  Tracks the knob and sends action messages to the receiver’s target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscroller/hitpart)*