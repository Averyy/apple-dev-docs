# keyUp(with:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Informs the receiver that the user has released a key.

**Availability**:
- macOS

## Declaration

```swift
func keyUp(with event: NSEvent)
```

```objc
- (void) keyUp:(NSEvent *) event;
```

#### Discussion

The default implementation simply passes this message to the next responder.

## Parameters

- `event`: An object encapsulating information about the key-up event.

## See Also

### Responding to Key Events
- [func keyDown(with: NSEvent)](./keydown%28with%29.md)
  Informs the receiver that the user has pressed a key.
- [func interpretKeyEvents([NSEvent])](./interpretkeyevents%28_%29.md)
  Handles a series of key events.
- [func performKeyEquivalent(with: NSEvent) -> Bool](./performkeyequivalent%28with%29.md)
  Handle a key equivalent.
- [func flushBufferedKeyEvents()](./flushbufferedkeyevents%28%29.md)
  Clears any unprocessed key events when overridden by subclasses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsresponder/keyup(with:))*