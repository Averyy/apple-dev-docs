# flushBufferedKeyEvents()

**Framework**: AppKit  
**Kind**: method

Clears any unprocessed key events when overridden by subclasses.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func flushBufferedKeyEvents()
```

## See Also

- [func keyDown(with: NSEvent)](nsresponder/keydown(with:).md)
  Informs the receiver that the user has pressed a key.
- [func keyUp(with: NSEvent)](nsresponder/keyup(with:).md)
  Informs the receiver that the user has released a key.
- [func interpretKeyEvents([NSEvent])](nsresponder/interpretkeyevents(_:).md)
  Handles a series of key events.
- [func performKeyEquivalent(with: NSEvent) -> Bool](nsresponder/performkeyequivalent(with:).md)
  Handle a key equivalent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsresponder/flushbufferedkeyevents())*