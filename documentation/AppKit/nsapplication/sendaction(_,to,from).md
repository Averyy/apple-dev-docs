# sendAction(_:to:from:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sends the given action message to the given target.

**Availability**:
- macOS

## Declaration

```swift
func sendAction(_ action: Selector, to target: Any?, from sender: Any?) -> Bool
```

```objc
- (BOOL) sendAction:(SEL) action to:(id) target from:(id) sender;
```

#### Return Value

[`true`](../../Swift/true.md) if the action was successfully sent; otherwise [`false`](../../Swift/false.md). This method also returns [`false`](../../Swift/false.md) if `anAction` is `nil`.

#### Discussion

If `aTarget` is `nil`, [`shared`](./shared.md) looks for an object that can respond to the message—that is, an object that implements a method matching `anAction`. It begins with the first responder of the key window. If the first responder can’t respond, it tries the first responder’s next responder and continues following next responder links up the responder chain. If none of the objects in the key window’s responder chain can handle the message, [`shared`](./shared.md) attempts to send the message to the key window’s delegate.

If the delegate doesn’t respond and the main window is different from the key window, [`shared`](./shared.md) begins again with the first responder in the main window. If objects in the main window can’t respond, [`shared`](./shared.md) attempts to send the message to the main window’s delegate. If still no object has responded, [`shared`](./shared.md) tries to handle the message itself. If [`shared`](./shared.md) can’t respond, it attempts to send the message to its own delegate.

## Parameters

- `action`: The action message you want to send.
- `target`: The target object that defines the specified action message.
- `sender`: The object to pass for the action message’s parameter.

## See Also

### Related Documentation
- [func makeWindowsPerform(Selector, inOrder: Bool) -> NSWindow?](./makewindowsperform%28_,inorder%29.md)
  Sends the specified message to each of the app’s window objects until one returns a non-`nil` value.
### Posting actions
- [func tryToPerform(Selector, with: Any?) -> Bool](./trytoperform%28_,with%29.md)
  Dispatches an action message to the specified target.
- [func target(forAction: Selector) -> Any?](./target%28foraction%29.md)
  Returns the object that receives the action message specified by the given selector.
- [func target(forAction: Selector, to: Any?, from: Any?) -> Any?](./target%28foraction,to,from%29.md)
  Searches for an object that can receive the message specified by the given selector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/sendaction(_:to:from:))*