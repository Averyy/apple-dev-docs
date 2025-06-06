# target(forAction:)

**Framework**: AppKit  
**Kind**: method

Returns the object that receives the action message specified by the given selector.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func target(forAction action: Selector) -> Any?
```

#### Return Value

The object that would receive the specified action message or `nil` if no target object would receive the message. This method also returns `nil` if `aSelector` is `nil`.

## Parameters

- `action`: The desired action message.

## See Also

- [func tryToPerform(Selector, with: Any?) -> Bool](nsapplication/trytoperform(_:with:).md)
  Dispatches an action message to the specified target.
- [func sendAction(Selector, to: Any?, from: Any?) -> Bool](nsapplication/sendaction(_:to:from:).md)
  Sends the given action message to the given target.
- [func target(forAction: Selector, to: Any?, from: Any?) -> Any?](nsapplication/target(foraction:to:from:).md)
  Searches for an object that can receive the message specified by the given selector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/target(foraction:))*