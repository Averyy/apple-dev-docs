# keyUp(with:)

**Framework**: AppKit  
**Kind**: method

Informs the receiver that the user has released a key.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func keyUp(with event: NSEvent)
```

#### Discussion

The default implementation simply passes this message to the next responder.

## Parameters

- `event`: An object encapsulating information about the key-up event.

## See Also

- [func keyDown(with: NSEvent)](nsresponder/keydown(with:).md)
  Informs the receiver that the user has pressed a key.
- [func interpretKeyEvents([NSEvent])](nsresponder/interpretkeyevents(_:).md)
  Handles a series of key events.
- [func performKeyEquivalent(with: NSEvent) -> Bool](nsresponder/performkeyequivalent(with:).md)
  Handle a key equivalent.
- [func flushBufferedKeyEvents()](nsresponder/flushbufferedkeyevents.md)
  Clears any unprocessed key events when overridden by subclasses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsresponder/keyup(with:))*