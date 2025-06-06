# tryToPerform(_:with:)

**Framework**: AppKit  
**Kind**: method

Dispatches an action message to the specified target.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func tryToPerform(_ action: Selector, with object: Any?) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if either the receiver or its delegate can accept the specified selector; otherwise, [`false`](https://developer.apple.com/documentation/swift/false). This method also returns [`false`](https://developer.apple.com/documentation/swift/false) if `aSelector` is `nil`.

#### Discussion

The receiver tries to perform the method `aSelector` using its inherited [`tryToPerform(_:with:)`](nsresponder/trytoperform(_:with:).md) method of [`NSResponder`](nsresponder.md). If the receiver doesn’t perform `aSelector`, the delegate is given the opportunity to perform it using its inherited [`perform(_:with:)`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol/perform(_:with:)) method of [`NSObject`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class).

## Parameters

- `action`: The action message you want to dispatch.
- `object`: The target object that defines the specified selector.

## See Also

- [func responds(to aSelector: Selector!) -> Bool](../ObjectiveC/NSObjectProtocol/responds(to:).md)
  Returns a Boolean value that indicates whether the receiver implements or inherits a method that can respond to a specified message.
- [func sendAction(Selector, to: Any?, from: Any?) -> Bool](nsapplication/sendaction(_:to:from:).md)
  Sends the given action message to the given target.
- [func target(forAction: Selector) -> Any?](nsapplication/target(foraction:).md)
  Returns the object that receives the action message specified by the given selector.
- [func target(forAction: Selector, to: Any?, from: Any?) -> Any?](nsapplication/target(foraction:to:from:).md)
  Searches for an object that can receive the message specified by the given selector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/trytoperform(_:with:))*