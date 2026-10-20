# tryToPerform(_:with:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Attempts to perform the method indicated by an action with a specified argument.

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

Returns [`false`](../../Swift/false.md) if no responder is found that responds to `action;` otherwise, [`true`](../../Swift/true.md).

#### Discussion

If the receiver responds to `action`, it invokes the method with `object` as the argument and returns [`true`](../../Swift/true.md). If the receiver doesn’t respond, it sends this message to its next responder with the same selector and object.

## Parameters

- `action`: The selector identifying the action method.
- `object`: The object to use as the sole argument of the action method.

## See Also

### Related Documentation
- [func sendAction(Selector, to: Any?, from: Any?) -> Bool](../nsapplication/sendaction%28_,to,from%29.md)
  Sends the given action message to the given target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsresponder/trytoperform(_:with:))*