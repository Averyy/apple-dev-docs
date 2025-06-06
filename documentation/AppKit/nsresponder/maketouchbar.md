# makeTouchBar()

**Framework**: AppKit  
**Kind**: method

Your custom subclass of the `NSResponder` class should override this method to create and configure your subclass’s default [`NSTouchBar`](nstouchbar.md) object.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
@MainActor
func makeTouchBar() -> NSTouchBar?
```

## See Also

- [var touchBar: NSTouchBar?](nsresponder/touchbar.md)
  The [`NSTouchBar`](nstouchbar.md) object associated with the responder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsresponder/maketouchbar())*