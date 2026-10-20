# flushBufferedKeyEvents()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Clears any unprocessed key events when overridden by subclasses.

**Availability**:
- macOS

## Declaration

```swift
func flushBufferedKeyEvents()
```

```objc
- (void) flushBufferedKeyEvents;
```

## See Also

### Responding to Key Events
- [func keyDown(with: NSEvent)](./keydown%28with%29.md)
  Informs the receiver that the user has pressed a key.
- [func keyUp(with: NSEvent)](./keyup%28with%29.md)
  Informs the receiver that the user has released a key.
- [func interpretKeyEvents([NSEvent])](./interpretkeyevents%28_%29.md)
  Handles a series of key events.
- [func performKeyEquivalent(with: NSEvent) -> Bool](./performkeyequivalent%28with%29.md)
  Handle a key equivalent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsresponder/flushbufferedkeyevents())*