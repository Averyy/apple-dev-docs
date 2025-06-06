# CSSearchQueryContext

**Framework**: Core Spotlight  
**Kind**: class

The behavior configuration to use for a search query.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
class CSSearchQueryContext
```

## Mentions

- [Searching for information in your app](searching-for-information-in-your-app.md)

## Topics

### Configuring search behavior
- [var fetchAttributes: [String]](cssearchquerycontext/fetchattributes.md)
  The attributes the system fetches for the searchable items.
- [var keyboardLanguage: String?](cssearchquerycontext/keyboardlanguage.md)
  The language used for the query.
- [var sourceOptions: CSSearchQueryContext.SourceOptions](cssearchquerycontext/sourceoptions-swift.property.md)
  The query source options to allow or deny Mail messages in the search.
- [CSSearchQueryContext.SourceOptions](cssearchquerycontext/sourceoptions-swift.struct.md)
  The query source options to allow or deny Mail messages in the search.
### Filtering the results
- [var filterQueries: [String]](cssearchquerycontext/filterqueries.md)
  The query string used to filter the results.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [CSUserQueryContext](csuserquerycontext.md)
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
- [class CSUserQueryContext](csuserquerycontext.md)
  The configuration details to apply to a user query.
- [class CSSearchQuery](cssearchquery.md)
  A type you use to programmatically search the indexed app content.
- [class CSSuggestion](cssuggestion.md)
  The kind of suggestion to use in a query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchquerycontext)*