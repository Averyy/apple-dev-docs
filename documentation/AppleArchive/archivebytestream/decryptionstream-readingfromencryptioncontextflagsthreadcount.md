# decryptionStream(readingFrom:encryptionContext:flags:threadCount:)

**Framework**: Apple Archive  
**Kind**: method

Creates a decryption sequential input stream.

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
static func decryptionStream(readingFrom encryptedStream: ArchiveByteStream, encryptionContext context: ArchiveEncryptionContext, flags: ArchiveFlags = [], threadCount: Int = 0) -> ArchiveByteStream?
```

#### Return Value

A new archive byte stream.

## Parameters

- `encryptedStream`: An input stream that provides encrypted and compressed data.
- `context`: The encryption context that provides options and credentials.
- `flags`: Flags that control the behavior of the operation.
- `threadCount`: The number of worker threads that the operation uses, set to   for default.

## See Also

- [static func randomAccessDecryptionStream(readingFrom: ArchiveByteStream, encryptionContext: ArchiveEncryptionContext, allocationLimit: Int, flags: ArchiveFlags, threadCount: Int) -> ArchiveByteStream?](archivebytestream/randomaccessdecryptionstream(readingfrom:encryptioncontext:allocationlimit:flags:threadcount:).md)
  Creates a decryption random access input stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archivebytestream/decryptionstream(readingfrom:encryptioncontext:flags:threadcount:))*