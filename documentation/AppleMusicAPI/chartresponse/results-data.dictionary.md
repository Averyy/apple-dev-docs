# ChartResponse.Results

**Framework**: Apple Music API  
**Kind**: dictionary  
**Role**: Object

A mapping of a requested type to an array of charts.

**Availability**:
- Apple Music 1.0+

## Declaration

```
object ChartResponse.Results
```

## Topics

### Related Objects
- [object ChartResponse.Results.AlbumsChart](./results-data.dictionary/albumschart.md)
  The albums results of a chart.
- [object ChartResponse.Results.MusicVideosChart](./results-data.dictionary/musicvideoschart.md)
  The music videos results of a chart.
- [object ChartResponse.Results.PlaylistsChart](./results-data.dictionary/playlistschart.md)
  The playlists results of a chart.
- [object ChartResponse.Results.SongsChart](./results-data.dictionary/songschart.md)
  The songs results of a chart.

## Properties

- `albums` ([ChartResponse.Results.AlbumsChart]) *(required)*: The albums results of a chart.
- `music-videos` ([ChartResponse.Results.MusicVideosChart]) *(required)*: The music videos results of a chart.
- `playlists` ([ChartResponse.Results.PlaylistsChart]) *(required)*: The playlists results of a chart.
- `songs` ([ChartResponse.Results.SongsChart]) *(required)*: The songs results of a chart.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/chartresponse/results-data.dictionary)*