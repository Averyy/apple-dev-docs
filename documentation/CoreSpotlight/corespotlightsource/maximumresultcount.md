# maximumResultCount

**Framework**: Core Spotlight  
**Kind**: property

The maximum number of results to retrieve from this source.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var maximumResultCount: Int?
```

#### Discussion

Use this property to limit the number of results the Spotlight search tool returns to the model. If you specify `nil`, the tool returns all results that match the model’s query. This maximum applies only to the current source, and doesn’t include results from other sources, which have their own maximum values. The default value of this property is `nil`.

## See Also

- [var fetchAttributes: [SearchableItemAttribute]](corespotlightsource/fetchattributes.md)
  The attributes to fetch for each item and provide to the model.
- [var sourceOptions: CSSearchQueryContext.SourceOptions](corespotlightsource/sourceoptions.md)
  Options you use to specify access to restricted content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/corespotlightsource/maximumresultcount)*