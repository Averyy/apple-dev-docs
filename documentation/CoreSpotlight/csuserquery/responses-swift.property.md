# responses

**Framework**: Core Spotlight  
**Kind**: property

The matching results and suggestions for the current query string.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var responses: CSUserQuery.Responses { get }
```

## Mentions

- [Building a search interface for your app](building-a-search-interface-for-your-app.md)

#### Discussion

Getting the value of this property starts the query and begins the delivery of responses. Typically, you get this property as part of a `for..in` loop to iterate over the responses, as shown in the following example:

```swift
var results: [CSUserQuery.Item] = []
var suggestions: [CSUserQuery.Suggestion] = []
let query = CSUserQuery(userQueryString: searchText, userQueryContext: queryContext)

for try await element in query.responses {
    switch(element) {
        case .item(let item):
            self.results.append(item)
            break
        case .suggestion(let suggestion):
            self.suggestions.append(suggestion)
            break
        @unknown default:
            break
    }
}
```

## See Also

- [var suggestions: CSUserQuery.Suggestions](csuserquery/suggestions-swift.property.md)
  An asynchronous sequence of suggested completions for the current query text.
- [CSUserQuery.Responses](csuserquery/responses-swift.struct.md)
  An asynchronous sequence that contains the results and suggestions for a query string.
- [CSUserQuery.Suggestions](csuserquery/suggestions-swift.struct.md)
  An asynchronous sequence that contains the suggested completions for a search string.
- [CSUserQuery.Item](csuserquery/item.md)
  A search result that the query returns in a response.
- [CSUserQuery.Suggestion](csuserquery/suggestion.md)
  A suggested text completion for a query’s search term.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/csuserquery/responses-swift.property)*