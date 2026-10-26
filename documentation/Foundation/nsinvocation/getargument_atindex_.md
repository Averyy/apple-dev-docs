# getArgument:atIndex:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns by indirection the receiver’s argument at a specified index.

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
- (void) getArgument:(void *) argumentLocation atIndex:(NSInteger) idx;
```

#### Discussion

This method copies the argument stored at `index` into the storage pointed to by `buffer`. The size of `buffer` must be large enough to accommodate the argument value. When the argument value is an object, pass a pointer to the variable (or memory) into which the object should be placed.

In the following example, `myInvocation` represents a call to a two-argument method called `createWithString:count:` in a class called `MyClass`, which takes an [`NSMutableString`](../nsmutablestring.md) and an `int`. The example performs the invocation with [`invoke`](./invoke.md), then retrieves the first argument with [`getArgument:atIndex:`](./getargument_atindex_.md) and copies it to a strongly-held property called `myObject`.

> ⚠️ **Warning**:  [`NSInvocation`](../nsinvocation.md) copies the return value directly into `buffer` without any memory bookkeeping, even when using Automatic Reference Counting (ARC). When using ARC, pass a pointer whose memory semantics match those expected by the method. Otherwise, an over-release crash may occur. For typical Objective-C methods, where ownership isn’t returned to the caller, use an `unsafe_unretained` variable. You can then copy this into another form of storage, like a strongly-held property. The following example shows how to properly manage memory when using ARC.

```objc
// Create invocation and set selector.
MyClass* myTarget = [[MyClass alloc] init];
NSMethodSignature* mySignature = [MyClass
                                  instanceMethodSignatureForSelector: @selector(createWithString:count:)];
NSInvocation* myInvocation = [NSInvocation invocationWithMethodSignature: mySignature];
[myInvocation setSelector: @selector(createWithString:count:)];

// Set arguments and invoke.
NSMutableString* argument2 = [NSMutableString stringWithString: @"A string"];
[myInvocation setArgument:&argument2 atIndex: 2];
int argument3 = 5;
[myInvocation setArgument:&argument3 atIndex: 3];

[myInvocation invokeWithTarget: myTarget];

// Retrieve first argument and assign to property.
__unsafe_unretained id tempObject = nil;
[myInvocation getArgument: &tempObject atIndex: 2];
self.myObject = tempObject;
NSLog(@"Argument 0 was: %@", self.myObject); // prints "A string"
```

This method raises [`invalidArgumentException`](../nsexceptionname/invalidargumentexception.md) if `index` is greater than the actual number of arguments for the selector.

## Parameters

- `argumentLocation`: An untyped buffer to hold the returned argument. See the discussion below relating to argument values that are objects.
- `idx`: An integer specifying the index of the argument to get.

  Indices 0 and 1 indicate the hidden arguments `self` and `_cmd`, respectively; these values can be retrieved directly with the `target` and `selector` methods. Use indices 2 and greater for the arguments normally passed in a message.

## See Also

### Related Documentation
- [numberOfArguments](../nsmethodsignature/numberofarguments.md)
  The number of arguments recorded in the receiver.
### Configuring an Invocation Object
- [selector](./selector.md)
  The receiver’s selector, or 0 if it hasn’t been set.
- [target](./target.md)
  The receiver’s target, or `nil` if the receiver has no target.
- [- setArgument:atIndex:](./setargument_atindex_.md)
  Sets an argument of the receiver.
- [argumentsRetained](./argumentsretained.md)
  A Boolean value that indicates if the receiver has retained its arguments.
- [- retainArguments](./retainarguments.md)
  If the receiver hasn’t already done so, retains the target and all object arguments of the receiver and copies all of its C-string arguments and blocks. If a returnvalue has been set, this is also retained or copied.
- [- setReturnValue:](./setreturnvalue_.md)
  Sets the receiver’s return value.
- [- getReturnValue:](./getreturnvalue_.md)
  Gets the invocation’s return value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsinvocation/getargument:atindex:)*