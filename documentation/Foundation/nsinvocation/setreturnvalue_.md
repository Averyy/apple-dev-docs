# setReturnValue:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Sets the receiver’s return value.

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
- (void) setReturnValue:(void *) retLoc;
```

## Discussion

This value is normally set when you send an [`invoke`](./invoke.md) or [`invokeWithTarget:`](./invokewithtarget_.md) message.

## Parameters

- `retLoc`: An untyped buffer whose contents are copied as the receiver’s return value.

## See Also

### Related Documentation
- [methodReturnLength](../nsmethodsignature/methodreturnlength.md)
  The number of bytes required for the return value.
- [methodReturnType](../nsmethodsignature/methodreturntype.md)
  A C string encoding the return type of the method in Objective-C type encoding.
### Configuring an Invocation Object
- [selector](./selector.md)
  The receiver’s selector, or 0 if it hasn’t been set.
- [target](./target.md)
  The receiver’s target, or `nil` if the receiver has no target.
- [- setArgument:atIndex:](./setargument_atindex_.md)
  Sets an argument of the receiver.
- [- getArgument:atIndex:](./getargument_atindex_.md)
  Returns by indirection the receiver’s argument at a specified index.
- [argumentsRetained](./argumentsretained.md)
  A Boolean value that indicates if the receiver has retained its arguments.
- [- retainArguments](./retainarguments.md)
  If the receiver hasn’t already done so, retains the target and all object arguments of the receiver and copies all of its C-string arguments and blocks. If a returnvalue has been set, this is also retained or copied.
- [- getReturnValue:](./getreturnvalue_.md)
  Gets the invocation’s return value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsinvocation/setreturnvalue:)*