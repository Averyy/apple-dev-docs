# MTLIOStatus.complete

**Framework**: Metal  
**Kind**: case

Indicates the GPU has successfully finished executing the input/output command buffer.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
case complete
```

## See Also

- [MTLIOStatus.pending](mtliostatus/pending.md)
  Indicates the GPU hasn’t finished executing the input/output command buffer.
- [MTLIOStatus.cancelled](mtliostatus/cancelled.md)
  Indicates the GPU has successfully abandoned the input/output command buffer.
- [MTLIOStatus.error](mtliostatus/error.md)
  Indicates the GPU experienced a problem with the input/output command buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtliostatus/complete)*