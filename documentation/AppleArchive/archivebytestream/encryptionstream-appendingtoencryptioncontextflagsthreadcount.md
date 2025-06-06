# encryptionStream(appendingTo:encryptionContext:flags:threadCount:)

**Framework**: Apple Archive  
**Kind**: method

Reopens an existing encryption sequential output stream.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+
- watchOS 8.0+

## Declaration

```swift
static func encryptionStream(appendingTo encryptedStream: ArchiveByteStream, encryptionContext context: ArchiveEncryptionContext, flags: ArchiveFlags = [], threadCount: Int = 0) -> ArchiveByteStream?
```

#### Return Value

A new archive byte stream.

#### Discussion

The operation writes encrypted and compressed data to the end of the supplied archive byte stream, `encryptedStream`.

Create the encryption context from `encryptedStream`, and add the credentials to unlock the stream before calling this function.

The stream that the function returns only implements [`read(into:)`](archivebytestreamprotocol/read(into:).md) and [`read(into:atOffset:)`](archivebytestreamprotocol/read(into:atoffset:).md).

## Parameters

- `encryptedStream`: An input stream that provides encrypted and compressed data. The stream must implement   and  .
- `context`: The encryption context that provides options and credentials.
- `flags`: Flags that control the behavior of the operation.
- `threadCount`: The number of worker threads that the operation uses, set to   for default.

## See Also

- [static func encryptionStream(writingTo: ArchiveByteStream, encryptionContext: ArchiveEncryptionContext, flags: ArchiveFlags, threadCount: Int) -> ArchiveByteStream?](archivebytestream/encryptionstream(writingto:encryptioncontext:flags:threadcount:).md)
  Creates a encryption sequential input stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archivebytestream/encryptionstream(appendingto:encryptioncontext:flags:threadcount:))*