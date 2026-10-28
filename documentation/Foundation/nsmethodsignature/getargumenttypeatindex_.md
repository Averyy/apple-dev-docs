# getArgumentTypeAtIndex:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns the type encoding for the argument at a given index.

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
- (const char *) getArgumentTypeAtIndex:(NSUInteger) idx;
```

## Return Value

The type encoding for the argument at `idx`.

## Discussion

Indexes begin with 0. The implicit arguments `self` (of type `id`) and `_cmd` (of type `SEL`) are at indexes 0 and 1; explicit arguments begin at index 2.

> ❗ **Important**:  If `index` exceeds the number of arguments, `NSInvalidArgumentException` is raised.

## Parameters

- `idx`: The index of the argument to get.

## See Also

### Getting Information on Argument Types
- [numberOfArguments](./numberofarguments.md)
  The number of arguments recorded in the receiver.
- [frameLength](./framelength.md)
  The number of bytes that the arguments, taken together, occupy on the stack.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmethodsignature/getargumenttypeatindex:)*