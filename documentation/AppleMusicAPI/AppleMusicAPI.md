# Apple Music API

**Framework**: Apple Music API  
**Kind**: module

Integrate streaming music with catalog and personal content.

**Availability**:
- Apple Music 1.0+

#### Overview

Use Apple Music API to access information about media in the Apple Music Catalog and a user’s personal iCloud Music Library.

- Apple Music Catalog includes all resources available in Apple Music.
- iCloud Music Library contains only those resources the user adds to their personal library. For example, it contains items from Apple Music, songs purchased from iTunes Store, and imports from discs and other apps. This library can include content that’s not in the Apple Music Catalog.

Use this API to retrieve information about albums, songs, artists, playlists, music videos, Apple Music stations, ratings, charts, recommendations, and the user’s most-recently played content. With proper authorization from the user, you can also create or modify playlists and apply ratings to the user’s content.

> **Note**:  Use the [`Apple Music Feed`](https://developer.apple.com/documentation/AppleMusicFeed) to access the Apple Music Catalog in bulk.

## Topics

### Essentials
- [Generating Developer Tokens](generating-developer-tokens.md)
  Generate a developer token needed to make requests to Apple Music API.
- [User Authentication for MusicKit](user-authentication-for-musickit.md)
  Authenticate requests for user data using the Music User Token.
- [Handling Requests and Responses](handling-requests-and-responses.md)
  Write a request and handle responses from the API.
- [Handling Resource Representation and Relationships](handling-resource-representation-and-relationships.md)
  Fetch resources with extended attributes and included relationships and relationship views.
- [Storefronts and Localization](storefronts-and-localization.md)
  Pick a region-specific geographic location from which to retrieve catalog information, or retrieve information from the user’s personal library.
- [Common Objects](common-objects.md)
  Understand the common JSON objects that framework responses contain.
- [Managing Content Ratings, Alternate Versions, and Equivalencies](managing-content-ratings-alternate-versions-and-equivalencies.md)
  Handle multiple and alternate versions of content.
- [Fetching Resources by Page](fetching-resources-by-page.md)
  Use pagination to fetch the next set of objects.
### Albums, Artists, Songs, and Videos
- [Albums](albums-api.md)
  Get an album’s name, artist, list of tracks, artwork, release date, and recording information, and add new albums to the user’s library.
- [Artists](artists-api.md)
  Get information about an artist, including the content they created and references to them in playlists and radio stations.
- [Songs](songs-api.md)
  Get information about a particular song, including the artist who created it and the album on which it appeared.
- [Music Videos](music-videos-api.md)
  Get information about a music video, including the artist who created it and the associated album, and add new videos to the user’s library.
### Playlists and Stations
- [Playlists](playlists-api.md)
  Get the contents of playlists, add new playlists to the user’s library, and add tracks to an existing playlist.
- [Apple Music Stations](apple-music-stations.md)
  Get information about streaming content offered by Apple Music.
### Search
- [Search](search.md)
  Search for albums, songs, artists, and other information in the user’s personal library or the Apple Music Catalog.
### Ratings, Genres, and Charts
- [Ratings](ratings-api.md)
  Get and set ratings for albums, songs, playlists, music videos, and stations.
- [Music Genres](music-genres.md)
  Get information about the genres of the user’s music or items in the Apple Music Catalog.
- [Charts](charts-api.md)
  Get chart information that shows the popularity of albums, songs, and music videos.
### Activities, Curators, and Record Labels
- [Activities](activities-api.md)
  Get request and response activities associated with the Apple Music Catalog.
- [Curators](curators-api.md)
  Get information about the person who curated a playlist or station.
- [Record Labels](record-labels-api.md)
  Get information on record labels in the Apple Music Catalog.
### Adding a resource to favorites
- [Add resource to favorites](add-resource-to-favorites.md)
  Add the user’s resource to favorites.
### Getting a user’s replay data
- [Get the user's replay data](get-the-user's-replay-data.md)
  Fetch the user’s replay data for the latest eligible year.
### Recommendations and history
- [Recommendations](recommendations.md)
  Get music recommendations based on the user’s library and purchase history.
- [History](history.md)
  Get historical information about the songs and stations the user played recently.
### Fetching Multiple Resource Types
- [Get Multiple Catalog Resources Using Resource-Typed ID Parameters](get-multiple-catalog-resources-by-resource-typed-ids-parameters.md)
  Fetch one or more catalog resources by using their identifiers.
- [Get Multiple Library Resources Using Resource-Typed ID Parameters](get-multiple-library-resources-by-resource-typed-ids-parameters.md)
  Fetch one or more library resources by using their identifiers.
### Endpoints
- [Placeholder Endpoint to Test Connectivity](dummy-endpoint-to-test-connectivity.md)
- [Get a User's Storefront](get-a-user's-storefront.md)
  Fetch a storefront for a specific user.
### Dictionaries
- [object AlbumPeriodSummaries](albumperiodsummaries.md)
  The album for the period summary.
- [object ArtistPeriodSummaries](artistperiodsummaries.md)
  The artist for the period summary.
- [object Artwork](artwork.md)
  An object that represents artwork.
- [object DescriptionAttribute](descriptionattribute.md)
  An object that represents a description attribute.
- [object EditorialNotes](editorialnotes.md)
  An object that represents a notes attribute.
- [object LangageTagResponse](langagetagresponse.md)
  The response to a language tag request.
- [object MusicSummaries](musicsummaries.md)
  The music for the period summary.
- [object MusicSummariesResponse](musicsummariesresponse.md)
- [object PaginatedResourceCollectionResponse](paginatedresourcecollectionresponse.md)
  A response object composed of paginated resource objects for the request.
- [object PlayParameters](playparameters.md)
  An object that represents play parameters for resources.
- [object Preview](preview.md)
  An object that represents a preview for resources.
- [object RelationshipResponse](relationshipresponse.md)
  The response for a direct resource relationship fetch.
- [object RelationshipViewResponse](relationshipviewresponse.md)
  The response for a direct resource view fetch.
- [object SongPeriodSummaries](songperiodsummaries.md)
  The song for the period summary.
- [object StorefrontsResponse](storefrontsresponse.md)
  The response to a storefront request.
- [object View](view.md)
  A to-one or to-many relationship view from one resource object to others representing interesting associations.

## See Also

- [Media Player](../MediaPlayer/MediaPlayer.md)
  Find and play songs, audio podcasts, audio books, and more from within your app.
- [StoreKit](../StoreKit/StoreKit.md)
  Support In-App Purchases and interactions with the App Store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AppleMusicAPI)*