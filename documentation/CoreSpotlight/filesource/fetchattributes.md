# fetchAttributes

**Framework**: Core Spotlight  
**Kind**: property

The attributes to fetch for each file or directory and provide to the model.

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

Use this property to minimize the number of round trips between the Spotlight search tool and your content. When you index your app’s content, you create a [`CSSearchableItemAttributeSet`](cssearchableitemattributeset.md) for each item and fill it with metadata about that item. For example, you might specify the title of a document and the number of pages it contains. For each item the Spotlight search tool identifies as a result, the tool retrieves the attributes you specify in this property. The tool delivers these attributes together with the item’s identifier to the model so it doesn’t have to request them later.

The default value of this property is an empty set, which delivers only the item’s identifier to the model.

## See Also

- [var scopes: [URL]](filesource/scopes.md)
  The directories to search.
- [var maximumResultCount: Int?](filesource/maximumresultcount.md)
  The maximum number of results to retrieve from this source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/filesource/fetchattributes)*