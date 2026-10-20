# mouseCancelled(with:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- macOS 26.0+

## Declaration

```swift
func mouseCancelled(with event: NSEvent)
```

```objc
- (void) mouseCancelled:(NSEvent *) event;
```

## See Also

### Handling touch and mouse events
- [func touchesBegan(with: NSEvent)](./touchesbegan%28with%29.md)
  Called when one or more fingers first make contact with an [`NSTouchBar`](../nstouchbar.md) instance on the Touch Bar.
- [func touchesCancelled(with: NSEvent)](./touchescancelled%28with%29.md)
  Called when a system event, such as a low-memory warning, cancels an in-progress touch event in an [`NSTouchBar`](../nstouchbar.md) object.
- [func touchesEnded(with: NSEvent)](./touchesended%28with%29.md)
  Called when one or more fingers are removed from contact with an [`NSTouchBar`](../nstouchbar.md) instance on the Touch Bar.
- [func touchesMoved(with: NSEvent)](./touchesmoved%28with%29.md)
  Called when one or more fingers, associated with an in-progress event, move within an [`NSTouchBar`](../nstouchbar.md) instance on the Touch Bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgesturerecognizer/mousecancelled(with:))*