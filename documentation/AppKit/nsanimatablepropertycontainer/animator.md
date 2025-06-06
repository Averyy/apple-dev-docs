# animator()

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Returns a proxy object for the receiver that can be used to initiate implied animation for property changes.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func animator() -> Self
```

#### Return Value

Returns a proxy object for the receiver that can initiate implied animations in response to property changes.

#### Discussion

The animator proxy object  should be treated as if it was the receiver itself, and may be passed to any code that accepts the receiver as a parameter.

Sending key-value coding compliant “set” messages to the proxy will trigger animation for automatically animated properties of its target object, if the active [`NSAnimationContext`](nsanimationcontext.md) in the current thread has a duration value greater than zero, and an animation for the property key is found by the [`NSAnimatablePropertyContainer`](nsanimatablepropertycontainer.md) search mechanism.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsanimatablepropertycontainer/animator())*