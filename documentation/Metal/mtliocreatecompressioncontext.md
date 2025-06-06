# MTLIOCreateCompressionContext(_:_:_:)

**Framework**: Metal  
**Kind**: func

Creates a compression context that you use to compress data into a single file.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+

## Declaration

```swift
func MTLIOCreateCompressionContext(_ path: String, _ type: MTLIOCompressionMethod, _ chunkSize: Int) -> MTLIOCompressionContext?
```

## Parameters

- `path`: A location in the file system where the function creates the new, compressed file.
- `type`: A compression codec the function uses to compress data resource file’s compression format.
- `chunkSize`: The number of uncompressed bytes the compression codec compresses at a time.

## See Also

- [enum MTLIOCompressionMethod](mtliocompressionmethod.md)
  The compression codecs that Metal supports for input/output handles.
- [func MTLIOCompressionContextDefaultChunkSize() -> Int](mtliocompressioncontextdefaultchunksize().md)
  Returns a compression chunk size you can use as a default for creating a compression context.
- [typealias MTLIOCompressionContext](mtliocompressioncontext.md)
  A pointer that represents the state of a file compression session in progress.
- [func MTLIOCompressionContextAppendData(MTLIOCompressionContext, UnsafeRawPointer, Int)](mtliocompressioncontextappenddata(_:_:_:).md)
  Adds data to a compression context.
- [func MTLIOFlushAndDestroyCompressionContext(MTLIOCompressionContext) -> MTLIOCompressionStatus](mtlioflushanddestroycompressioncontext(_:).md)
  Finishes compressing and saves the file that a compression context represents.
- [enum MTLIOCompressionStatus](mtliocompressionstatus.md)
  Represents the final state of a compression context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtliocreatecompressioncontext(_:_:_:))*