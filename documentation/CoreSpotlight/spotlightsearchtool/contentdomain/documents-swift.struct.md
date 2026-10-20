# SpotlightSearchTool.ContentDomain.Documents

**Framework**: Core Spotlight  
**Kind**: struct  
**Role**: Structure

Attribute mapping for the documents domain.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct Documents
```

## Topics

### Configuring the domain
- [init(authors: [SearchableItemAttribute]?, keywords: [SearchableItemAttribute]?, created: [SearchableItemAttribute]?, modified: [SearchableItemAttribute]?)](./documents-swift.struct/init%28authors,keywords,created,modified%29.md)
### Getting the domain attributes
- [var authors: [SearchableItemAttribute]?](./documents-swift.struct/authors.md)
  Attributes queried for document authors. Default: [`authorNames`](../../searchableitemattribute/authornames.md)
- [var created: [SearchableItemAttribute]?](./documents-swift.struct/created.md)
  Attributes queried for the creation date. Default: [`contentCreationDate`](../../searchableitemattribute/contentcreationdate.md)
- [var keywords: [SearchableItemAttribute]?](./documents-swift.struct/keywords.md)
  Attributes queried for content keywords. Default: [`textContent`](../../searchableitemattribute/textcontent.md)
- [var modified: [SearchableItemAttribute]?](./documents-swift.struct/modified.md)
  Attributes queried for the modified date. Default: [`contentModificationDate`](../../searchableitemattribute/contentmodificationdate.md)

## Relationships

### Conforms To
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Getting the documents domain
- [static var documents: SpotlightSearchTool.ContentDomain](./documents-swift.type.property.md)
  Documents, notes, and text-heavy content.
- [static func documents(SpotlightSearchTool.ContentDomain.Documents) -> SpotlightSearchTool.ContentDomain](./documents%28_%29.md)
  Documents, notes, and text-heavy content with custom attribute mapping.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/spotlightsearchtool/contentdomain/documents-swift.struct)*