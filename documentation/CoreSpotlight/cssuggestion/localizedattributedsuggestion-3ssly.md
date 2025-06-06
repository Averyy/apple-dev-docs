# localizedAttributedSuggestion

**Framework**: Core Spotlight  
**Kind**: property

An attributed string for the localized suggestion.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var localizedAttributedSuggestion: AttributedString { get }
```

#### Discussion

The `localizedAttributedString` provides the suggestion text that the system uses to replace the text in the search bar. The system uses the attributed string to highlight the range of the suggestion string that matches the user query string.

For example, the user types “search”, and the system offers a suggestion for “search suggestion”, where the system marks up “search” using the [`CSSuggestionHighlightAttributeName`](cssuggestionhighlightattributename.md). Your app can use the range to add a bold highlight, if desired.

## See Also

- [var suggestionKind: CSSuggestion.SuggestionKind](cssuggestion/suggestionkind-swift.property.md)
  The type of suggestion.
- [CSSuggestion.SuggestionKind](cssuggestion/suggestionkind-swift.enum.md)
  The suggestion type that determines how the system handles a suggestion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssuggestion/localizedattributedsuggestion-3ssly)*