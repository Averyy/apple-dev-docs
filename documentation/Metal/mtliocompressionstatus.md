# MTLIOCompressionStatus

**Framework**: Metal  
**Kind**: enum

Represents the final state of a compression context.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
enum MTLIOCompressionStatus
```

#### Overview

The [`MTLIOFlushAndDestroyCompressionContext(_:)`](mtlioflushanddestroycompressioncontext(_:).md) returns a [`MTLIOCompressionStatus`](mtliocompressionstatus.md) instance to reflect the final state of a compression context.

## Topics

### Compression Result States
- [MTLIOCompressionStatus.complete](mtliocompressionstatus/complete.md)
  Indicates the compression API successfully flushed and destroyed a compression context.
- [MTLIOCompressionStatus.error](mtliocompressionstatus/error.md)
  Indicates the compression API had an error while flushing and destroying a compression context.
### Initializers
- [init?(rawValue: Int)](mtliocompressionstatus/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func MTLIOCreateCompressionContext(String, MTLIOCompressionMethod, Int) -> MTLIOCompressionContext?](mtliocreatecompressioncontext(_:_:_:).md)
  Creates a compression context that you use to compress data into a single file.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtliocompressionstatus)*