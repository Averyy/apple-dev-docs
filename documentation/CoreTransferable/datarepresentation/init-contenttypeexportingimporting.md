# init(contentType:exporting:importing:)

**Framework**: Core Transferable  
**Kind**: init

Creates a representation that allows transporting an item as binary data.

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
init(contentType: UTType, exporting: @escaping (Item) async throws -> Data, importing: @escaping (Data) async throws -> Item)
```

## Parameters

- `contentType`: A uniform type identifier that best describes the item.
- `exporting`: A closure that provides a data representation of the given item.
- `importing`: A closure that instantiates the item with given binary data.

## See Also

- [init(importedContentType: UTType, importing: (Data) async throws -> Item)](datarepresentation/init(importedcontenttype:importing:).md)
  Creates a representation that allows importing an item as binary data.
- [init(exportedContentType: UTType, exporting: (Item) async throws -> Data)](datarepresentation/init(exportedcontenttype:exporting:).md)
  Creates a representation that allows exporting an item as binary data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretransferable/datarepresentation/init(contenttype:exporting:importing:))*