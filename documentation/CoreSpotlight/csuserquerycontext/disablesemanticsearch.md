# disableSemanticSearch

**Framework**: Core Spotlight  
**Kind**: property

A Boolean value that indicates whether to exclude semantic-based search results from the output.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var disableSemanticSearch: Bool { get set }
```

#### Discussion

Semantic searching finds matches that are related to the original term, but not necessarily a lexical match. For example, a search for the string “Sun and Moon” might also return a result with a title like “Sol and Luna”. The default value of this property is `true`, which enables the delivery of semantic search results.

You might set this property to `false` when you want to perform only a lexical match. For example, you might disable semantic search when looking for a proper name.

## See Also

- [var maxResultCount: Int](csuserquerycontext/maxresultcount.md)
  The maximum number of search results for the query to return.
- [var maxSuggestionCount: Int](csuserquerycontext/maxsuggestioncount.md)
  The maximum number of suggested text completions for the query to return.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/csuserquerycontext/disablesemanticsearch)*