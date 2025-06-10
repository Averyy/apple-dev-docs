# CSUserQuery.Responses

**Framework**: Core Spotlight  
**Kind**: struct

An asynchronous sequence that contains the results and suggestions for a query string.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
struct Responses
```

#### Discussion

A `CSUserQuery/Responses-struct` structure contains the results of a query. Fetch this structure from the [`responses`](csuserquery/responses-swift.property.md) property of your query object to execute the query automatically and begin the delivery of the results. Each element that this structure returns to you is either a search result or a suggested completion of the current search text. Check the element type and handle it accordingly.

For more information about how to use this structure, see the [`responses`](csuserquery/responses-swift.property.md) property.

## Topics

### Getting the response type
- [CSUserQuery.Responses.Response](csuserquery/responses-swift.struct/response.md)
### Iterating over the responses
- [CSUserQuery.Responses.Iterator](csuserquery/responses-swift.struct/iterator.md)

## Relationships

### Conforms To
- [AsyncSequence](../Swift/AsyncSequence.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var responses: CSUserQuery.Responses](csuserquery/responses-swift.property.md)
  The matching results and suggestions for the current query string.
- [var suggestions: CSUserQuery.Suggestions](csuserquery/suggestions-swift.property.md)
  An asynchronous sequence of suggested completions for the current query text.
- [CSUserQuery.Suggestions](csuserquery/suggestions-swift.struct.md)
  An asynchronous sequence that contains the suggested completions for a search string.
- [CSUserQuery.Item](csuserquery/item.md)
  A search result that the query returns in a response.
- [CSUserQuery.Suggestion](csuserquery/suggestion.md)
  A suggested text completion for a query’s search term.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/csuserquery/responses-swift.struct)*