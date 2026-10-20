# interpretKeyEvents(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Handles a series of key events.

**Availability**:
- macOS

## Declaration

```swift
func interpretKeyEvents(_ eventArray: [NSEvent])
```

```objc
- (void) interpretKeyEvents:(NSArray<NSEvent *> *) eventArray;
```

#### Discussion

This method, which is invoked by subclasses from the [`keyDown(with:)`](./keydown%28with%29.md) method, sends the character input in `eventArray` to the system input manager for interpretation as text to insert or commands to perform. The input manager responds to the request by sending [`insertText(_:)`](../nsstandardkeybindingresponding/inserttext%28_%29.md) and [`doCommand(by:)`](../nsstandardkeybindingresponding/docommand%28by%29.md) messages back to the invoker of this method. Subclasses shouldn’t override this method.

See the [`NSInputManager`](../nsinputmanager.md) and [`NSTextInput`](../nstextinput.md) class and protocol specifications for more information on input management.

## Parameters

- `eventArray`: An array of key-event characters to give to the system input manager.

## See Also

### Responding to Key Events
- [func keyDown(with: NSEvent)](./keydown%28with%29.md)
  Informs the receiver that the user has pressed a key.
- [func keyUp(with: NSEvent)](./keyup%28with%29.md)
  Informs the receiver that the user has released a key.
- [func performKeyEquivalent(with: NSEvent) -> Bool](./performkeyequivalent%28with%29.md)
  Handle a key equivalent.
- [func flushBufferedKeyEvents()](./flushbufferedkeyevents%28%29.md)
  Clears any unprocessed key events when overridden by subclasses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsresponder/interpretkeyevents(_:))*