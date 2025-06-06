# touchesCancelled(with:)

**Framework**: AppKit  
**Kind**: method

Called when a system event, such as a low-memory warning, cancels an in-progress touch event in an [`NSTouchBar`](nstouchbar.md) object.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
@MainActor
func touchesCancelled(with event: NSEvent)
```

## See Also

- [func touchesBegan(with: NSEvent)](nsgesturerecognizer/touchesbegan(with:).md)
  Called when one or more fingers first make contact with an [`NSTouchBar`](nstouchbar.md) instance on the Touch Bar.
- [func touchesEnded(with: NSEvent)](nsgesturerecognizer/touchesended(with:).md)
  Called when one or more fingers are removed from contact with an [`NSTouchBar`](nstouchbar.md) instance on the Touch Bar.
- [func touchesMoved(with: NSEvent)](nsgesturerecognizer/touchesmoved(with:).md)
  Called when one or more fingers, associated with an in-progress event, move within an [`NSTouchBar`](nstouchbar.md) instance on the Touch Bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgesturerecognizer/touchescancelled(with:))*