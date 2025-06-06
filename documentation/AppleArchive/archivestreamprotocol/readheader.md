# readHeader()

**Framework**: Apple Archive  
**Kind**: method  
**Required**: Yes

Reads the next entry header.

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
func readHeader() throws -> ArchiveHeader?
```

#### Return Value

A new header instance, or `nil` if the operation reaches the end of the archive stream.

## See Also

- [func writeHeader(ArchiveHeader) throws](archivestreamprotocol/writeheader(_:).md)
  Writes an entry header.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archivestreamprotocol/readheader())*