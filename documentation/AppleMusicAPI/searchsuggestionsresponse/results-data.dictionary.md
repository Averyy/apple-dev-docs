# SearchSuggestionsResponse.Results

**Framework**: Apple Music API  
**Kind**: dictionary  
**Role**: Object

An object that represents the results of a search suggestions query.

**Availability**:
- Apple Music 1.0+

## Declaration

```
object SearchSuggestionsResponse.Results
```

## Topics

### Related Objects
- [object SearchSuggestionsResponse.Results.TermSuggestion](./results-data.dictionary/termsuggestion.md)
  A suggested search term from a search suggestion response.
- [object SearchSuggestionsResponse.Results.TopResultSuggestion](./results-data.dictionary/topresultsuggestion.md)
  A suggested popular result for similar search prefix terms.

## Properties

- `suggestions` ([*]) *(required)*: An array of possible valid search queries determined from the search suggestion.

  **Allowed Types**: `SearchSuggestionsResponse.Results.TermSuggestion`, `SearchSuggestionsResponse.Results.TopResultSuggestion`


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/searchsuggestionsresponse/results-data.dictionary)*