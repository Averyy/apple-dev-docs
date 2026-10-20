# readBlob(key:into:)

**Framework**: Apple Archive  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Reads the current entry blob data.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS
- watchOS 7.0+

## Declaration

```swift
func readBlob(key: ArchiveHeader.FieldKey, into buffer: UnsafeMutableRawBufferPointer) throws
```

## Parameters

- `key`: The blob field key.
- `buffer`: The data buffer that the operation fills with the entry blob data.

## See Also

### Reading and Writing Blobs
- [func writeBlob(key: ArchiveHeader.FieldKey, from: UnsafeRawBufferPointer) throws](./writeblob%28key,from%29.md)
  Writes an entry blob data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archivestreamprotocol/readblob(key:into:))*