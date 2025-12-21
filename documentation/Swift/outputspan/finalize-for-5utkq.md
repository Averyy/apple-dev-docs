# finalize(for:)

**Framework**: Swift  
**Kind**: method

Consume the output span and return the number of initialized elements.

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
consuming func finalize(for buffer: Slice<UnsafeMutableBufferPointer<Element>>) -> Int
```

#### Return Value

The number of initialized elements in the same buffer, as tracked by the consumed `OutputSpan` instance.

#### Discussion

This method should be invoked in the scope where the `OutputSpan` was created, when it is time to commit the contents of the updated buffer back into the construct being initialized.

The context that created the output span is expected to remember what memory region the span is addressing. This consuming method expects to receive a copy of the same buffer pointer as a (loose) proof of ownership.

## Parameters

- `buffer`: The buffer we expect the   to reference.   This must be the same region of memory passed to   the   initializer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/outputspan/finalize(for:)-5utkq)*