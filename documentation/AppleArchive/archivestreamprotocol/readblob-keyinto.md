# readBlob(key:into:)

**Framework**: Apple Archive  
**Kind**: method  
**Required**: Yes

Reads the current entry blob data.

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
func readBlob(key: ArchiveHeader.FieldKey, into buffer: UnsafeMutableRawBufferPointer) throws
```

## Parameters

- `key`: The blob field key.
- `buffer`: The data buffer that the operation fills with the entry blob data.

## See Also

- [func writeBlob(key: ArchiveHeader.FieldKey, from: UnsafeRawBufferPointer) throws](archivestreamprotocol/writeblob(key:from:).md)
  Writes an entry blob data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archivestreamprotocol/readblob(key:into:))*