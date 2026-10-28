# target

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The receiver’s target, or `nil` if the receiver has no target.

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
@property (assign, nullable) id target;
```

## Discussion

The target is the receiver of the message sent by [`invoke`](./invoke.md).

## See Also

### Related Documentation
- [- invokeWithTarget:](./invokewithtarget_.md)
  Sets the receiver’s target, sends the receiver’s message (with arguments) to that target, and sets the return value.
### Configuring an Invocation Object
- [selector](./selector.md)
  The receiver’s selector, or 0 if it hasn’t been set.
- [- setArgument:atIndex:](./setargument_atindex_.md)
  Sets an argument of the receiver.
- [- getArgument:atIndex:](./getargument_atindex_.md)
  Returns by indirection the receiver’s argument at a specified index.
- [argumentsRetained](./argumentsretained.md)
  A Boolean value that indicates if the receiver has retained its arguments.
- [- retainArguments](./retainarguments.md)
  If the receiver hasn’t already done so, retains the target and all object arguments of the receiver and copies all of its C-string arguments and blocks. If a returnvalue has been set, this is also retained or copied.
- [- setReturnValue:](./setreturnvalue_.md)
  Sets the receiver’s return value.
- [- getReturnValue:](./getreturnvalue_.md)
  Gets the invocation’s return value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsinvocation/target)*