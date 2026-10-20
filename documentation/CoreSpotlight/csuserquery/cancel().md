# cancel()

**Framework**: Core Spotlight  
**Kind**: method

Cancels the current query operation.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func cancel()
```

#### Discussion

Cancel a query operation when you no longer need the results. You can use this method to cancel queries started using either the [`start()`](csuserquery/start().md) method or by accessing the [`responses`](csuserquery/responses-swift.property.md) property.  After you cancel a query operation, you can’t restart it. To perform a new query, create a new query object. For example, you might cancel one query and start a new one when the text in your app’s search control changes.

## See Also

- [func start()](csuserquery/start.md)
  Starts searching the index for items that match the current query string and parameters.
- [var foundSuggestionsHandler: (([CSSuggestion]) -> Void)?](csuserquery/foundsuggestionshandler.md)
  The block to execute when the query delivers a new batch of suggested items.
- [var foundSuggestionCount: Int](csuserquery/foundsuggestioncount.md)
  The number of suggested items the query found so far.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/csuserquery/cancel())*