# performKeyEquivalent(with:)

**Framework**: AppKit  
**Kind**: method

Handle a key equivalent.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func performKeyEquivalent(with event: NSEvent) -> Bool
```

#### Discussion

Override to handle key equivalents. If the character code or codes in `event` match the receiver’s key equivalent, the receiver should respond to the event and return [`true`](https://developer.apple.com/documentation/swift/true). The default implementation does nothing and returns [`false`](https://developer.apple.com/documentation/swift/false).

> **Note**:  [`performKeyEquivalent(with:)`](nsresponder/performkeyequivalent(with:).md) takes an [`NSEvent`](nsevent.md) object as its argument, while [`performMnemonic:`](nsresponder/performmnemonic:.md) takes an [`NSString`](https://developer.apple.com/documentation/Foundation/NSString) object containing the uninterpreted characters of the key event. You should extract the characters for a key equivalent using the `NSEvent` method  [`charactersIgnoringModifiers`](nsevent/charactersignoringmodifiers.md).

## Parameters

- `event`: An event object that represents the key equivalent pressed.

## See Also

- [func performKeyEquivalent(with: NSEvent) -> Bool](nsview/performkeyequivalent(with:).md)
  Implemented by subclasses to respond to key equivalents (also known as keyboard shortcuts).
- [func performKeyEquivalent(with: NSEvent) -> Bool](nsbutton/performkeyequivalent(with:).md)
  Checks the button’s key equivalent against the specified event and, if they match, simulates the button being clicked.
- [func keyDown(with: NSEvent)](nsresponder/keydown(with:).md)
  Informs the receiver that the user has pressed a key.
- [func keyUp(with: NSEvent)](nsresponder/keyup(with:).md)
  Informs the receiver that the user has released a key.
- [func interpretKeyEvents([NSEvent])](nsresponder/interpretkeyevents(_:).md)
  Handles a series of key events.
- [func flushBufferedKeyEvents()](nsresponder/flushbufferedkeyevents.md)
  Clears any unprocessed key events when overridden by subclasses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsresponder/performkeyequivalent(with:))*