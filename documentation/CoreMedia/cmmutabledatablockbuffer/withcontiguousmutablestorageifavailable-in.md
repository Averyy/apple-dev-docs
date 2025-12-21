# withContiguousMutableStorageIfAvailable(in:_:)

**Framework**: Core Media  
**Kind**: method

Access contents of the buffer if available as contiguous memory block.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
mutating func withContiguousMutableStorageIfAvailable<R>(in range: Range<Int>? = nil, _ body: (UnsafeMutableRawBufferPointer) throws -> sending R) rethrows -> sending R?
```

#### Discussion

This method calls body(buffer), where buffer is a pointer to the block buffers contiguous storage. If the contiguous storage doesn’t exist,  the method doesn’t call body — it immediately returns nil.

## Parameters

- `range`: Range of the buffer to access. Pass nil to access the whole buffer.
- `body`: Closure to execute with the memory block


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmmutabledatablockbuffer/withcontiguousmutablestorageifavailable(in:_:))*