# tryToPerform(_:with:)

**Framework**: AppKit  
**Kind**: method

Attempts to perform the method indicated by an action with a specified argument.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func tryToPerform(_ action: Selector, with object: Any?) -> Bool
```

#### Return Value

Returns [`false`](https://developer.apple.com/documentation/swift/false) if no responder is found that responds to `action;` otherwise, [`true`](https://developer.apple.com/documentation/swift/true).

#### Discussion

If the receiver responds to `action`, it invokes the method with `object` as the argument and returns [`true`](https://developer.apple.com/documentation/swift/true). If the receiver doesn’t respond, it sends this message to its next responder with the same selector and object.

## Parameters

- `action`: The selector identifying the action method.
- `object`: The object to use as the sole argument of the action method.

## See Also

- [func sendAction(Selector, to: Any?, from: Any?) -> Bool](nsapplication/sendaction(_:to:from:).md)
  Sends the given action message to the given target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsresponder/trytoperform(_:with:))*