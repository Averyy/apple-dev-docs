# Artists.Views.ArtistsTopMusicVideosView

**Framework**: Apple Music API  
**Kind**: dictionary  
**Role**: Object

A relationship view from this artist to relevant music videos associated with the artist.

**Availability**:
- Apple Music 1.0+

## Declaration

```
object Artists.Views.ArtistsTopMusicVideosView
```

## Topics

### Related Objects
- [object Artists.Views.ArtistsTopMusicVideosView.Attributes](./artiststopmusicvideosview/attributes-data.dictionary.md)
  Relevant music videos associated with the artist.

## Properties

- `href` (string): A relative location for the view.
- `next` (string): A relative cursor to fetch the next paginated collection of resources in the view if more exist.
- `attributes` (Artists.Views.ArtistsTopMusicVideosView.Attributes) *(required)*: The attributes for the view.
- `data` ([MusicVideos]) *(required)*: Relevant music videos associated with the artist.

## See Also

### Related Objects
- [object Artists.Views.ArtistsAppearsOnAlbumsView](./artistsappearsonalbumsview.md)
  A relationship view from this artist to a selection of albums from other artists on which this artist also appears.
- [object Artists.Views.ArtistsCompilationAlbumsView](./artistscompilationalbumsview.md)
  A relationship view from this artist to albums associated with the artist categorized as compilations.
- [object Artists.Views.ArtistsFeaturedAlbumsView](./artistsfeaturedalbumsview.md)
  A relationship view from this artist to a collection of albums selected as featured for the artist.
- [object Artists.Views.ArtistsFeaturedMusicVideosView](./artistsfeaturedmusicvideosview.md)
  A relationship view from this artist to a collection of music videos selected as featured for the artist.
- [object Artists.Views.ArtistsFeaturedPlaylistsView](./artistsfeaturedplaylistsview.md)
  A relationship view from this artist to relevant playlists associated with the artist.
- [object Artists.Views.ArtistsFullAlbumsView](./artistsfullalbumsview.md)
  A relationship view from this artist to full-release albums associated with the artist.
- [object Artists.Views.ArtistsLatestReleaseView](./artistslatestreleaseview.md)
  A relationship view from this artist to the latest release for the artist determined to still be recent by the Apple Music Catalog.
- [object Artists.Views.ArtistsLiveAlbumsView](./artistslivealbumsview.md)
  A relationship view from this artist to albums associated with the artist categorized as live performances.
- [object Artists.Views.ArtistsSimilarArtistsView](./artistssimilarartistsview.md)
  A relationship view from this artist to other artists similar to this artist.
- [object Artists.Views.ArtistsSinglesView](./artistssinglesview.md)
  A relationship view from this artist to albums associated with the artist categorized as singles.
- [object Artists.Views.ArtistsTopSongsView](./artiststopsongsview.md)
  A relationship view from this artist to songs associated with the artist based on popularity in the current storefront.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/artists/views-data.dictionary/artiststopmusicvideosview)*