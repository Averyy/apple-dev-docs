# MTLIOCompressionContextDefaultChunkSize()

**Framework**: Metal  
**Kind**: func

Returns a compression chunk size you can use as a default for creating a compression context.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
func MTLIOCompressionContextDefaultChunkSize() -> Int
```

## See Also

- [func MTLIOCreateCompressionContext(String, MTLIOCompressionMethod, Int) -> MTLIOCompressionContext?](mtliocreatecompressioncontext(_:_:_:).md)
  Creates a compression context that you use to compress data into a single file.
- [enum MTLIOCompressionMethod](mtliocompressionmethod.md)
  The compression codecs that Metal supports for input/output handles.
- [typealias MTLIOCompressionContext](mtliocompressioncontext.md)
  A pointer that represents the state of a file compression session in progress.
- [func MTLIOCompressionContextAppendData(MTLIOCompressionContext, UnsafeRawPointer, Int)](mtliocompressioncontextappenddata(_:_:_:).md)
  Adds data to a compression context.
- [func MTLIOFlushAndDestroyCompressionContext(MTLIOCompressionContext) -> MTLIOCompressionStatus](mtlioflushanddestroycompressioncontext(_:).md)
  Finishes compressing and saves the file that a compression context represents.
- [enum MTLIOCompressionStatus](mtliocompressionstatus.md)
  Represents the final state of a compression context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtliocompressioncontextdefaultchunksize())*