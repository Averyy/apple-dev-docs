# SpotlightSearchTool.ContentDomain.Items

**Framework**: Core Spotlight  
**Kind**: struct  
**Role**: Structure

Attribute mapping for the items domain.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct Items
```

## Topics

### Configuring the domain
- [init(title: [SearchableItemAttribute]?, text: [SearchableItemAttribute]?, created: [SearchableItemAttribute]?, modified: [SearchableItemAttribute]?)](./items-swift.struct/init%28title,text,created,modified%29.md)
### Getting the domain attributes
- [var created: [SearchableItemAttribute]?](./items-swift.struct/created.md)
  Attributes queried for the creation date. Default: [`contentCreationDate`](../../searchableitemattribute/contentcreationdate.md)
- [var modified: [SearchableItemAttribute]?](./items-swift.struct/modified.md)
  Attributes queried for the modified date. Default: [`contentModificationDate`](../../searchableitemattribute/contentmodificationdate.md)
- [var text: [SearchableItemAttribute]?](./items-swift.struct/text.md)
  Attributes queried for content keywords. Default: [`textContent`](../../searchableitemattribute/textcontent.md)
- [var title: [SearchableItemAttribute]?](./items-swift.struct/title.md)
  Attributes queried for the item title. Default: [`title`](../../searchableitemattribute/title.md)

## Relationships

### Conforms To
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Getting the items domain
- [static var items: SpotlightSearchTool.ContentDomain](./items-swift.type.property.md)
  Any items with title, text, and dates.
- [static func items(SpotlightSearchTool.ContentDomain.Items) -> SpotlightSearchTool.ContentDomain](./items%28_%29.md)
  Any items with title, text, and dates with custom attribute mapping.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/spotlightsearchtool/contentdomain/items-swift.struct)*