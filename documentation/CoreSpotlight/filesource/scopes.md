# scopes

**Framework**: Core Spotlight  
**Kind**: property

The directories to search.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var scopes: [URL]
```

#### Discussion

Specify one or more directory URLs to scope the search to those directories and their subdirectories. The default value of this property is an empty array, which searches all indexed volumes.

## See Also

- [var fetchAttributes: [SearchableItemAttribute]](filesource/fetchattributes.md)
  The attributes to fetch for each file or directory and provide to the model.
- [var maximumResultCount: Int?](filesource/maximumresultcount.md)
  The maximum number of results to retrieve from this source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/filesource/scopes)*