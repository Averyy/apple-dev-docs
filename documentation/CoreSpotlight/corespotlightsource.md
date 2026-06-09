# CoreSpotlightSource

**Framework**: Core Spotlight  
**Kind**: struct

A search source that retrieves data from the app’s Spotlight index.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct CoreSpotlightSource
```

## Mentions

- [Making your indexed content available to Foundation Models](making-your-indexed-content-available-to-foundation-models.md)

#### Overview

Use this type to configure the Spotlight search tool to search your app’s indexed content. When performing searches, the tool queries your content for [`CSSearchableItem`](cssearchableitem.md) objects that match the specified criteria. When delivering search results to the model, the tool delivers each item’s identifier and any attributes you specify in the [`fetchAttributes`](corespotlightsource/fetchattributes.md) property. To provide additional item-specific content that isn’t in the Spotlight index, provide a delegate object to generate that data dynamically from your content.

This type is `@unchecked Sendable` because [`CSSearchableIndexDelegate`](cssearchableindexdelegate.md) is a non-Sendable ObjC protocol. If you provide a delegate object, you must ensure that object is safe to use across isolation boundaries.

## Topics

### Creating a Spotlight source
- [init(fetchAttributes: [SearchableItemAttribute])](corespotlightsource/init(fetchattributes:).md)
- [init(searchableIndexDelegate: (any CSSearchableIndexDelegate)?, fetchAttributes: [SearchableItemAttribute])](corespotlightsource/init(searchableindexdelegate:fetchattributes:).md)
### Configuring the search options
- [var fetchAttributes: [SearchableItemAttribute]](corespotlightsource/fetchattributes.md)
  The attributes to fetch for each item and provide to the model.
- [var sourceOptions: CSSearchQueryContext.SourceOptions](corespotlightsource/sourceoptions.md)
  Options you use to specify access to restricted content.
- [var maximumResultCount: Int?](corespotlightsource/maximumresultcount.md)
  The maximum number of results to retrieve from this source.
### Providing additional attributes
- [var searchableIndexDelegate: (any CSSearchableIndexDelegate)?](corespotlightsource/searchableindexdelegate.md)
  An optional delegate object you use to provide additional data about items in search results.
- [protocol CSSearchableIndexDelegate](cssearchableindexdelegate.md)
  A protocol that defines methods a delegate object or app extension uses to handle communication from the on-device index.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct SearchSource](searchsource.md)
  A source of data for Spotlight to search.
- [struct FileSource](filesource.md)
  A search source that retrieves indexed metadata from files and directories visible to Spotlight.
- [struct SearchableItemAttribute](searchableitemattribute.md)
  An attribute from a content item that the Spotlight search tool can include in search results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/corespotlightsource)*