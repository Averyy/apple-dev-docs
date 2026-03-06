# SearchSuggestionsResponse.Results.TermSuggestion

**Framework**: Apple Music API  
**Kind**: dictionary

A suggested search term from a search suggestion response.

**Availability**:
- Apple Music 1.0+

## Declaration

```swift
object SearchSuggestionsResponse.Results.TermSuggestion
```

## Properties

- `displayTerm` (string) *(required)*: A potentially censored term to display to the user to select from. Use the `searchTerm` value for the actual search.
- `kind` (string) *(required)*: The kind of suggestion.
- `searchTerm` (string) *(required)*: The term to use as a search input when using this suggestion.

## See Also

- [object SearchSuggestionsResponse.Results.TopResultSuggestion](searchsuggestionsresponse/results-data.dictionary/topresultsuggestion.md)
  A suggested popular result for similar search prefix terms.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/searchsuggestionsresponse/results-data.dictionary/termsuggestion)*