# interpretKeyEvents(_:)

**Framework**: AppKit  
**Kind**: method

Handles a series of key events.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func interpretKeyEvents(_ eventArray: [NSEvent])
```

#### Discussion

This method, which is invoked by subclasses from the [`keyDown(with:)`](nsresponder/keydown(with:).md) method, sends the character input in `eventArray` to the system input manager for interpretation as text to insert or commands to perform. The input manager responds to the request by sending [`insertText(_:)`](nsstandardkeybindingresponding/inserttext(_:).md) and [`doCommand(by:)`](nsstandardkeybindingresponding/docommand(by:).md) messages back to the invoker of this method. Subclasses shouldn’t override this method.

See the [`NSInputManager`](nsinputmanager.md) and [`NSTextInput`](nstextinput.md) class and protocol specifications for more information on input management.

## Parameters

- `eventArray`: An array of key-event characters to give to the system input manager.

## See Also

- [func keyDown(with: NSEvent)](nsresponder/keydown(with:).md)
  Informs the receiver that the user has pressed a key.
- [func keyUp(with: NSEvent)](nsresponder/keyup(with:).md)
  Informs the receiver that the user has released a key.
- [func performKeyEquivalent(with: NSEvent) -> Bool](nsresponder/performkeyequivalent(with:).md)
  Handle a key equivalent.
- [func flushBufferedKeyEvents()](nsresponder/flushbufferedkeyevents.md)
  Clears any unprocessed key events when overridden by subclasses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsresponder/interpretkeyevents(_:))*