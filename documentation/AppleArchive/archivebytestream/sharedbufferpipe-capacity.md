# sharedBufferPipe(capacity:)

**Framework**: Apple Archive  
**Kind**: method

Creates a pair of streams and links them by a shared buffer.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+
- watchOS 7.0+

## Declaration

```swift
static func sharedBufferPipe(capacity: Int) -> (output: ArchiveByteStream, input: ArchiveByteStream)?
```

#### Return Value

A new pair of [`ArchiveByteStream`](archivebytestream.md) instances on success; `nil` otherwise.

#### Discussion

This function creates two [`ArchiveByteStream`](archivebytestream.md) instances that provide one-way communication between two threads. One thread calls the sequential output stream `output`, and the other thread calls the sequential input stream `input`. The function blocks writing to `output` when the buffer is full, and blocks reading from `input` when the buffer is empty.

If either thread calls [`cancel`](archiveheader/entrymessagestatus/cancel.md), the operation aborts both streams, and immediately calls return (without blocking) with an error.

Closing `output`, indicates end-of-file (EOF) and writing additional bytes fails. After the operation reaches EOF and has read all data, the read function on `input` returns `0` to signal EOF.

The operation destroys the underlying buffer after it closes both streams.

## Parameters

- `capacity`: The size of the internal buffer allocation, in bytes.

## See Also

- [static func customStream<C>(instance: C) -> ArchiveByteStream?](archivebytestream/customstream(instance:).md)
  Returns a new archive byte stream instance mapped to an object that conforms to the archive byte stream protocol.
- [static func withStream<C, E>(wrapping: C, (ArchiveByteStream) throws -> E) throws -> E](archivebytestream/withstream(wrapping:_:).md)
  Calls the given closure with an archive byte stream instance mapped to an object that conforms to the archive byte stream protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archivebytestream/sharedbufferpipe(capacity:))*