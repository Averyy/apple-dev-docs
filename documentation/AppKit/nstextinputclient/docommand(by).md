# doCommand(by:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Invokes the action specified by the given selector.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func doCommand(by selector: Selector)
```

```objc
- (void) doCommandBySelector:(SEL) selector;
```

#### Discussion

If `selector` cannot be invoked, then `doCommandBySelector:` should not pass this message up the responder chain. `NSResponder` also implements this method, and it does forward uninvokable commands up the responder chain, but a text view should not. A text view implementing the `NSTextInputClient` protocol inherits from `NSView`, which inherits from `NSResponder`, so your implementation of this method will override the one in `NSResponder`. It should not call `super`.

## Parameters

- `selector`: The selector to invoke.

## See Also

### Related Documentation
- [func interpretKeyEvents([NSEvent])](../nsresponder/interpretkeyevents%28_%29.md)
  Handles a series of key events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextinputclient/docommand(by:))*