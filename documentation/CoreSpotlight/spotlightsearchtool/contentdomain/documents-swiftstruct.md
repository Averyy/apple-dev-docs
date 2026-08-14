# SpotlightSearchTool.ContentDomain.Documents

**Framework**: Core Spotlight  
**Kind**: struct

Attribute mapping for the documents domain.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct Documents
```

## Topics

### Configuring the domain
- [init(authors: [SearchableItemAttribute]?, keywords: [SearchableItemAttribute]?, created: [SearchableItemAttribute]?, modified: [SearchableItemAttribute]?)](spotlightsearchtool/contentdomain/documents-swift.struct/init(authors:keywords:created:modified:).md)
### Getting the domain attributes
- [var authors: [SearchableItemAttribute]?](spotlightsearchtool/contentdomain/documents-swift.struct/authors.md)
  Attributes queried for document authors. Default: [`authorNames`](searchableitemattribute/authornames.md)
- [var created: [SearchableItemAttribute]?](spotlightsearchtool/contentdomain/documents-swift.struct/created.md)
  Attributes queried for the creation date. Default: [`contentCreationDate`](searchableitemattribute/contentcreationdate.md)
- [var keywords: [SearchableItemAttribute]?](spotlightsearchtool/contentdomain/documents-swift.struct/keywords.md)
  Attributes queried for content keywords. Default: [`textContent`](searchableitemattribute/textcontent.md)
- [var modified: [SearchableItemAttribute]?](spotlightsearchtool/contentdomain/documents-swift.struct/modified.md)
  Attributes queried for the modified date. Default: [`contentModificationDate`](searchableitemattribute/contentmodificationdate.md)

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [static var documents: SpotlightSearchTool.ContentDomain](spotlightsearchtool/contentdomain/documents-swift.type.property.md)
  Documents, notes, and text-heavy content.
- [static func documents(SpotlightSearchTool.ContentDomain.Documents) -> SpotlightSearchTool.ContentDomain](spotlightsearchtool/contentdomain/documents(_:).md)
  Documents, notes, and text-heavy content with custom attribute mapping.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/spotlightsearchtool/contentdomain/documents-swift.struct)*