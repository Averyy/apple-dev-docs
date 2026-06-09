# SearchSource

**Framework**: Core Spotlight  
**Kind**: struct

A source of data for Spotlight to search.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct SearchSource
```

#### Overview

When configuring the search tool, use this type to specify whether to retrieve data from the app’s Spotlight index or from files at the specified locations. Each of the sources sets the scope of the search, along with other parameters.

## Topics

### Searching a Spotlight index
- [static var coreSpotlight: SearchSource](searchsource/corespotlight.md)
  A source that retrieves data from the app’s Spotlight index.
- [static func coreSpotlight(CoreSpotlightSource) -> SearchSource](searchsource/corespotlight(_:).md)
  Returns a source that retrieves data from the app’s Spotlight index.
### Searching files and directories
- [static var files: SearchSource](searchsource/files.md)
  A source that retrieves data from the files and directories you specify.
- [static func files(FileSource) -> SearchSource](searchsource/files(_:).md)
  Returns a source that retrieves data from the files and directories you specify.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct CoreSpotlightSource](corespotlightsource.md)
  A search source that retrieves data from the app’s Spotlight index.
- [struct FileSource](filesource.md)
  A search source that retrieves indexed metadata from files and directories visible to Spotlight.
- [struct SearchableItemAttribute](searchableitemattribute.md)
  An attribute from a content item that the Spotlight search tool can include in search results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/searchsource)*