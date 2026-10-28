# keyDown(with:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Informs the receiver that the user has pressed a key.

**Availability**:
- macOS

## Declaration

```swift
func keyDown(with event: NSEvent)
```

```objc
- (void) keyDown:(NSEvent *) event;
```

## Discussion

The receiver can interpret `event` itself, or pass it to the system input manager using [`interpretKeyEvents(_:)`](./interpretkeyevents%28_%29.md). The default implementation simply passes this message to the next responder.

## Parameters

- `event`: An object encapsulating information about the key-down event.

## See Also

### Responding to Key Events
- [func keyUp(with: NSEvent)](./keyup%28with%29.md)
  Informs the receiver that the user has released a key.
- [func interpretKeyEvents([NSEvent])](./interpretkeyevents%28_%29.md)
  Handles a series of key events.
- [func performKeyEquivalent(with: NSEvent) -> Bool](./performkeyequivalent%28with%29.md)
  Handle a key equivalent.
- [func flushBufferedKeyEvents()](./flushbufferedkeyevents%28%29.md)
  Clears any unprocessed key events when overridden by subclasses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsresponder/keydown(with:))*