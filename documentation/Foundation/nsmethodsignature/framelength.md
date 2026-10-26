# frameLength

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The number of bytes that the arguments, taken together, occupy on the stack.

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
@property (readonly) NSUInteger frameLength;
```

#### Discussion

This number varies with the hardware architecture the application runs on.

## See Also

### Getting Information on Argument Types
- [- getArgumentTypeAtIndex:](./getargumenttypeatindex_.md)
  Returns the type encoding for the argument at a given index.
- [numberOfArguments](./numberofarguments.md)
  The number of arguments recorded in the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmethodsignature/framelength)*