# retainArguments

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

If the receiver hasn’t already done so, retains the target and all object arguments of the receiver and copies all of its C-string arguments and blocks. If a returnvalue has been set, this is also retained or copied.

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
- (void) retainArguments;
```

## Discussion

Before this method is invoked, [`argumentsRetained`](./argumentsretained.md) returns [`false`](../../Swift/false.md); after, it returns [`true`](../../Swift/true.md).

For efficiency, newly created `NSInvocation` objects don’t retain or copy their arguments, nor do they retain their targets, copy C strings, or copy any associated blocks. You should instruct an `NSInvocation` object to retain its arguments if you intend to cache it, because the arguments may otherwise be released before the invocation is invoked. `NSTimer` objects always instruct their invocations to retain their arguments, for example, because there’s usually a delay before a timer fires.

## See Also

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
- [- setReturnValue:](./setreturnvalue_.md)
  Sets the receiver’s return value.
- [- getReturnValue:](./getreturnvalue_.md)
  Gets the invocation’s return value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsinvocation/retainarguments)*