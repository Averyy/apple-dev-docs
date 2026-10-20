# writeBlob(key:from:)

**Framework**: Apple Archive  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Writes an entry blob data.

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
func writeBlob(key: ArchiveHeader.FieldKey, from buffer: UnsafeRawBufferPointer) throws
```

## Parameters

- `key`: The blob field key.
- `buffer`: The data buffer that the operation uses as a source for the entry blob data.

## See Also

### Reading and Writing Blobs
- [func readBlob(key: ArchiveHeader.FieldKey, into: UnsafeMutableRawBufferPointer) throws](./readblob%28key,into%29.md)
  Reads the current entry blob data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archivestreamprotocol/writeblob(key:from:))*