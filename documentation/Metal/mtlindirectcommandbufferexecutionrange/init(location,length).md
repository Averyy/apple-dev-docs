# init(location:length:)

**Framework**: Metal  
**Kind**: init  
**Role**: Initializer

Initializes an command execution range.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
init(location: UInt32, length: UInt32)
```

## Parameters

- `location`: The start index of the range.
- `length`: The number of items in the range.

## See Also

### Creating a command execution range
- [init()](./init%28%29.md)
  Initializes an empty command execution range.
- [func MTLIndirectCommandBufferExecutionRangeMake(UInt32, UInt32) -> MTLIndirectCommandBufferExecutionRange](../mtlindirectcommandbufferexecutionrangemake%28_,_%29.md)
  Creates a command execution range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlindirectcommandbufferexecutionrange/init(location:length:))*