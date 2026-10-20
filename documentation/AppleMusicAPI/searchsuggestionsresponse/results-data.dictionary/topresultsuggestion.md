# SearchSuggestionsResponse.Results.TopResultSuggestion

**Framework**: Apple Music API  
**Kind**: dictionary  
**Role**: Object

A suggested popular result for similar search prefix terms.

**Availability**:
- Apple Music 1.0+

## Declaration

```
object SearchSuggestionsResponse.Results.TopResultSuggestion
```

## Properties

- `content` ((Activities | Albums | AppleCurators | Artists | Curators | MusicVideos | Playlists | RecordLabels | Songs | Stations)) *(required)*: The actual resource for the suggested content.

  **Allowed Types**: `Activities`, `Albums`, `AppleCurators`, `Artists`, `Curators`, `MusicVideos`, `Playlists`, `RecordLabels`, `Songs`, `Stations`
- `kind` (string) *(required)*: The kind of suggestion.

  **Allowed Values**: `topResults`

## See Also

### Related Objects
- [object SearchSuggestionsResponse.Results.TermSuggestion](./termsuggestion.md)
  A suggested search term from a search suggestion response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/searchsuggestionsresponse/results-data.dictionary/topresultsuggestion)*