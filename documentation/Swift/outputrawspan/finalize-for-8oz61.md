# finalize(for:)

**Framework**: Swift  
**Kind**: method

Consume the output span (relinquishing its control over the buffer it is addressing), and return the number of initialized bytes in it.

**Availability**:
- iOS 12.2+
- iPadOS 12.2+
- Mac Catalyst 12.2+
- macOS 10.14.4+
- tvOS 12.2+
- visionOS 1.0+
- watchOS 5.2+

## Declaration

```swift
consuming func finalize(for buffer: UnsafeMutableRawBufferPointer) -> Int
```

#### Return Value

The number of initialized bytes in the same buffer, as tracked by the consumed `OutputRawSpan` instance.

#### Discussion

This method should be invoked in the scope where the `OutputRawSpan` was created, when it is time to commit the contents of the updated buffer back into the construct being initialized.

The context that created the output span is expected to remember what memory region the span is addressing. This consuming method expects to receive a copy of the same buffer pointer as a (loose) proof of ownership.

## Parameters

- `buffer`: The buffer we expect the   to reference.   This must be the same region of memory passed to   the   initializer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/outputrawspan/finalize(for:)-8oz61)*