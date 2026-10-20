# writeHeader(_:)

**Framework**: Apple Archive  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Writes an entry header.

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
func writeHeader(_ header: ArchiveHeader) throws
```

## Parameters

- `header`: The entry header to which the operation writes.

## See Also

### Reading and Writing Headers
- [func readHeader() throws -> ArchiveHeader?](./readheader%28%29.md)
  Reads the next entry header.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archivestreamprotocol/writeheader(_:))*