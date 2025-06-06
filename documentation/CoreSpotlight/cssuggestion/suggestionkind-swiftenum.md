# CSSuggestion.SuggestionKind

**Framework**: Core Spotlight  
**Kind**: enum

The suggestion type that determines how the system handles a suggestion.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
enum SuggestionKind
```

#### Overview

Suggestions that the system returns from the query handler have [`CSSuggestion.SuggestionKind.default`](cssuggestion/suggestionkind-swift.enum/default.md).

## Topics

### Suggestion types
- [CSSuggestion.SuggestionKind.none](cssuggestion/suggestionkind-swift.enum/none.md)
  Blocks the system from displaying the suggestion.
- [CSSuggestion.SuggestionKind.custom](cssuggestion/suggestionkind-swift.enum/custom.md)
  Sorts the custom suggestions together.
- [CSSuggestion.SuggestionKind.default](cssuggestion/suggestionkind-swift.enum/default.md)
  Displays the suggestion normally.
### Initializers
- [init?(rawValue: Int)](cssuggestion/suggestionkind-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var localizedAttributedSuggestion: AttributedString](cssuggestion/localizedattributedsuggestion-3ssly.md)
  An attributed string for the localized suggestion.
- [var suggestionKind: CSSuggestion.SuggestionKind](cssuggestion/suggestionkind-swift.property.md)
  The type of suggestion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssuggestion/suggestionkind-swift.enum)*