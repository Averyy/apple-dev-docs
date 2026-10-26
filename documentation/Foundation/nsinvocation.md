# NSInvocation

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

An Objective-C message rendered as an object.

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
@interface NSInvocation : NSObject
```

#### Overview

[`NSInvocation`](./nsinvocation.md) objects are used to store and forward messages between objects and between applications, primarily by [`Timer`](./timer.md) objects and the distributed objects system. An [`NSInvocation`](./nsinvocation.md) object contains all the elements of an Objective-C message: a target, a selector, arguments, and the return value. Each of these elements can be set directly, and the return value is set automatically when the [`NSInvocation`](./nsinvocation.md) object is dispatched.

An [`NSInvocation`](./nsinvocation.md) object can be repeatedly dispatched to different targets; its arguments can be modified between dispatch for varying results; even its selector can be changed to another with the same method signature (argument and return types). This flexibility makes [`NSInvocation`](./nsinvocation.md) useful for repeating messages with many arguments and variations; rather than retyping a slightly different expression for each message, you modify the [`NSInvocation`](./nsinvocation.md) object as needed each time before dispatching it to a new target.

[`NSInvocation`](./nsinvocation.md) does not support invocations of methods with either variable numbers of arguments or `union` arguments. You should use the [`invocationWithMethodSignature:`](./nsinvocation/invocationwithmethodsignature_.md) class method to create [`NSInvocation`](./nsinvocation.md) objects; you should not create these objects using [`alloc`](../ObjectiveC/nsobject-swift.class/alloc.md) and [`init()`](../ObjectiveC/nsobject-swift.class/init%28%29.md).

This class does not retain the arguments for the contained invocation by default. If those objects might disappear between the time you create your instance of [`NSInvocation`](./nsinvocation.md) and the time you use it, you should explicitly retain the objects yourself or invoke the [`retainArguments`](./nsinvocation/retainarguments.md) method to have the invocation object retain them itself.

> **Note**:  [`NSInvocation`](./nsinvocation.md) conforms to the [`NSCoding`](./nscoding.md) protocol, but only supports coding by an [`NSPortCoder`](./nsportcoder.md). [`NSInvocation`](./nsinvocation.md) does not support archiving.

## Topics

### Creating NSInvocation Objects
- [+ invocationWithMethodSignature:](./nsinvocation/invocationwithmethodsignature_.md)
  Returns an `NSInvocation` object able to construct messages using a given method signature.
### Configuring an Invocation Object
- [selector](./nsinvocation/selector.md)
  The receiver’s selector, or 0 if it hasn’t been set.
- [target](./nsinvocation/target.md)
  The receiver’s target, or `nil` if the receiver has no target.
- [- setArgument:atIndex:](./nsinvocation/setargument_atindex_.md)
  Sets an argument of the receiver.
- [- getArgument:atIndex:](./nsinvocation/getargument_atindex_.md)
  Returns by indirection the receiver’s argument at a specified index.
- [argumentsRetained](./nsinvocation/argumentsretained.md)
  A Boolean value that indicates if the receiver has retained its arguments.
- [- retainArguments](./nsinvocation/retainarguments.md)
  If the receiver hasn’t already done so, retains the target and all object arguments of the receiver and copies all of its C-string arguments and blocks. If a returnvalue has been set, this is also retained or copied.
- [- setReturnValue:](./nsinvocation/setreturnvalue_.md)
  Sets the receiver’s return value.
- [- getReturnValue:](./nsinvocation/getreturnvalue_.md)
  Gets the invocation’s return value.
### Dispatching an Invocation
- [- invoke](./nsinvocation/invoke.md)
  Sends the receiver’s message (with arguments) to its target and sets the return value.
- [- invokeWithTarget:](./nsinvocation/invokewithtarget_.md)
  Sets the receiver’s target, sends the receiver’s message (with arguments) to that target, and sets the return value.
### Getting the Method Signature
- [methodSignature](./nsinvocation/methodsignature.md)
  The receiver’s method signature.
### Instance Methods
- [- invokeUsingIMP:](./nsinvocation/invokeusingimp_.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)

## See Also

### Invocations
- [NSMethodSignature](./nsmethodsignature.md)
  A record of the type information for the return value and parameters of a method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsinvocation)*