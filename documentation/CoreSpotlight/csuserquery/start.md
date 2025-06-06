# start()

**Framework**: Corespotlight  
**Kind**: method

Starts searching the index for items that match the current query string and parameters.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func start()
```

## Mentions

- [Building a search interface for your app](building-a-search-interface-for-your-app.md)

#### Discussion

This method uses the configured search parameters and query string to begin a search of the index. It then delivers the results of that search to the closures in the [`foundItemsHandler`](cssearchquery/founditemshandler.md), [`foundSuggestionsHandler`](csuserquery/foundsuggestionshandler.md), and [`completionHandler`](cssearchquery/completionhandler.md) properties of the query object.

> **Note**: Don’t call this method if you fetch the query results using the [`responses`](csuserquery/responses-swift.property.md) property. Accessing that property automatically starts the query.

## See Also

- [func cancel()](csuserquery/cancel.md)
  Cancels the current query operation.
- [var foundSuggestionsHandler: (([CSSuggestion]) -> Void)?](csuserquery/foundsuggestionshandler.md)
  The block to execute when the query delivers a new batch of suggested items.
- [var foundSuggestionCount: Int](csuserquery/foundsuggestioncount.md)
  The number of suggested items the query found so far.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/csuserquery/start())*