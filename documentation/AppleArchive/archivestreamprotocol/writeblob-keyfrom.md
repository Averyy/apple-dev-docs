# writeBlob(key:from:)

**Framework**: Apple Archive  
**Kind**: method  
**Required**: Yes

Writes an entry blob data.

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
func writeBlob(key: ArchiveHeader.FieldKey, from buffer: UnsafeRawBufferPointer) throws
```

## Parameters

- `key`: The blob field key.
- `buffer`: The data buffer that the operation uses as a source for the entry blob data.

## See Also

- [func readBlob(key: ArchiveHeader.FieldKey, into: UnsafeMutableRawBufferPointer) throws](archivestreamprotocol/readblob(key:into:).md)
  Reads the current entry blob data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archivestreamprotocol/writeblob(key:from:))*