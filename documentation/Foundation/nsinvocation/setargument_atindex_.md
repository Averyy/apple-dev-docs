# setArgument:atIndex:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Sets an argument of the receiver.

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
- (void) setArgument:(void *) argumentLocation atIndex:(NSInteger) idx;
```

#### Discussion

This method copies the contents of `buffer` as the argument at `index`. The number of bytes copied is determined by the argument size.

When the argument value is an object, pass a pointer to the variable (or memory) from which the object should be copied:

```objc
NSArray *anArray;
[invocation setArgument:&anArray atIndex:3];
```

This method raises `NSInvalidArgumentException` if the value of `index` is greater than the actual number of arguments for the selector.

## Parameters

- `argumentLocation`: An untyped buffer containing an argument to be assigned to the receiver. See the discussion below relating to argument values that are objects.
- `idx`: An integer specifying the index of the argument.

  Indices 0 and 1 indicate the hidden arguments `self` and `_cmd`, respectively; you should set these values directly with the [`target`](./target.md) and [`selector`](./selector.md) properties. Use indices 2 and greater for the arguments normally passed in a message.

## See Also

### Related Documentation
- [numberOfArguments](../nsmethodsignature/numberofarguments.md)
  The number of arguments recorded in the receiver.
### Configuring an Invocation Object
- [selector](./selector.md)
  The receiver’s selector, or 0 if it hasn’t been set.
- [target](./target.md)
  The receiver’s target, or `nil` if the receiver has no target.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsinvocation/setargument:atindex:)*