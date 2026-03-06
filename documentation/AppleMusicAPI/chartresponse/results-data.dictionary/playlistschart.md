# ChartResponse.Results.PlaylistsChart

**Framework**: Apple Music API  
**Kind**: dictionary

The playlists results of a chart.

**Availability**:
- Apple Music 1.0+

## Declaration

```swift
object ChartResponse.Results.PlaylistsChart
```

## Properties

- `chart` (string) *(required)*: The unique name of the chart to use when fetching a specific chart.
- `data` ([Playlists]) *(required)*: The popularity-ordered playlists for the chart.
- `href` (string): A relative location to fetch the chart results directly.
- `name` (string) *(required)*: The localized display name for the chart.
- `next` (string): A relative cursor to fetch the next paginated results for the chart if more exist.

## See Also

- [object ChartResponse.Results.AlbumsChart](chartresponse/results-data.dictionary/albumschart.md)
  The albums results of a chart.
- [object ChartResponse.Results.MusicVideosChart](chartresponse/results-data.dictionary/musicvideoschart.md)
  The music videos results of a chart.
- [object ChartResponse.Results.SongsChart](chartresponse/results-data.dictionary/songschart.md)
  The songs results of a chart.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/chartresponse/results-data.dictionary/playlistschart)*