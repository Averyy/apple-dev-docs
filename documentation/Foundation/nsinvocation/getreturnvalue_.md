# getReturnValue:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Gets the invocation’s return value.

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
- (void) getReturnValue:(void *) retLoc;
```

## Discussion

Use the `NSMethodSignature` method [`methodReturnLength`](../nsmethodsignature/methodreturnlength.md) to determine the size needed for `buffer`:

```objc
NSUInteger length = [[myInvocation methodSignature] methodReturnLength];
buffer = (void *)malloc(length);
[invocation getReturnValue:buffer];
```

When the return value is an object, pass a pointer to the variable (or memory) into which [`NSInvocation`](../nsinvocation.md) should place the object. In the following example, `myInvocation` represents a call to a no-argument method called `createReturnValue` in a class called `MyClass`, which returns an [`NSMutableString`](../nsmutablestring.md). The example performs the invocation with [`invoke`](./invoke.md), then retrieves the object with [`getReturnValue:`](./getreturnvalue_.md) and copies it to a strongly-held property called `myObject`.

> ⚠️ **Warning**:  [`NSInvocation`](../nsinvocation.md) copies the return value directly into `buffer` without any memory bookkeeping, even when using Automatic Reference Counting (ARC). When using ARC, pass a pointer whose memory semantics match those expected by the method. Otherwise, an over-release crash may occur. For typical Objective-C methods, where ownership isn’t returned to the caller, use an `unsafe_unretained` variable. You can then copy this into another form of storage, like a strongly-held property. However, if the only thing keeping the returned value alive is the invocation’s [`target`](./target.md), then you must keep the target alive while using the returned value. You can do this with the macro [`NS_VALID_UNTIL_END_OF_SCOPE`](../ns_valid_until_end_of_scope.md) on the target. The following example shows how to properly manage memory when using ARC.

```objc
// Create invocation, set selector, and invoke.
NS_VALID_UNTIL_END_OF_SCOPE MyClass* myTarget = [[MyClass alloc] init];
NSMethodSignature* mySignature = [MyClass
    instanceMethodSignatureForSelector: @selector(createReturnValue)];
NSInvocation* myInvocation = [NSInvocation invocationWithMethodSignature: mySignature];
[myInvocation setSelector: @selector(createReturnValue)];

[myInvocation invokeWithTarget: myTarget];

// Retrieve return value and assign to property.
__unsafe_unretained id tempObject = nil;
[myInvocation getReturnValue: &tempObject];
self.myObject = tempObject;
```

If you haven’t invoked the [`NSInvocation`](../nsinvocation.md) object, the result of this method is undefined.

## Parameters

- `retLoc`: An untyped buffer into which the invocation copies its return value. It should be large enough to accommodate the value. See the discussion below for more information about `buffer`.

## See Also

### Related Documentation
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
- [- setReturnValue:](./setreturnvalue_.md)
  Sets the receiver’s return value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsinvocation/getreturnvalue:)*