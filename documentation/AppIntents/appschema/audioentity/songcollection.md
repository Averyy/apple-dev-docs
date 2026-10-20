# songCollection

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An entity schema for a song collection.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var songCollection: some AppSchemaEntity { get }
```

#### Discussion

To make your app’s content available to Apple Intelligence, conform your [`AppEntity`](../../appentity.md) to a schema that describes your content to the system. If your app’s functionality aligns with the `audio` domain and its content matches the `songCollection` schema, you can generate the properties and protocol conformance the schema requires for your app entity implementation with the `@AppEntity( .audio.songCollection)` Swift macro. To make your app work with Siri, see [Apple Intelligence and Siri AI](../../apple-intelligence-and-siri-ai.md).

The following example shows an app entity that conforms to the `songCollection` schema:

```swift
@AppEntity(schema: .audio.songCollection)
struct SongCollectionEntity {
    // MARK: Static

    static let defaultQuery = SongCollectionEntityQuery()

    // MARK: Properties

    let id: <#Identifiable.ID#>

    var title: String?

    var displayRepresentation: DisplayRepresentation {
        <#DisplayRepresentation#>
    }

    // MARK: Query

    struct SongCollectionEntityQuery: EntityQuery {
        func entities(for identifiers: [SongCollectionEntity.ID]) async throws -> [SongCollectionEntity] {
            <#code#>
        }
    }
}
```

The schema supports the following system experiences:

- Siri
- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [Getting started with the App Intents framework](../../getting-started-with-the-app-intents-framework.md).

## See Also

### Content and parameter types
- [var album: some AppSchemaEntity](./album.md)
  An entity schema for an album.
- [var algorithmicRadioStation: some AppSchemaEntity](./algorithmicradiostation.md)
  An entity schema for an algorithmic radio station.
- [var ambientSound: some AppSchemaEntity](./ambientsound.md)
  An entity schema for an ambient sound.
- [var artist: some AppSchemaEntity](./artist.md)
  An entity schema for an artist.
- [var audiobook: some AppSchemaEntity](./audiobook.md)
  An entity schema for an audiobook.
- [var classicalMusicRecording: some AppSchemaEntity](./classicalmusicrecording.md)
  An entity schema for a classical music recording.
- [var liveRadioStation: some AppSchemaEntity](./liveradiostation.md)
  An entity schema for a live radio station.
- [var newsBrief: some AppSchemaEntity](./newsbrief.md)
  An entity schema for  news brief.
- [var newsProvider: some AppSchemaEntity](./newsprovider.md)
  An entity schema for  news provider.
- [var playlist: some AppSchemaEntity](./playlist.md)
  An entity schema for a playlist.
- [var podcastCollection: some AppSchemaEntity](./podcastcollection.md)
  An entity schema for a podcast collection.
- [var podcastEpisode: some AppSchemaEntity](./podcastepisode.md)
  An entity schema for a podcast episode.
- [var podcastShow: some AppSchemaEntity](./podcastshow.md)
  An entity schema for a podcast show.
- [var radioShow: some AppSchemaEntity](./radioshow.md)
  An entity schema for a radio show.
- [var radioShowEpisode: some AppSchemaEntity](./radioshowepisode.md)
  An entity schema for a radio show episode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/audioentity/songcollection)*