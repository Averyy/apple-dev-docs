# objc_msgSendSuper_stret

**Framework**: Objective-C Runtime  
**Kind**: func  
**Role**: Function

Sends a message with a data-structure return value to the superclass of an instance of a class.

**Availability**:
- macOS 10.0+

## Declaration

```c
extern void objc_msgSendSuper_stret();
```

#### Parameters

- **`super`**: A pointer to an [`objc_super`](./objc_super-swift.struct.md) data structure. Pass values identifying the context the message was sent to, including the instance of the class that is to receive the message and the superclass at which to start searching for the method implementation.
- **`op`**: A pointer of type [`SEL`](./sel.md). Pass the selector of the method.
- **`...`**: A variable argument list containing the arguments to the method.

#### Discussion

When it encounters a method call, the compiler generates a call to one of the functions `objc_msgSend`, `objc_msgSend_stret`, `objc_msgSendSuper`, or `objc_msgSendSuper_stret`. Messages sent to an object’s superclass (using the `super` keyword) are sent using `objc_msgSendSuper`; other messages are sent using `objc_msgSend`. Methods that have data structures as return values are sent using `objc_msgSendSuper_stret` and `objc_msgSend_stret`.

## See Also

### Sending Messages
- [objc_msgSend](./objc_msgsend.md)
  Sends a message with a simple return value to an instance of a class.
- [objc_msgSend_fpret](./objc_msgsend_fpret.md)
  Sends a message with a floating-point return value to an instance of a class.
- [objc_msgSend_stret](./objc_msgsend_stret.md)
  Sends a message with a data-structure return value to an instance of a class.
- [objc_msgSendSuper](./objc_msgsendsuper.md)
  Sends a message with a simple return value to the superclass of an instance of a class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/objc_msgsendsuper_stret)*