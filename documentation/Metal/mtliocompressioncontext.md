# MTLIOCompressionContext

**Framework**: Metal  
**Kind**: typealias  
**Role**: Type Alias

A pointer that represents the state of a file compression session in progress.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
typealias MTLIOCompressionContext = UnsafeMutableRawPointer
```

```c
typedef void * MTLIOCompressionContext;
```

## See Also

### Asset compression
- [func MTLIOCreateCompressionContext(String, MTLIOCompressionMethod, Int) -> MTLIOCompressionContext?](./mtliocreatecompressioncontext%28_,_,_%29.md)
  Creates a compression context that you use to compress data into a single file.
- [enum MTLIOCompressionMethod](./mtliocompressionmethod.md)
  The compression codecs that Metal supports for input/output handles.
- [func MTLIOCompressionContextDefaultChunkSize() -> Int](./mtliocompressioncontextdefaultchunksize%28%29.md)
  Returns a compression chunk size you can use as a default for creating a compression context.
- [func MTLIOCompressionContextAppendData(MTLIOCompressionContext, UnsafeRawPointer, Int)](./mtliocompressioncontextappenddata%28_,_,_%29.md)
  Adds data to a compression context.
- [func MTLIOFlushAndDestroyCompressionContext(MTLIOCompressionContext) -> MTLIOCompressionStatus](./mtlioflushanddestroycompressioncontext%28_%29.md)
  Finishes compressing and saves the file that a compression context represents.
- [enum MTLIOCompressionStatus](./mtliocompressionstatus.md)
  Represents the final state of a compression context.
- [MTLIOCreateCompressionContext](./mtliocreatecompressioncontext.md)
  Creates a compression context that you use to compress data into a single file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtliocompressioncontext)*