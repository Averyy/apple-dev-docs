# sendAction(_:to:from:)

**Framework**: AppKit  
**Kind**: method

Sends the given action message to the given target.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func sendAction(_ action: Selector, to target: Any?, from sender: Any?) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the action was successfully sent; otherwise [`false`](https://developer.apple.com/documentation/Swift/false). This method also returns [`false`](https://developer.apple.com/documentation/Swift/false) if `anAction` is `nil`.

#### Discussion

If `aTarget` is `nil`, [`shared`](nsapplication/shared.md) looks for an object that can respond to the message—that is, an object that implements a method matching `anAction`. It begins with the first responder of the key window. If the first responder can’t respond, it tries the first responder’s next responder and continues following next responder links up the responder chain. If none of the objects in the key window’s responder chain can handle the message, [`shared`](nsapplication/shared.md) attempts to send the message to the key window’s delegate.

If the delegate doesn’t respond and the main window is different from the key window, [`shared`](nsapplication/shared.md) begins again with the first responder in the main window. If objects in the main window can’t respond, [`shared`](nsapplication/shared.md) attempts to send the message to the main window’s delegate. If still no object has responded, [`shared`](nsapplication/shared.md) tries to handle the message itself. If [`shared`](nsapplication/shared.md) can’t respond, it attempts to send the message to its own delegate.

## Parameters

- `action`: The action message you want to send.
- `target`: The target object that defines the specified action message.
- `sender`: The object to pass for the action message’s parameter.

## See Also

- [func makeWindowsPerform(Selector, inOrder: Bool) -> NSWindow?](nsapplication/makewindowsperform(_:inorder:).md)
  Sends the specified message to each of the app’s window objects until one returns a non-`nil` value.
- [func tryToPerform(Selector, with: Any?) -> Bool](nsapplication/trytoperform(_:with:).md)
  Dispatches an action message to the specified target.
- [func target(forAction: Selector) -> Any?](nsapplication/target(foraction:).md)
  Returns the object that receives the action message specified by the given selector.
- [func target(forAction: Selector, to: Any?, from: Any?) -> Any?](nsapplication/target(foraction:to:from:).md)
  Searches for an object that can receive the message specified by the given selector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/sendaction(_:to:from:))*