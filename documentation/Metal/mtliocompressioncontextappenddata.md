# MTLIOCompressionContextAppendData(_:_:_:)

**Framework**: Metal  
**Kind**: func

Adds data to a compression context.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func MTLIOCompressionContextAppendData(_ context: MTLIOCompressionContext, _ data: UnsafeRawPointer, _ size: Int)
```

## Parameters

- `context`: An   instance that you create with the   function.
- `data`: A pointer to memory that contains the data the function adds to the compression context.
- `size`: The number of bytes the function adds to the compression context from the data pointer.

## See Also

- [func MTLIOCreateCompressionContext(String, MTLIOCompressionMethod, Int) -> MTLIOCompressionContext?](mtliocreatecompressioncontext(_:_:_:).md)
  Creates a compression context that you use to compress data into a single file.
- [enum MTLIOCompressionMethod](mtliocompressionmethod.md)
  The compression codecs that Metal supports for input/output handles.
- [func MTLIOCompressionContextDefaultChunkSize() -> Int](mtliocompressioncontextdefaultchunksize().md)
  Returns a compression chunk size you can use as a default for creating a compression context.
- [typealias MTLIOCompressionContext](mtliocompressioncontext.md)
  A pointer that represents the state of a file compression session in progress.
- [func MTLIOFlushAndDestroyCompressionContext(MTLIOCompressionContext) -> MTLIOCompressionStatus](mtlioflushanddestroycompressioncontext(_:).md)
  Finishes compressing and saves the file that a compression context represents.
- [enum MTLIOCompressionStatus](mtliocompressionstatus.md)
  Represents the final state of a compression context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtliocompressioncontextappenddata(_:_:_:))*