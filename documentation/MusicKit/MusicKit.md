# MusicKit

**Framework**: MusicKit  
**Kind**: module

Integrate your app with Apple Music.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

#### Overview

Use MusicKit to integrate your app with [`Apple Music API`](https://developer.apple.com/documentation/AppleMusicAPI), a web service you use to access information about music items in the Apple Music catalog. Using MusicKit, you can more easily build apps that tie into Apple Music.

The framework provides a model layer for accessing music items in Swift, as well as playback support so you can add music to your app. Additionally, it provides some related user interface elements, such as a view to display images that correspond to artwork for a music item, or a way to present music subscription offers to users who may not have an active Apple Music subscription.

> ❗ **Important**: Users must grant permission for your app to access their music data. Add the [`NSAppleMusicUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSAppleMusicUsageDescription) key to your app’s `Info.plist` file, and include a description of how you intend to use the user’s media. If this key isn’t present, the system terminates your app when it tries to access the user’s music.

Request permission for your app to use MusicKit with [`MusicAuthorization`](musicauthorization.md). Check specific capabilities for the current [`MusicSubscription`](musicsubscription.md) to ensure your music-related functionality is available to the user. Find music items using a search term with [`MusicCatalogSearchRequest`](musiccatalogsearchrequest.md), or find music items using a filter with [`MusicCatalogResourceRequest`](musiccatalogresourcerequest.md). Play music in your app with one of the two music players that MusicKit offers. Allow the user to begin a free trial for Apple Music from within your app by presenting a music subscription offer.

You can load content from an arbitrary Apple Music API endpoint with [`MusicDataRequest`](musicdatarequest.md) to take further advantage of additional functionality available in Apple Music API.

## Topics

### Essentials
- [Using Automatic Developer Token Generation for Apple Music API](using-automatic-token-generation-for-apple-music-api.md)
  Enable your app’s integration with the MusicKit App Service in the developer portal.
- [Using MusicKit to Integrate with Apple Music](using_musickit_to_integrate_with_apple_music.md)
  Find an album in Apple Music that corresponds to a CD in a user’s collection, and present the information for the album.
- [NSAppleMusicUsageDescription](../BundleResources/Information-Property-List/NSAppleMusicUsageDescription.md)
  A message that tells the user why the app is requesting access to the user’s media library.
### Music Items
- [struct Album](album.md)
  A music item that represents an album.
- [struct Artist](artist.md)
  A music item that represents an artist.
- [struct Curator](curator.md)
  A music item that represents a curator.
- [struct Genre](genre.md)
  A music item that represents a genre.
- [struct MusicVideo](musicvideo.md)
  A music item that represents a music video.
- [struct Playlist](playlist.md)
  A music item that represents a playlist.
- [struct RadioShow](radioshow.md)
  A music item that represents a radio show.
- [struct RecordLabel](recordlabel.md)
  A music item that represents a record label.
- [struct Song](song.md)
  A music item that represents a song.
- [struct Station](station.md)
  A music item that represents a station.
- [enum Track](track.md)
  A music item that represents a track.
### Music Item Attributes
- [enum ContentRating](contentrating.md)
  The rating of the content that potentially plays while playing a resource.
- [struct EditorialNotes](editorialnotes.md)
  An object that represents editorial notes.
- [struct PreviewAsset](previewasset.md)
  An object that represents a preview for resources.
### Catalog Search
- [struct MusicCatalogSearchRequest](musiccatalogsearchrequest.md)
  A request that your app uses to fetch items from the Apple Music catalog using a search term.
- [struct MusicCatalogSearchResponse](musiccatalogsearchresponse.md)
  An object that contains results for a catalog search request.
- [protocol MusicCatalogSearchable](musiccatalogsearchable.md)
  A protocol for music items that your app can fetch by using a catalog search request.
### Resource Loading Using Filters
- [struct MusicCatalogResourceRequest](musiccatalogresourcerequest.md)
  A request that your app uses to fetch items from the Apple Music catalog using a filter.
- [struct MusicCatalogResourceResponse](musiccatalogresourceresponse.md)
  An object that contains results for a catalog resource request.
- [protocol AlbumFilter](albumfilter.md)
  Album properties your app uses as a filter for a catalog resource request.
- [protocol ArtistFilter](artistfilter.md)
  Artist properties your app uses as a filter for a catalog resource request.
- [protocol CuratorFilter](curatorfilter.md)
  Curator properties your app uses as a filter for a catalog resource request.
- [protocol GenreFilter](genrefilter.md)
  Genre properties your app uses as a filter for a catalog resource request.
- [protocol MusicVideoFilter](musicvideofilter.md)
  Music video properties your app uses as a filter for a catalog resource request.
- [protocol PlaylistFilter](playlistfilter.md)
  Playlist properties your app uses as a filter for a catalog resource request.
- [protocol RadioShowFilter](radioshowfilter.md)
  Radio Show properties your app uses as a filter for a catalog resource request.
- [protocol RecordLabelFilter](recordlabelfilter.md)
  The set of record label properties your app uses as a filter for a catalog resource request.
- [protocol SongFilter](songfilter.md)
  Song properties your app uses as a filter for a catalog resource request.
- [protocol StationFilter](stationfilter.md)
  The set of station properties your app uses as a filter for a catalog resource request.
- [protocol FilterableMusicItem](filterablemusicitem.md)
  A declaration of the associated type that contains the set of music item properties your app uses as a filter for a catalog resource request.
### General Purpose Data Request
- [struct MusicDataRequest](musicdatarequest.md)
  A request for loading data from an arbitrary Apple Music API endpoint.
- [struct MusicDataResponse](musicdataresponse.md)
  An object containing results for a data request.
### Playback
- [class ApplicationMusicPlayer](applicationmusicplayer.md)
  An object your app uses to play music in a way that doesn’t affect the Music app’s state.
- [class SystemMusicPlayer](systemmusicplayer.md)
  An object your app uses to play music by controlling the Music app’s state.
- [class MusicPlayer](musicplayer.md)
  An object your app uses to play music.
- [protocol PlayableMusicItem](playablemusicitem.md)
  A set of properties that a music player uses to initiate playback for a music item.
- [struct PlayParameters](playparameters.md)
  An opaque object that represents parameters to initiate playback of a playable music item using a music player.
### Artwork
- [struct Artwork](artwork.md)
  An object that represents artwork for a music item.
- [struct ArtworkImage](artworkimage.md)
  A view that displays the image for a music item’s artwork.
### Authorization
- [struct MusicAuthorization](musicauthorization.md)
  A type that allows you to request the user’s informed consent for your app to access their music data.
### Apple Music Subscription
- [struct MusicSubscription](musicsubscription.md)
  A representation of the current state of the user’s subscription to Apple Music.
- [struct MusicSubscriptionOffer](musicsubscriptionoffer.md)
  A type for grouping other types for showing subscription offers for Apple Music.
### Token management
- [typealias MusicTokenProvider](musictokenprovider.md)
  An object that music requests use to access Apple Music API.
- [protocol MusicDeveloperTokenProvider](musicdevelopertokenprovider.md)
  A set of methods that music requests use to access Apple Music API.
- [class MusicUserTokenProvider](musicusertokenprovider.md)
  A class that music requests use to fetch user tokens your app requires to access Apple Music API.
- [struct MusicTokenRequestOptions](musictokenrequestoptions.md)
  Options that music requests pass into token provider methods to fetch a required token for accessing Apple Music API.
- [enum MusicTokenRequestError](musictokenrequesterror.md)
  An error that the token provider or music requests can throw upon requesting any token necessary for accessing Apple Music API.
- [class DefaultMusicTokenProvider](defaultmusictokenprovider.md)
  The default token provider that music requests use to access Apple Music API.
### Utility
- [protocol MusicItem](musicitem.md)
  A protocol with basic requirements for music items.
- [struct MusicItemID](musicitemid.md)
  An object that represents a unique identifier for a music item.
- [struct MusicItemCollection](musicitemcollection.md)
  A collection of music items.
- [protocol MusicPropertyContainer](musicpropertycontainer.md)
  A protocol for music items that allow loading additional properties that you can fetch asynchronously.
- [class MusicRelationshipProperty](musicrelationshipproperty.md)
  An identifier for a music item relationship property from a specific root type to a specific value type for the element of the resulting collection.
- [class MusicExtendedAttributeProperty](musicextendedattributeproperty.md)
  An identifier for a music item extended attribute property from a specific root type to a specific resulting value type.
- [class MusicAttributeProperty](musicattributeproperty.md)
  An identifier for a music item attribute property from a specific root type to a specific resulting value type.
- [class PartialMusicAsyncProperty](partialmusicasyncproperty.md)
  A partially type-erased identifier for a music item property that you can fetch asynchronously from a concrete root type to any resulting value type.
- [class PartialMusicProperty](partialmusicproperty.md)
  A partially type-erased identifier for a music item property from a concrete root type to any resulting value type.
- [class AnyMusicProperty](anymusicproperty.md)
  A type-erased identifier for a music item property, from any root type to any resulting value type.
### Classes
- [class MusicLibrary](musiclibrary.md)
  An object your app uses to access the user’s music library.
### Protocols
- [protocol LibraryAlbumFilter](libraryalbumfilter.md)
  Album properties your app uses as a filter for a library request.
- [protocol LibraryAlbumSortProperties](libraryalbumsortproperties.md)
  Album properties your app uses to sort results for a library request.
- [protocol LibraryArtistFilter](libraryartistfilter.md)
  Artist properties your app uses as a filter for a library request.
- [protocol LibraryArtistSortProperties](libraryartistsortproperties.md)
  Artist properties your app uses to sort results for a library request.
- [protocol LibraryGenreFilter](librarygenrefilter.md)
  Genre properties your app uses as a filter for a library request.
- [protocol LibraryGenreSortProperties](librarygenresortproperties.md)
  Genre properties your app uses to sort results for a library request.
- [protocol LibraryMusicVideoFilter](librarymusicvideofilter.md)
  Music video properties your app uses as a filter for a library request.
- [protocol LibraryMusicVideoSortProperties](librarymusicvideosortproperties.md)
  Music video properties your app uses to sort results for a library request.
- [protocol LibraryPlaylistEntryFilter](libraryplaylistentryfilter.md)
  Playlist entry properties your app uses as a filter for a library request.
- [protocol LibraryPlaylistEntrySortProperties](libraryplaylistentrysortproperties.md)
  Playlist entry properties your app uses to sort results for a library request.
- [protocol LibraryPlaylistFilter](libraryplaylistfilter.md)
  Playlist properties your app uses as a filter for a library request.
- [protocol LibraryPlaylistSortProperties](libraryplaylistsortproperties.md)
  Playlist properties your app uses to sort results for a library request.
- [protocol LibrarySongFilter](librarysongfilter.md)
  Song properties your app uses as a filter for a library request.
- [protocol LibrarySongSortProperties](librarysongsortproperties.md)
  Song properties your app uses to sort results for a library request.
- [protocol LibraryTrackFilter](librarytrackfilter.md)
  Track properties your app uses as a filter for a library request.
- [protocol LibraryTrackSortProperties](librarytracksortproperties.md)
  Track properties your app uses to sort results for a library request.
- [protocol MusicCatalogChartRequestable](musiccatalogchartrequestable.md)
  A protocol for music items that your app can fetch by using a catalog charts request.
- [protocol MusicCatalogTopLevelResourceRequesting](musiccatalogtoplevelresourcerequesting.md)
  A protocol for music items that your app can fetch by using a catalog resource request without any filter.
- [protocol MusicLibraryAddable](musiclibraryaddable.md)
  A protocol for music items that your app can add to the music library.
- [protocol MusicLibraryRequestFilterValueEquatable](musiclibraryrequestfiltervalueequatable.md)
  A protocol for types of values your app can use with equality filters when fetching items using a music library request.
- [protocol MusicLibraryRequestFilterValueMembershipComparable](musiclibraryrequestfiltervaluemembershipcomparable.md)
  A protocol for types of values your app can use with membership filters when fetching items using a music library request.
- [protocol MusicLibraryRequestable](musiclibraryrequestable.md)
  A protocol for music items that your app can fetch by using a library request.
- [protocol MusicLibrarySearchable](musiclibrarysearchable.md)
  A protocol for music items that your app can fetch by using a library search request.
- [protocol MusicLibrarySectionRequestable](musiclibrarysectionrequestable.md)
  A protocol for types your app uses as sections when fetching items using a library sectioned request.
- [protocol MusicPersonalRecommendationItem](musicpersonalrecommendationitem.md)
  A protocol for music items that your app can fetch by using a personal recommendations request.
- [protocol MusicPlaylistAddable](musicplaylistaddable.md)
  A protocol for music items that your app can add to a playlist.
- [protocol MusicRecentlyPlayedRequestable](musicrecentlyplayedrequestable.md)
  A protocol for music items that your app can fetch by using a recently played request.
### Structures
- [struct MusicCatalogChart](musiccatalogchart.md)
  An object that contains popular items in the Apple Music catalog.
- [struct MusicCatalogChartsRequest](musiccatalogchartsrequest.md)
  A request that your app uses to fetch the most popular items in the Apple Music catalog.
- [struct MusicCatalogChartsResponse](musiccatalogchartsresponse.md)
  An object that contains results for a catalog charts request.
- [struct MusicCatalogSearchSuggestionsRequest](musiccatalogsearchsuggestionsrequest.md)
  A request that your app uses to fetch suggestions from the Apple Music catalog using a search term.
- [struct MusicCatalogSearchSuggestionsResponse](musiccatalogsearchsuggestionsresponse.md)
  An object that contains results for a catalog search suggestions request.
- [struct MusicLibraryRequest](musiclibraryrequest.md)
  A request that your app uses to fetch items from the user’s music library.
- [struct MusicLibraryResponse](musiclibraryresponse.md)
  An object that contains results for a library request.
- [struct MusicLibrarySearchRequest](musiclibrarysearchrequest.md)
  A request that your app uses to fetch items from user’s library using a search term.
- [struct MusicLibrarySearchResponse](musiclibrarysearchresponse.md)
  An object that contains results for a library search request.
- [struct MusicLibrarySection](musiclibrarysection.md)
  A section for a library sectioned response.
- [struct MusicLibrarySectionedRequest](musiclibrarysectionedrequest.md)
  A request that your app uses to fetch items grouped by sections from the user’s music library.
- [struct MusicLibrarySectionedResponse](musiclibrarysectionedresponse.md)
  An object that contains results for a library sectioned request.
- [struct MusicPersonalRecommendation](musicpersonalrecommendation.md)
  An object that contains recommended items based on the user’s library and listening history.
- [struct MusicPersonalRecommendationsRequest](musicpersonalrecommendationsrequest.md)
  A request that your app uses to fetch music recommendations based on the user’s library and listening history.
- [struct MusicPersonalRecommendationsResponse](musicpersonalrecommendationsresponse.md)
  An object that contains results for a personal recommendations request.
- [struct MusicRecentlyPlayedRequest](musicrecentlyplayedrequest.md)
  A request that your app uses to fetch items the user has recently played.
- [struct MusicRecentlyPlayedResponse](musicrecentlyplayedresponse.md)
  An object that contains items the user has recently played.
- [struct TitledSection](titledsection.md)
  A section you can use to request items from the library grouped by title.
### Type Aliases
- [typealias MusicRecentlyPlayedContainerRequest](musicrecentlyplayedcontainerrequest.md)
  A request that your app uses to fetch albums, playlists or stations that the user has recently played.
- [typealias MusicRecentlyPlayedContainerResponse](musicrecentlyplayedcontainerresponse.md)
  An object that contains albums, playlists or stations that the user has recently played.
### Enumerations
- [enum AudioVariant](audiovariant.md)
  Variants that indicate the quality of audio available for an item.
- [enum MusicCatalogChartKind](musiccatalogchartkind.md)
  The available kinds of catalog charts.
- [enum MusicPropertySource](musicpropertysource.md)
  An enumeration that specifies which source to use when requesting properties and relationships.
- [enum RecentlyPlayedMusicItem](recentlyplayedmusicitem.md)
  An item that represents an album, a playlist, or a station that the user has recently played.

## See Also

- [Media Player](../MediaPlayer/MediaPlayer.md)
  Find and play songs, audio podcasts, audio books, and more from within your app.
- [Apple Music API](../AppleMusicAPI/AppleMusicAPI.md)
  Integrate streaming music with catalog and personal content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/MusicKit)*