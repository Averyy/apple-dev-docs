# invokeWithTarget:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Sets the receiver’s target, sends the receiver’s message (with arguments) to that target, and sets the return value.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```objc
- (void) invokeWithTarget:(id) target;
```

#### Discussion

You must set the receiver’s selector and argument values before calling this method.

## Parameters

- `target`: The object to set as the receiver’s target.

## See Also

### Related Documentation
- [selector](./selector.md)
  The receiver’s selector, or 0 if it hasn’t been set.
- [- setArgument:atIndex:](./setargument_atindex_.md)
  Sets an argument of the receiver.
- [- getReturnValue:](./getreturnvalue_.md)
  Gets the invocation’s return value.
- [target](./target.md)
  The receiver’s target, or `nil` if the receiver has no target.
### Dispatching an Invocation
- [- invoke](./invoke.md)
  Sends the receiver’s message (with arguments) to its target and sets the return value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsinvocation/invokewithtarget:)*