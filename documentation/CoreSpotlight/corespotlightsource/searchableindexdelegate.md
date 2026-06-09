# searchableIndexDelegate

**Framework**: Core Spotlight  
**Kind**: property

An optional delegate object you use to provide additional data about items in search results.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var searchableIndexDelegate: (any CSSearchableIndexDelegate)?
```

#### Discussion

Use this delegate object to provide detailed information about your searchable items to the model. Some information in the Spotlight index is searchable, but not recoverable. For example, Spotlight can’t recover the original text or HTML content you supply for an item. When it needs this information, the search tool asks your delegate to provide a new [`CSSearchableItem`](cssearchableitem.md) object with the same content as the original one.

If you configure the Spotlight search tool to use the [`SpotlightSearchTool.GuidanceLevel.dynamic(_:)`](spotlightsearchtool/guidancelevel/dynamic(_:).md) guidance level, you can also use this delegate to fill in any missing attributes. Dynamic profiles cause the tool to search specific attributes of each item. If those attributes aren’t available in the index, the tool uses your delegate to recreate the item.

If you don’t provide a delegate object, the tool uses only the information it retrieves from the source.

## See Also

- [protocol CSSearchableIndexDelegate](cssearchableindexdelegate.md)
  A protocol that defines methods a delegate object or app extension uses to handle communication from the on-device index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/corespotlightsource/searchableindexdelegate)*