# target(forAction:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the object that receives the action message specified by the given selector.

**Availability**:
- macOS

## Declaration

```swift
func target(forAction action: Selector) -> Any?
```

```objc
- (id) targetForAction:(SEL) action;
```

## Return Value

The object that would receive the specified action message or `nil` if no target object would receive the message. This method also returns `nil` if `aSelector` is `nil`.

## Parameters

- `action`: The desired action message.

## See Also

### Posting actions
- [func tryToPerform(Selector, with: Any?) -> Bool](./trytoperform%28_,with%29.md)
  Dispatches an action message to the specified target.
- [func sendAction(Selector, to: Any?, from: Any?) -> Bool](./sendaction%28_,to,from%29.md)
  Sends the given action message to the given target.
- [func target(forAction: Selector, to: Any?, from: Any?) -> Any?](./target%28foraction,to,from%29.md)
  Searches for an object that can receive the message specified by the given selector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/target(foraction:))*