# target(forAction:to:from:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Searches for an object that can receive the message specified by the given selector.

**Availability**:
- macOS

## Declaration

```swift
func target(forAction action: Selector, to target: Any?, from sender: Any?) -> Any?
```

```objc
- (id) targetForAction:(SEL) action to:(id) target from:(id) sender;
```

#### Return Value

The object that can accept the specified action message or `nil` if no target object can receive the message from the specified `sender`. Returns `nil` if `anAction` is `nil`.

#### Discussion

The system looks for an object that implements a method matching `anAction`.

If `aTarget` is specified, the system verifies that it’s a valid target for the provided action and sender, returning `aTarget` if valid, `nil` otherwise.

If the provided target is `nil`, the search begins with the first responder of the key window. The system follows the responder object looking for targets. If no object capable of handling the message is found in the responder chain, the system returns `nil`.

## Parameters

- `action`: The desired action message. May be `nil`, in which case this method will return `nil`.
- `target`: The target object to check. Specify `nil` if you want to search the responder chain starting with the current first responder.
- `sender`: The potential sender for the action message.

## See Also

### Posting actions
- [func tryToPerform(Selector, with: Any?) -> Bool](./trytoperform%28_,with%29.md)
  Dispatches an action message to the specified target.
- [func sendAction(Selector, to: Any?, from: Any?) -> Bool](./sendaction%28_,to,from%29.md)
  Sends the given action message to the given target.
- [func target(forAction: Selector) -> Any?](./target%28foraction%29.md)
  Returns the object that receives the action message specified by the given selector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/target(foraction:to:from:))*