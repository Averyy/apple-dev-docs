# touchesEnded(with:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Called when one or more fingers are removed from contact with an [`NSTouchBar`](../nstouchbar.md) instance on the Touch Bar.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
func touchesEnded(with event: NSEvent)
```

```objc
- (void) touchesEndedWithEvent:(NSEvent *) event;
```

## See Also

### Handling touch and mouse events
- [func touchesBegan(with: NSEvent)](./touchesbegan%28with%29.md)
  Called when one or more fingers first make contact with an [`NSTouchBar`](../nstouchbar.md) instance on the Touch Bar.
- [func touchesCancelled(with: NSEvent)](./touchescancelled%28with%29.md)
  Called when a system event, such as a low-memory warning, cancels an in-progress touch event in an [`NSTouchBar`](../nstouchbar.md) object.
- [func touchesMoved(with: NSEvent)](./touchesmoved%28with%29.md)
  Called when one or more fingers, associated with an in-progress event, move within an [`NSTouchBar`](../nstouchbar.md) instance on the Touch Bar.
- [func mouseCancelled(with: NSEvent)](./mousecancelled%28with%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgesturerecognizer/touchesended(with:))*