# randomAccessDecryptionStream(readingFrom:encryptionContext:allocationLimit:flags:threadCount:)

**Framework**: Apple Archive  
**Kind**: method

Creates a decryption random access input stream.

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
static func randomAccessDecryptionStream(readingFrom encryptedStream: ArchiveByteStream, encryptionContext context: ArchiveEncryptionContext, allocationLimit: Int = Int.max, flags: ArchiveFlags = [], threadCount: Int = 0) -> ArchiveByteStream?
```

#### Return Value

A new archive byte stream.

## Parameters

- `encryptedStream`: An input stream that provides encrypted and compressed data.
- `context`: Encryption context that provides options and credentials.
- `allocationLimit`: The requested memory allocation size in bytes. Set to   for lowest memory footprint or   for best performance.
- `flags`: Flags that control the behavior of the operation.
- `threadCount`: The number of worker threads that the operation uses, set to   for default.

## See Also

- [static func decryptionStream(readingFrom: ArchiveByteStream, encryptionContext: ArchiveEncryptionContext, flags: ArchiveFlags, threadCount: Int) -> ArchiveByteStream?](archivebytestream/decryptionstream(readingfrom:encryptioncontext:flags:threadcount:).md)
  Creates a decryption sequential input stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archivebytestream/randomaccessdecryptionstream(readingfrom:encryptioncontext:allocationlimit:flags:threadcount:))*