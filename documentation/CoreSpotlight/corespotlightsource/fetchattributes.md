# fetchAttributes

**Framework**: Core Spotlight  
**Kind**: property

The attributes to fetch for each item and provide to the model.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var fetchAttributes: [SearchableItemAttribute]
```

#### Discussion

Use this property to minimize the number of round trips between the Spotlight search tool and your content. When you index your app’s content, you create a [`CSSearchableItemAttributeSet`](cssearchableitemattributeset.md) for each item and fill it with metadata about that item. For example, retrieve the display name, author, and subject attributes by setting this property to `[.displayName, .authors, .subject]`. For each item, the tool retrieves the attributes you specify and delivers them to the model.

The default value of this property is an empty set, which delivers only the item’s identifier to the model.

## See Also

- [var sourceOptions: CSSearchQueryContext.SourceOptions](corespotlightsource/sourceoptions.md)
  Options you use to specify access to restricted content.
- [var maximumResultCount: Int?](corespotlightsource/maximumresultcount.md)
  The maximum number of results to retrieve from this source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/corespotlightsource/fetchattributes)*