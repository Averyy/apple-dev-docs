# tryToPerform(_:with:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Dispatches an action message to the specified target.

**Availability**:
- macOS

## Declaration

```swift
func tryToPerform(_ action: Selector, with object: Any?) -> Bool
```

```objc
- (BOOL) tryToPerform:(SEL) action with:(id) object;
```

#### Return Value

[`true`](../../Swift/true.md) if either the receiver or its delegate can accept the specified selector; otherwise, [`false`](../../Swift/false.md). This method also returns [`false`](../../Swift/false.md) if `aSelector` is `nil`.

#### Discussion

The receiver tries to perform the method `aSelector` using its inherited [`tryToPerform(_:with:)`](../nsresponder/trytoperform%28_,with%29.md) method of [`NSResponder`](../nsresponder.md). If the receiver doesn’t perform `aSelector`, the delegate is given the opportunity to perform it using its inherited [`perform(_:with:)`](../../ObjectiveC/nsobjectprotocol/perform%28_,with%29.md) method of [`NSObject`](../../ObjectiveC/nsobject-swift.class.md).

## Parameters

- `action`: The action message you want to dispatch.
- `object`: The target object that defines the specified selector.

## See Also

### Related Documentation
- [func responds(to: Selector!) -> Bool](../../ObjectiveC/nsobjectprotocol/responds%28to%29.md)
  Returns a Boolean value that indicates whether the receiver implements or inherits a method that can respond to a specified message.
### Posting actions
- [func sendAction(Selector, to: Any?, from: Any?) -> Bool](./sendaction%28_,to,from%29.md)
  Sends the given action message to the given target.
- [func target(forAction: Selector) -> Any?](./target%28foraction%29.md)
  Returns the object that receives the action message specified by the given selector.
- [func target(forAction: Selector, to: Any?, from: Any?) -> Any?](./target%28foraction,to,from%29.md)
  Searches for an object that can receive the message specified by the given selector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/trytoperform(_:with:))*