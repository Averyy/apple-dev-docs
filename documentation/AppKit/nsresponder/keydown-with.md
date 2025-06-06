# keyDown(with:)

**Framework**: AppKit  
**Kind**: method

Informs the receiver that the user has pressed a key.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func keyDown(with event: NSEvent)
```

#### Discussion

The receiver can interpret `event` itself, or pass it to the system input manager using [`interpretKeyEvents(_:)`](nsresponder/interpretkeyevents(_:).md). The default implementation simply passes this message to the next responder.

## Parameters

- `event`: An object encapsulating information about the key-down event.

## See Also

- [func keyUp(with: NSEvent)](nsresponder/keyup(with:).md)
  Informs the receiver that the user has released a key.
- [func interpretKeyEvents([NSEvent])](nsresponder/interpretkeyevents(_:).md)
  Handles a series of key events.
- [func performKeyEquivalent(with: NSEvent) -> Bool](nsresponder/performkeyequivalent(with:).md)
  Handle a key equivalent.
- [func flushBufferedKeyEvents()](nsresponder/flushbufferedkeyevents.md)
  Clears any unprocessed key events when overridden by subclasses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsresponder/keydown(with:))*