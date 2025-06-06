# MTLIOCompressionContext

**Framework**: Metal  
**Kind**: typealias

A pointer that represents the state of a file compression session in progress.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
typealias MTLIOCompressionContext = UnsafeMutableRawPointer
```

## See Also

- [func MTLIOCreateCompressionContext(String, MTLIOCompressionMethod, Int) -> MTLIOCompressionContext?](mtliocreatecompressioncontext(_:_:_:).md)
  Creates a compression context that you use to compress data into a single file.
- [enum MTLIOCompressionMethod](mtliocompressionmethod.md)
  The compression codecs that Metal supports for input/output handles.
- [func MTLIOCompressionContextDefaultChunkSize() -> Int](mtliocompressioncontextdefaultchunksize().md)
  Returns a compression chunk size you can use as a default for creating a compression context.
- [func MTLIOCompressionContextAppendData(MTLIOCompressionContext, UnsafeRawPointer, Int)](mtliocompressioncontextappenddata(_:_:_:).md)
  Adds data to a compression context.
- [func MTLIOFlushAndDestroyCompressionContext(MTLIOCompressionContext) -> MTLIOCompressionStatus](mtlioflushanddestroycompressioncontext(_:).md)
  Finishes compressing and saves the file that a compression context represents.
- [enum MTLIOCompressionStatus](mtliocompressionstatus.md)
  Represents the final state of a compression context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtliocompressioncontext)*