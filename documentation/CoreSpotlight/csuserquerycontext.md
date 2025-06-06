# CSUserQueryContext

**Framework**: Core Spotlight  
**Kind**: class

The configuration details to apply to a user query.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class CSUserQueryContext
```

## Mentions

- [Building a search interface for your app](building-a-search-interface-for-your-app.md)

#### Overview

Use an instance of `CSUserQueryContext` to configure the search parameters for a [`CSUserQuery`](csuserquery.md) object. This object stores configuration details that the query uses to modify the search results it delivers. For example, use this object to specify the maximum number of results or suggestions you want the query to return. You can also use it to enable or disable the ranking of results by Spotlight.

For information about search filters and other configurable query parameters, see the parent class [`CSSearchQueryContext`](cssearchquerycontext.md).

## Topics

### Creating a query context
- [init(currentSuggestion: CSSuggestion?)](csuserquerycontext/init(currentsuggestion:).md)
  Creates a new query context object with an optional suggested search string.
### Configuring search options
- [var maxResultCount: Int](csuserquerycontext/maxresultcount.md)
  The maximum number of search results for the query to return.
- [var maxSuggestionCount: Int](csuserquerycontext/maxsuggestioncount.md)
  The maximum number of suggested text completions for the query to return.
- [var disableSemanticSearch: Bool](csuserquerycontext/disablesemanticsearch.md)
  A Boolean value that indicates whether to exclude semantic-based search results from the output.
### Configuring the ranked results behavior
- [var enableRankedResults: Bool](csuserquerycontext/enablerankedresults.md)
  A Boolean value that indicates whether the query sorts results by their relevance.
- [var maxRankedResultCount: Int](csuserquerycontext/maxrankedresultcount.md)
  The maximum number of ranked results to return during the query.

## Relationships

### Inherits From
- [CSSearchQueryContext](cssearchquerycontext.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [Building a search interface for your app](building-a-search-interface-for-your-app.md)
  Add a search interface to your app to execute Spotlight queries and offer suggested text completions.
- [Searching for information in your app](searching-for-information-in-your-app.md)
  Search for app-specific content and refine search results using predicates and filters.
- [class CSUserQuery](csuserquery.md)
  A type you use to initiate searches from your interface and offer suggested text completions.
- [class CSSearchQuery](cssearchquery.md)
  A type you use to programmatically search the indexed app content.
- [class CSSearchQueryContext](cssearchquerycontext.md)
  The behavior configuration to use for a search query.
- [class CSSuggestion](cssuggestion.md)
  The kind of suggestion to use in a query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/csuserquerycontext)*