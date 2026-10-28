# objc_msgSend

**Framework**: Objective-C Runtime  
**Kind**: func  
**Role**: Function

Sends a message with a simple return value to an instance of a class.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```c
extern void objc_msgSend();
```

## Parameters

- **`self`**: A pointer that points to the instance of the class that is to receive the message.
- **`op`**: The selector of the method that handles the message.
- **`...`**: A variable argument list containing the arguments to the method.

## Return Value

The return value of the method.

## Discussion

When it encounters a method call, the compiler generates a call to one of the functions `objc_msgSend`, `objc_msgSend_stret`, `objc_msgSendSuper`, or `objc_msgSendSuper_stret`. Messages sent to an object’s superclass (using the `super` keyword) are sent using `objc_msgSendSuper`; other messages are sent using `objc_msgSend`. Methods that have data structures as return values are sent using `objc_msgSendSuper_stret` and `objc_msgSend_stret`.

## See Also

### Sending Messages
- [objc_msgSend_fpret](./objc_msgsend_fpret.md)
  Sends a message with a floating-point return value to an instance of a class.
- [objc_msgSend_stret](./objc_msgsend_stret.md)
  Sends a message with a data-structure return value to an instance of a class.
- [objc_msgSendSuper](./objc_msgsendsuper.md)
  Sends a message with a simple return value to the superclass of an instance of a class.
- [objc_msgSendSuper_stret](./objc_msgsendsuper_stret.md)
  Sends a message with a data-structure return value to the superclass of an instance of a class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/objc_msgsend)*