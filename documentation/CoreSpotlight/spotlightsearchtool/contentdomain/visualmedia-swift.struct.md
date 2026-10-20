# SpotlightSearchTool.ContentDomain.VisualMedia

**Framework**: Core Spotlight  
**Kind**: struct  
**Role**: Structure

Attribute mapping for the visual media domain.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct VisualMedia
```

## Topics

### Configuring the domain
- [init(people: [SearchableItemAttribute]?, description: [SearchableItemAttribute]?, location: [SearchableItemAttribute]?, date: [SearchableItemAttribute]?)](./visualmedia-swift.struct/init%28people,description,location,date%29.md)
### Getting the domain attributes
- [var date: [SearchableItemAttribute]?](./visualmedia-swift.struct/date.md)
  Attributes queried for the capture date. Default: [`contentCreationDate`](../../searchableitemattribute/contentcreationdate.md)
- [var description: [SearchableItemAttribute]?](./visualmedia-swift.struct/description.md)
  Attributes queried for visual content description.
- [var location: [SearchableItemAttribute]?](./visualmedia-swift.struct/location.md)
  Attributes queried for the location. Default: [`city`](../../searchableitemattribute/city.md)
- [var people: [SearchableItemAttribute]?](./visualmedia-swift.struct/people.md)
  Attributes queried for people appearing in images/video. Default: [`identifier`](../../searchableitemattribute/identifier.md)

## Relationships

### Conforms To
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Getting the visual media domain
- [static var visualMedia: SpotlightSearchTool.ContentDomain](./visualmedia-swift.type.property.md)
  Photos, videos, and other visual content.
- [static func visualMedia(SpotlightSearchTool.ContentDomain.VisualMedia) -> SpotlightSearchTool.ContentDomain](./visualmedia%28_%29.md)
  Photos, videos, and other visual content with custom attribute mapping.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/spotlightsearchtool/contentdomain/visualmedia-swift.struct)*