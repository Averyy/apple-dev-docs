# MTLIOStatus.cancelled

**Framework**: Metal  
**Kind**: case  
**Role**: Case

Indicates the GPU has successfully abandoned the input/output command buffer.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
case cancelled
```

```c
MTLIOStatusCancelled
```

## See Also

### I/O command queue states
- [MTLIOStatus.pending](./pending.md)
  Indicates the GPU hasn’t finished executing the input/output command buffer.
- [MTLIOStatus.complete](./complete.md)
  Indicates the GPU has successfully finished executing the input/output command buffer.
- [MTLIOStatus.error](./error.md)
  Indicates the GPU experienced a problem with the input/output command buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtliostatus/cancelled)*