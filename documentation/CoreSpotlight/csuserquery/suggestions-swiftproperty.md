# suggestions

**Framework**: Core Spotlight  
**Kind**: property

An asynchronous sequence of suggested completions for the current query text.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var suggestions: CSUserQuery.Suggestions { get }
```

#### Discussion

Getting the value of this property starts the query and begins the delivery of suggestions. Typically, you get this property as part of a `for..in` loop to iterate over the suggestions and display them in your interface.

## See Also

- [var responses: CSUserQuery.Responses](csuserquery/responses-swift.property.md)
  The matching results and suggestions for the current query string.
- [CSUserQuery.Responses](csuserquery/responses-swift.struct.md)
  An asynchronous sequence that contains the results and suggestions for a query string.
- [CSUserQuery.Suggestions](csuserquery/suggestions-swift.struct.md)
  An asynchronous sequence that contains the suggested completions for a search string.
- [CSUserQuery.Item](csuserquery/item.md)
  A search result that the query returns in a response.
- [CSUserQuery.Suggestion](csuserquery/suggestion.md)
  A suggested text completion for a query’s search term.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/csuserquery/suggestions-swift.property)*