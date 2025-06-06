# maxSuggestionCount

**Framework**: Core Spotlight  
**Kind**: property

The maximum number of suggested text completions for the query to return.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var maxSuggestionCount: Int { get set }
```

#### Discussion

You might specify different limits to account for the amount of available space.

## See Also

- [var maxResultCount: Int](csuserquerycontext/maxresultcount.md)
  The maximum number of search results for the query to return.
- [var disableSemanticSearch: Bool](csuserquerycontext/disablesemanticsearch.md)
  A Boolean value that indicates whether to exclude semantic-based search results from the output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/csuserquerycontext/maxsuggestioncount)*