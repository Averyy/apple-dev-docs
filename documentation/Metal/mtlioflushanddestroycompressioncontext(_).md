# MTLIOFlushAndDestroyCompressionContext(_:)

**Framework**: Metal  
**Kind**: func  
**Role**: Function

Finishes compressing and saves the file that a compression context represents.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func MTLIOFlushAndDestroyCompressionContext(_ context: MTLIOCompressionContext) -> MTLIOCompressionStatus
```

```c
extern MTLIOCompressionStatus MTLIOFlushAndDestroyCompressionContext(MTLIOCompressionContext context);
```

#### Return Value

An [`MTLIOCompressionStatus`](./mtliocompressionstatus.md) instance.

## Parameters

- `context`: A compression context that you create with the [`MTLIOCreateCompressionContext(_:_:_:)`](./mtliocreatecompressioncontext%28_,_,_%29.md) function.

## See Also

### Asset compression
- [func MTLIOCreateCompressionContext(String, MTLIOCompressionMethod, Int) -> MTLIOCompressionContext?](./mtliocreatecompressioncontext%28_,_,_%29.md)
  Creates a compression context that you use to compress data into a single file.
- [enum MTLIOCompressionMethod](./mtliocompressionmethod.md)
  The compression codecs that Metal supports for input/output handles.
- [func MTLIOCompressionContextDefaultChunkSize() -> Int](./mtliocompressioncontextdefaultchunksize%28%29.md)
  Returns a compression chunk size you can use as a default for creating a compression context.
- [typealias MTLIOCompressionContext](./mtliocompressioncontext.md)
  A pointer that represents the state of a file compression session in progress.
- [func MTLIOCompressionContextAppendData(MTLIOCompressionContext, UnsafeRawPointer, Int)](./mtliocompressioncontextappenddata%28_,_,_%29.md)
  Adds data to a compression context.
- [enum MTLIOCompressionStatus](./mtliocompressionstatus.md)
  Represents the final state of a compression context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlioflushanddestroycompressioncontext(_:))*