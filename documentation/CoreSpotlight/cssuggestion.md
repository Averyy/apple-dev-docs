# CSSuggestion

**Framework**: Core Spotlight  
**Kind**: class  
**Role**: Class

The kind of suggestion to use in a query.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class CSSuggestion
```

```objc
@interface CSSuggestion : NSObject
```

## Mentions

- [Building a search interface for your app](./building-a-search-interface-for-your-app.md)

#### Overview

Your app uses `CSSuggestion` objects to populate a contextual menu of suggestions.

## Topics

### Setting suggestion attributes
- [var localizedAttributedSuggestion: AttributedString](./cssuggestion/localizedattributedsuggestion-3ssly.md)
  An attributed string for the localized suggestion.
- [var suggestionKind: CSSuggestion.SuggestionKind](./cssuggestion/suggestionkind-swift.property.md)
  The type of suggestion.
- [CSSuggestion.SuggestionKind](./cssuggestion/suggestionkind-swift.enum.md)
  The suggestion type that determines how the system handles a suggestion.
### Comparing suggestions
- [func compare(CSSuggestion) -> ComparisonResult](./cssuggestion/compare%28_%29.md)
  Compares the suggestion with a second specified suggestion.
- [func compare(byRank: CSSuggestion) -> ComparisonResult](./cssuggestion/compare%28byrank%29.md)
### Initializers
- [init?(coder: NSCoder)](./cssuggestion/init%28coder%29.md)
### Instance Properties
- [localizedAttributedSuggestion](./cssuggestion/localizedattributedsuggestion-oq3b.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Queries
- [Building a search interface for your app](./building-a-search-interface-for-your-app.md)
  Add a search interface to your app to execute Spotlight queries and offer suggested text completions.
- [Searching for information in your app](./searching-for-information-in-your-app.md)
  Search for app-specific content and refine search results using predicates and filters.
- [class CSUserQuery](./csuserquery.md)
  A type you use to initiate searches from your interface and offer suggested text completions.
- [class CSUserQueryContext](./csuserquerycontext.md)
  The configuration details to apply to a user query.
- [class CSSearchQuery](./cssearchquery.md)
  A type you use to programmatically search the indexed app content.
- [class CSSearchQueryContext](./cssearchquerycontext.md)
  The behavior configuration to use for a search query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssuggestion)*