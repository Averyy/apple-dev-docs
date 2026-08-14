# SpotlightSearchTool.ContentDomain.Items

**Framework**: Core Spotlight  
**Kind**: struct

Attribute mapping for the items domain.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct Items
```

## Topics

### Configuring the domain
- [init(title: [SearchableItemAttribute]?, text: [SearchableItemAttribute]?, created: [SearchableItemAttribute]?, modified: [SearchableItemAttribute]?)](spotlightsearchtool/contentdomain/items-swift.struct/init(title:text:created:modified:).md)
### Getting the domain attributes
- [var created: [SearchableItemAttribute]?](spotlightsearchtool/contentdomain/items-swift.struct/created.md)
  Attributes queried for the creation date. Default: [`contentCreationDate`](searchableitemattribute/contentcreationdate.md)
- [var modified: [SearchableItemAttribute]?](spotlightsearchtool/contentdomain/items-swift.struct/modified.md)
  Attributes queried for the modified date. Default: [`contentModificationDate`](searchableitemattribute/contentmodificationdate.md)
- [var text: [SearchableItemAttribute]?](spotlightsearchtool/contentdomain/items-swift.struct/text.md)
  Attributes queried for content keywords. Default: [`textContent`](searchableitemattribute/textcontent.md)
- [var title: [SearchableItemAttribute]?](spotlightsearchtool/contentdomain/items-swift.struct/title.md)
  Attributes queried for the item title. Default: [`title`](searchableitemattribute/title.md)

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [static var items: SpotlightSearchTool.ContentDomain](spotlightsearchtool/contentdomain/items-swift.type.property.md)
  Any items with title, text, and dates.
- [static func items(SpotlightSearchTool.ContentDomain.Items) -> SpotlightSearchTool.ContentDomain](spotlightsearchtool/contentdomain/items(_:).md)
  Any items with title, text, and dates with custom attribute mapping.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/spotlightsearchtool/contentdomain/items-swift.struct)*