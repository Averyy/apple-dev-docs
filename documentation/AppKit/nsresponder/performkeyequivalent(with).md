# performKeyEquivalent(with:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Handle a key equivalent.

**Availability**:
- macOS

## Declaration

```swift
func performKeyEquivalent(with event: NSEvent) -> Bool
```

```objc
- (BOOL) performKeyEquivalent:(NSEvent *) event;
```

#### Discussion

Override to handle key equivalents. If the character code or codes in `event` match the receiver’s key equivalent, the receiver should respond to the event and return [`true`](../../Swift/true.md). The default implementation does nothing and returns [`false`](../../Swift/false.md).

> **Note**:  [`performKeyEquivalent(with:)`](./performkeyequivalent%28with%29.md) takes an [`NSEvent`](../nsevent.md) object as its argument, while [`performMnemonic:`](./performmnemonic_.md) takes an [`NSString`](../../Foundation/nsstring.md) object containing the uninterpreted characters of the key event. You should extract the characters for a key equivalent using the `NSEvent` method  [`charactersIgnoringModifiers`](../nsevent/charactersignoringmodifiers.md).

## Parameters

- `event`: An event object that represents the key equivalent pressed.

## See Also

### Related Documentation
- [func performKeyEquivalent(with: NSEvent) -> Bool](../nsview/performkeyequivalent%28with%29.md)
  Implemented by subclasses to respond to key equivalents (also known as keyboard shortcuts).
- [func performKeyEquivalent(with: NSEvent) -> Bool](../nsbutton/performkeyequivalent%28with%29.md)
  Checks the button’s key equivalent against the specified event and, if they match, simulates the button being clicked.
### Responding to Key Events
- [func keyDown(with: NSEvent)](./keydown%28with%29.md)
  Informs the receiver that the user has pressed a key.
- [func keyUp(with: NSEvent)](./keyup%28with%29.md)
  Informs the receiver that the user has released a key.
- [func interpretKeyEvents([NSEvent])](./interpretkeyevents%28_%29.md)
  Handles a series of key events.
- [func flushBufferedKeyEvents()](./flushbufferedkeyevents%28%29.md)
  Clears any unprocessed key events when overridden by subclasses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsresponder/performkeyequivalent(with:))*