# CSUserQuery.Suggestion

**Framework**: Core Spotlight  
**Kind**: struct

A suggested text completion for a query’s search term.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
struct Suggestion
```

## Mentions

- [Building a search interface for your app](building-a-search-interface-for-your-app.md)

#### Discussion

When executing its query, a [`CSUserQuery`](csuserquery.md) object returns both results and suggestions for text completions of the current term. Use the [`suggestion`](csuserquery/suggestion/suggestion.md) property of this structure to get one of the suggestions to display in your app’s interface and use in a new query.

## Topics

### Instance Properties
- [var suggestion: CSSuggestion](csuserquery/suggestion/suggestion.md)

## Relationships

### Conforms To
- [Comparable](../Swift/Comparable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var responses: CSUserQuery.Responses](csuserquery/responses-swift.property.md)
  The matching results and suggestions for the current query string.
- [var suggestions: CSUserQuery.Suggestions](csuserquery/suggestions-swift.property.md)
  An asynchronous sequence of suggested completions for the current query text.
- [CSUserQuery.Responses](csuserquery/responses-swift.struct.md)
  An asynchronous sequence that contains the results and suggestions for a query string.
- [CSUserQuery.Suggestions](csuserquery/suggestions-swift.struct.md)
  An asynchronous sequence that contains the suggested completions for a search string.
- [CSUserQuery.Item](csuserquery/item.md)
  A search result that the query returns in a response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/csuserquery/suggestion)*