# SpotlightSearchTool.ContentDomain.VisualMedia

**Framework**: Core Spotlight  
**Kind**: struct

Attribute mapping for the visual media domain.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct VisualMedia
```

## Topics

### Configuring the domain
- [init(people: [SearchableItemAttribute]?, description: [SearchableItemAttribute]?, location: [SearchableItemAttribute]?, date: [SearchableItemAttribute]?)](spotlightsearchtool/contentdomain/visualmedia-swift.struct/init(people:description:location:date:).md)
### Getting the domain attributes
- [var date: [SearchableItemAttribute]?](spotlightsearchtool/contentdomain/visualmedia-swift.struct/date.md)
  Attributes queried for the capture date. Default: [`contentCreationDate`](searchableitemattribute/contentcreationdate.md)
- [var description: [SearchableItemAttribute]?](spotlightsearchtool/contentdomain/visualmedia-swift.struct/description.md)
  Attributes queried for visual content description.
- [var location: [SearchableItemAttribute]?](spotlightsearchtool/contentdomain/visualmedia-swift.struct/location.md)
  Attributes queried for the location. Default: [`city`](searchableitemattribute/city.md)
- [var people: [SearchableItemAttribute]?](spotlightsearchtool/contentdomain/visualmedia-swift.struct/people.md)
  Attributes queried for people appearing in images/video. Default: [`identifier`](searchableitemattribute/identifier.md)

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [static var visualMedia: SpotlightSearchTool.ContentDomain](spotlightsearchtool/contentdomain/visualmedia-swift.type.property.md)
  Photos, videos, and other visual content.
- [static func visualMedia(SpotlightSearchTool.ContentDomain.VisualMedia) -> SpotlightSearchTool.ContentDomain](spotlightsearchtool/contentdomain/visualmedia(_:).md)
  Photos, videos, and other visual content with custom attribute mapping.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/spotlightsearchtool/contentdomain/visualmedia-swift.struct)*