# FileSource

**Framework**: Core Spotlight  
**Kind**: struct

A search source that retrieves indexed metadata from files and directories visible to Spotlight.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct FileSource
```

## Mentions

- [Making your indexed content available to Foundation Models](making-your-indexed-content-available-to-foundation-models.md)

#### Overview

Use this type to search the metadata of your app’s custom file types. Configure the source with one or more directories for the tool to search. During a query, the Spotlight considers only the previously indexed files in those directories. When it finds a match, the tool delivers the item and any attributes you specify in the [`fetchAttributes`](filesource/fetchattributes.md) property to the model for consideration.

For more information about indexing your app’s files, see [`CSImportExtension`](csimportextension.md).

## Topics

### Creating a file source
- [init(fetchAttributes: [SearchableItemAttribute])](filesource/init(fetchattributes:).md)
### Configuring the search options
- [var fetchAttributes: [SearchableItemAttribute]](filesource/fetchattributes.md)
  The attributes to fetch for each file or directory and provide to the model.
- [var scopes: [URL]](filesource/scopes.md)
  The directories to search.
- [var maximumResultCount: Int?](filesource/maximumresultcount.md)
  The maximum number of results to retrieve from this source.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [struct SearchSource](searchsource.md)
  A source of data for Spotlight to search.
- [struct CoreSpotlightSource](corespotlightsource.md)
  A search source that retrieves data from the app’s Spotlight index.
- [struct SearchableItemAttribute](searchableitemattribute.md)
  An attribute from a content item that the Spotlight search tool can include in search results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/filesource)*