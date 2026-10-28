# NSMethodSignature

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

A record of the type information for the return value and parameters of a method.

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
@interface NSMethodSignature : NSObject
```

## Overview

Use an [`NSMethodSignature`](./nsmethodsignature.md) object to forward messages that the receiving object does not respond to—most notably in the case of distributed objects. You typically create an [`NSMethodSignature`](./nsmethodsignature.md) object using the [`NSObject`](../ObjectiveC/nsobject-swift.class.md) [`methodSignatureForSelector:`](../ObjectiveC/nsobject-swift.class/methodsignatureforselector_.md) instance method (in macOS 10.5 and later you can also use [`signatureWithObjCTypes:`](./nsmethodsignature/signaturewithobjctypes_.md)). It is then used to create an [`NSInvocation`](./nsinvocation.md) object, which is passed as the argument to a [`forwardInvocation:`](../ObjectiveC/nsobject-swift.class/forwardinvocation_.md) message to send the invocation on to whatever other object can handle the message. In the default case, [`NSObject`](../ObjectiveC/nsobject-swift.class.md) invokes [`doesNotRecognizeSelector(_:)`](../ObjectiveC/nsobject-swift.class/doesnotrecognizeselector%28_%29.md), which raises an exception. For distributed objects, the [`NSInvocation`](./nsinvocation.md) object is encoded using the information in the [`NSMethodSignature`](./nsmethodsignature.md) object and sent to the real object represented by the receiver of the message.

### Type Encodings

An `NSMethodSignature` object is initialized with an array of characters representing the string encoding of return and argument types for a method. You can get the string encoding of a particular type using the `@encode()` compiler directive. Because string encodings are implementation-specific, you should not hard-code these values.

A method signature consists of one or more characters for the method return type, followed by the string encodings of the implicit arguments `self` and `_cmd`, followed by zero or more explicit arguments. You can determine the string encoding and the length of a return type using [`methodReturnType`](./nsmethodsignature/methodreturntype.md) and [`methodReturnLength`](./nsmethodsignature/methodreturnlength.md) properties. You can access arguments individually using the [`getArgumentTypeAtIndex:`](./nsmethodsignature/getargumenttypeatindex_.md) method and [`numberOfArguments`](./nsmethodsignature/numberofarguments.md) property.

For example, the `NSString` instance method [`contains(_:)`](./nsstring/contains%28_%29.md) has a method signature with the following arguments:

1. `@encode(BOOL)` (`c`) for the return type
2. `@encode(id)` (`@`) for the receiver (`self`)
3. `@encode(SEL)` (`:`) for the selector (`_cmd`)
4. `@encode(NSString *)` (`@`) for the first explicit argument

See [Type Encodings](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjCRuntimeGuide/Articles/ocrtTypeEncodings.html#//apple_ref/doc/uid/TP40008048-CH100) in [Objective-C Runtime Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjCRuntimeGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40008048) for more information.

## Topics

### Creating a Method Signature Object
- [+ signatureWithObjCTypes:](./nsmethodsignature/signaturewithobjctypes_.md)
  Returns an `NSMethodSignature` object for the given Objective-C method type string.
### Getting Information on Argument Types
- [- getArgumentTypeAtIndex:](./nsmethodsignature/getargumenttypeatindex_.md)
  Returns the type encoding for the argument at a given index.
- [numberOfArguments](./nsmethodsignature/numberofarguments.md)
  The number of arguments recorded in the receiver.
- [frameLength](./nsmethodsignature/framelength.md)
  The number of bytes that the arguments, taken together, occupy on the stack.
### Getting Information on Return Types
- [methodReturnType](./nsmethodsignature/methodreturntype.md)
  A C string encoding the return type of the method in Objective-C type encoding.
- [methodReturnLength](./nsmethodsignature/methodreturnlength.md)
  The number of bytes required for the return value.
### Determining Synchronous Status
- [- isOneway](./nsmethodsignature/isoneway.md)
  Whether the receiver is asynchronous when invoked through distributed objects.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)

## See Also

### Invocations
- [NSInvocation](./nsinvocation.md)
  An Objective-C message rendered as an object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmethodsignature)*