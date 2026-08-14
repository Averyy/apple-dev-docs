# CSUserQuery.Item

**Framework**: Core Spotlight  
**Kind**: struct

A search result that the query returns in a response.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
struct Item
```

## Topics

### Instance Properties
- [var item: CSSearchableItem](csuserquery/item/item.md)

## Relationships

### Conforms To
- [Comparable](../swift/comparable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Identifiable](../swift/identifiable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var responses: CSUserQuery.Responses](csuserquery/responses-swift.property.md)
  The matching results and suggestions for the current query string.
- [var suggestions: CSUserQuery.Suggestions](csuserquery/suggestions-swift.property.md)
  An asynchronous sequence of suggested completions for the current query text.
- [CSUserQuery.Responses](csuserquery/responses-swift.struct.md)
  An asynchronous sequence that contains the results and suggestions for a query string.
- [CSUserQuery.Suggestions](csuserquery/suggestions-swift.struct.md)
  An asynchronous sequence that contains the suggested completions for a search string.
- [CSUserQuery.Suggestion](csuserquery/suggestion.md)
  A suggested text completion for a query’s search term.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/csuserquery/item)*