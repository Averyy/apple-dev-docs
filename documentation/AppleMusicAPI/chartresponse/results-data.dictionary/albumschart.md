# ChartResponse.Results.AlbumsChart

**Framework**: Apple Music API  
**Kind**: dictionary

The albums results of a chart.

**Availability**:
- Apple Music 1.0+

## Declaration

```swift
object ChartResponse.Results.AlbumsChart
```

## Properties

- `chart` (string) *(required)*: The unique name of the chart to use when fetching a specific chart.
- `data` ([Albums]) *(required)*: The popularity-ordered albums for the chart.
- `href` (string): A relative location to fetch the chart results directly.
- `name` (string) *(required)*: The localized display name for the chart.
- `next` (string): A relative cursor to fetch the next paginated results for the chart if more exist.

## See Also

- [object ChartResponse.Results.MusicVideosChart](chartresponse/results-data.dictionary/musicvideoschart.md)
  The music videos results of a chart.
- [object ChartResponse.Results.PlaylistsChart](chartresponse/results-data.dictionary/playlistschart.md)
  The playlists results of a chart.
- [object ChartResponse.Results.SongsChart](chartresponse/results-data.dictionary/songschart.md)
  The songs results of a chart.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/chartresponse/results-data.dictionary/albumschart)*