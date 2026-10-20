# CSUserQuery.Suggestions

**Framework**: Core Spotlight  
**Kind**: struct  
**Role**: Structure

An asynchronous sequence that contains the suggested completions for a search string.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
struct Suggestions
```

## Topics

### Structures
- [CSUserQuery.Suggestions.Iterator](./suggestions-swift.struct/iterator.md)

## Relationships

### Conforms To
- [AsyncSequence](../../Swift/asyncsequence.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Executing the query automatically
- [var responses: CSUserQuery.Responses](./responses-swift.property.md)
  The matching results and suggestions for the current query string.
- [var suggestions: CSUserQuery.Suggestions](./suggestions-swift.property.md)
  An asynchronous sequence of suggested completions for the current query text.
- [CSUserQuery.Responses](./responses-swift.struct.md)
  An asynchronous sequence that contains the results and suggestions for a query string.
- [CSUserQuery.Item](./item.md)
  A search result that the query returns in a response.
- [CSUserQuery.Suggestion](./suggestion.md)
  A suggested text completion for a query’s search term.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/csuserquery/suggestions-swift.struct)*