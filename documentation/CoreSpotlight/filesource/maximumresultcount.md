# maximumResultCount

**Framework**: Core Spotlight  
**Kind**: property

The maximum number of results to retrieve from this source.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var maximumResultCount: Int?
```

#### Discussion

Use this property to limit the number of results the Spotlight search tool returns to the model. If you specify `nil`, the tool returns all results that match the model’s query. This maximum applies only to the current source, and doesn’t include results from other sources, which have their own maximum values. The default value of this property is `nil`.

## See Also

- [var fetchAttributes: [SearchableItemAttribute]](filesource/fetchattributes.md)
  The attributes to fetch for each file or directory and provide to the model.
- [var scopes: [URL]](filesource/scopes.md)
  The directories to search.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/filesource/maximumresultcount)*