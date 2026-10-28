# SpotlightSearchTool.ContentDomain.Communications

**Framework**: Core Spotlight  
**Kind**: struct  
**Role**: Structure

Attribute mapping for the communications domain.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct Communications
```

## Overview

Each field is an optional array of [`SearchableItemAttribute`](../../searchableitemattribute.md) values to query across. `nil` uses the built-in default mapping. Use [`textContent`](../../searchableitemattribute/textcontent.md) to trigger a full-text keyword search across all indexed content.

## Topics

### Configuring the domain
- [init(authors: [SearchableItemAttribute]?, recipients: [SearchableItemAttribute]?, sent: [SearchableItemAttribute]?, received: [SearchableItemAttribute]?, topic: [SearchableItemAttribute]?)](./communications-swift.struct/init%28authors,recipients,sent,received,topic%29.md)
### Getting the domain attributes
- [var authors: [SearchableItemAttribute]?](./communications-swift.struct/authors.md)
  Attributes queried for the author field. Default: [`authorNames`](../../searchableitemattribute/authornames.md)
- [var received: [SearchableItemAttribute]?](./communications-swift.struct/received.md)
  Attributes queried for the received date field. Default: [`contentCreationDate`](../../searchableitemattribute/contentcreationdate.md)
- [var recipients: [SearchableItemAttribute]?](./communications-swift.struct/recipients.md)
  Attributes queried for the recipient field. Default: [`recipientNames`](../../searchableitemattribute/recipientnames.md)
- [var sent: [SearchableItemAttribute]?](./communications-swift.struct/sent.md)
  Attributes queried for the sent date field. Default: [`contentCreationDate`](../../searchableitemattribute/contentcreationdate.md)
- [var topic: [SearchableItemAttribute]?](./communications-swift.struct/topic.md)
  Attributes queried for the subject/body field. Default: [`textContent`](../../searchableitemattribute/textcontent.md)

## Relationships

### Conforms To
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Getting the communications domain
- [static var communications: SpotlightSearchTool.ContentDomain](./communications-swift.type.property.md)
  Email, messaging, and other person-to-person communication.
- [static func communications(SpotlightSearchTool.ContentDomain.Communications) -> SpotlightSearchTool.ContentDomain](./communications%28_%29.md)
  Email, messaging, and other person-to-person communication with custom attribute mapping.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/spotlightsearchtool/contentdomain/communications-swift.struct)*