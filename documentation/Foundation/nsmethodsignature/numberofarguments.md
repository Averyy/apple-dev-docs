# numberOfArguments

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The number of arguments recorded in the receiver.

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
@property (readonly) NSUInteger numberOfArguments;
```

## Discussion

There are always at least two arguments, because an `NSMethodSignature` object includes the implicit arguments `self` and `_cmd`, which are the first two arguments passed to every method implementation.

## See Also

### Getting Information on Argument Types
- [- getArgumentTypeAtIndex:](./getargumenttypeatindex_.md)
  Returns the type encoding for the argument at a given index.
- [frameLength](./framelength.md)
  The number of bytes that the arguments, taken together, occupy on the stack.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmethodsignature/numberofarguments)*