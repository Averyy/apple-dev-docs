# radioShow

**Framework**: App Intents  
**Kind**: property

An entity schema for a radio show.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var radioShow: some AppSchemaEntity { get }
```

#### Discussion

To make your app’s content available to Apple Intelligence, conform your [`AppEntity`](appentity.md) to a schema that describes your content to the system. If your app’s functionality aligns with the `audio` domain and its content matches the `radioShow` schema, you can generate the properties and protocol conformance the schema requires for your app entity implementation with the `@AppEntity( .audio.radioShow)` Swift macro. To make your app work with Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

The following example shows an app entity that conforms to the `radioShow` schema:

```swift
@AppEntity(schema: .audio.radioShow)
struct RadioShowEntity {
    // MARK: Static

    static let defaultQuery = RadioShowEntityQuery()

    // MARK: Properties

    let id: <#Identifiable.ID#>

    var title: String

    var displayRepresentation: DisplayRepresentation {
        <#DisplayRepresentation#>
    }

    // MARK: Query

    struct RadioShowEntityQuery: EntityQuery {
        func entities(for identifiers: [RadioShowEntity.ID]) async throws -> [RadioShowEntity] {
            <#code#>
        }
    }
}
```

The schema supports the following system experiences:

- Siri
- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [`Getting started with the App Intents framework`](getting-started-with-the-app-intents-framework.md).

## See Also

- [var album: some AppSchemaEntity](appschema/audioentity/album.md)
  An entity schema for an album.
- [var algorithmicRadioStation: some AppSchemaEntity](appschema/audioentity/algorithmicradiostation.md)
  An entity schema for an algorithmic radio station.
- [var ambientSound: some AppSchemaEntity](appschema/audioentity/ambientsound.md)
  An entity schema for an ambient sound.
- [var artist: some AppSchemaEntity](appschema/audioentity/artist.md)
  An entity schema for an artist.
- [var audiobook: some AppSchemaEntity](appschema/audioentity/audiobook.md)
  An entity schema for an audiobook.
- [var classicalMusicRecording: some AppSchemaEntity](appschema/audioentity/classicalmusicrecording.md)
  An entity schema for a classical music recording.
- [var liveRadioStation: some AppSchemaEntity](appschema/audioentity/liveradiostation.md)
  An entity schema for a live radio station.
- [var newsBrief: some AppSchemaEntity](appschema/audioentity/newsbrief.md)
  An entity schema for  news brief.
- [var newsProvider: some AppSchemaEntity](appschema/audioentity/newsprovider.md)
  An entity schema for  news provider.
- [var playlist: some AppSchemaEntity](appschema/audioentity/playlist.md)
  An entity schema for a playlist.
- [var podcastCollection: some AppSchemaEntity](appschema/audioentity/podcastcollection.md)
  An entity schema for a podcast collection.
- [var podcastEpisode: some AppSchemaEntity](appschema/audioentity/podcastepisode.md)
  An entity schema for a podcast episode.
- [var podcastShow: some AppSchemaEntity](appschema/audioentity/podcastshow.md)
  An entity schema for a podcast show.
- [var radioShowEpisode: some AppSchemaEntity](appschema/audioentity/radioshowepisode.md)
  An entity schema for a radio show episode.
- [var song: some AppSchemaEntity](appschema/audioentity/song.md)
  An entity schema for a song.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/audioentity/radioshow)*