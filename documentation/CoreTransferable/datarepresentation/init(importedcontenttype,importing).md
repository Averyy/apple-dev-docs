# init(importedContentType:importing:)

**Framework**: Core Transferable  
**Kind**: init  
**Role**: Initializer

Creates a representation that allows importing an item as binary data.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
init(importedContentType: UTType, importing: @escaping @Sendable (Data) async throws -> Item)
```

## Parameters

- `importedContentType`: A uniform type identifier that best describes the item.
- `importing`: A closure that instantiates the item with given binary data

## See Also

### Creating a transfer representation
- [init(contentType: UTType, exporting: (Item) async throws -> Data, importing: (Data) async throws -> Item)](./init%28contenttype,exporting,importing%29.md)
  Creates a representation that allows transporting an item as binary data.
- [init(exportedContentType: UTType, exporting: (Item) async throws -> Data)](./init%28exportedcontenttype,exporting%29.md)
  Creates a representation that allows exporting an item as binary data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretransferable/datarepresentation/init(importedcontenttype:importing:))*