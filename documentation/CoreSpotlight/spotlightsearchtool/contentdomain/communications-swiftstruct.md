# SpotlightSearchTool.ContentDomain.Communications

**Framework**: Core Spotlight  
**Kind**: struct

Attribute mapping for the communications domain.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct Communications
```

#### Overview

Each field is an optional array of [`SearchableItemAttribute`](searchableitemattribute.md) values to query across. `nil` uses the built-in default mapping. Use [`textContent`](searchableitemattribute/textcontent.md) to trigger a full-text keyword search across all indexed content.

## Topics

### Configuring the domain
- [init(authors: [SearchableItemAttribute]?, recipients: [SearchableItemAttribute]?, sent: [SearchableItemAttribute]?, received: [SearchableItemAttribute]?, topic: [SearchableItemAttribute]?)](spotlightsearchtool/contentdomain/communications-swift.struct/init(authors:recipients:sent:received:topic:).md)
### Getting the domain attributes
- [var authors: [SearchableItemAttribute]?](spotlightsearchtool/contentdomain/communications-swift.struct/authors.md)
  Attributes queried for the author field. Default: [`authorNames`](searchableitemattribute/authornames.md)
- [var received: [SearchableItemAttribute]?](spotlightsearchtool/contentdomain/communications-swift.struct/received.md)
  Attributes queried for the received date field. Default: [`contentCreationDate`](searchableitemattribute/contentcreationdate.md)
- [var recipients: [SearchableItemAttribute]?](spotlightsearchtool/contentdomain/communications-swift.struct/recipients.md)
  Attributes queried for the recipient field. Default: [`recipientNames`](searchableitemattribute/recipientnames.md)
- [var sent: [SearchableItemAttribute]?](spotlightsearchtool/contentdomain/communications-swift.struct/sent.md)
  Attributes queried for the sent date field. Default: [`contentCreationDate`](searchableitemattribute/contentcreationdate.md)
- [var topic: [SearchableItemAttribute]?](spotlightsearchtool/contentdomain/communications-swift.struct/topic.md)
  Attributes queried for the subject/body field. Default: [`textContent`](searchableitemattribute/textcontent.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [static var communications: SpotlightSearchTool.ContentDomain](spotlightsearchtool/contentdomain/communications-swift.type.property.md)
  Email, messaging, and other person-to-person communication.
- [static func communications(SpotlightSearchTool.ContentDomain.Communications) -> SpotlightSearchTool.ContentDomain](spotlightsearchtool/contentdomain/communications(_:).md)
  Email, messaging, and other person-to-person communication with custom attribute mapping.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/spotlightsearchtool/contentdomain/communications-swift.struct)*