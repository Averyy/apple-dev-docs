# MTLIOCompressionContextDefaultChunkSize()

**Framework**: Metal  
**Kind**: func  
**Role**: Function

Returns a compression chunk size you can use as a default for creating a compression context.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
func MTLIOCompressionContextDefaultChunkSize() -> Int
```

```c
extern size_t MTLIOCompressionContextDefaultChunkSize();
```

## See Also

### Asset compression
- [func MTLIOCreateCompressionContext(String, MTLIOCompressionMethod, Int) -> MTLIOCompressionContext?](./mtliocreatecompressioncontext%28_,_,_%29.md)
  Creates a compression context that you use to compress data into a single file.
- [enum MTLIOCompressionMethod](./mtliocompressionmethod.md)
  The compression codecs that Metal supports for input/output handles.
- [typealias MTLIOCompressionContext](./mtliocompressioncontext.md)
  A pointer that represents the state of a file compression session in progress.
- [func MTLIOCompressionContextAppendData(MTLIOCompressionContext, UnsafeRawPointer, Int)](./mtliocompressioncontextappenddata%28_,_,_%29.md)
  Adds data to a compression context.
- [func MTLIOFlushAndDestroyCompressionContext(MTLIOCompressionContext) -> MTLIOCompressionStatus](./mtlioflushanddestroycompressioncontext%28_%29.md)
  Finishes compressing and saves the file that a compression context represents.
- [enum MTLIOCompressionStatus](./mtliocompressionstatus.md)
  Represents the final state of a compression context.
- [MTLIOCreateCompressionContext](./mtliocreatecompressioncontext.md)
  Creates a compression context that you use to compress data into a single file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtliocompressioncontextdefaultchunksize())*