# album

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An entity schema for an album.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var album: some AppSchemaEntity { get }
```

## Discussion

To make your app’s content available to Apple Intelligence, conform your [`AppEntity`](../../appentity.md) to a schema that describes your content to the system. If your app’s functionality aligns with the `audio` domain and its content matches the `album` schema, you can generate the properties and protocol conformance the schema requires for your app entity implementation with the `@AppEntity(schema: .audio.album)` Swift macro. To make your app work with Siri, see [Apple Intelligence and Siri AI](../../apple-intelligence-and-siri-ai.md).

The following example shows an app entity that conforms to the `album` schema. You can create a type that conforms to the schema by adding the `@AppEntity` macro above the type’s declaration. Xcode inserts a template type into your code for you, which includes the macro, when you type the first few characters of `audio_album` and select it from the code-completion suggestions:

```swift
@AppEntity(schema: .audio.album)
struct AlbumEntity {
    // MARK: Default query

    /// The standard lookup the system runs to find one or more album entities, unless you provide another.
    static let defaultQuery = AlbumEntityQuery()

    // MARK: Entity properties

    /// The unique identifier for the album entity.
    let id: <#Identifiable.ID#>

    var title: String

    var artistName: String

    var artists: [<#ArtistEntity#>]

    var universalProductCode: String?

    /// The details the system shows to identify the album entity to a person, such as a title and image.
    var displayRepresentation: DisplayRepresentation {
        <#DisplayRepresentation#>
    }

    // MARK: Query type

    /// A type that looks up one or more album entities by their identifiers.
    struct AlbumEntityQuery: EntityQuery {
        func entities(for identifiers: [AlbumEntity.ID]) async throws -> [AlbumEntity] {
            <#code#>
        }
    }
}
```

The schema supports the following system experiences:

- Siri
- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [Getting started with the App Intents framework](../../getting-started-with-the-app-intents-framework.md).

## Properties of the album entity

Each property in the code listing above describes a facet of the entity your app provides to the system. The following table describes what each property represents.

| Property | Type | Origin | Discussion |
| --- | --- | --- | --- |
| `title` | `String` | Swift | Title |
| `artistName` | `String` | Swift | Artist Name |
| `artists` | `[@AppEntity(schema: .audio.artist)]` | Your app | Artists `ArtistEntity` is a placeholder name for a type that conforms to the [`artist`](./artist.md) entity schema, which your app defines and implements. |
| `universalProductCode` | `String?` | Swift | Universal Product Code |

## See Also

### Content and parameter types
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
  An entity schema for news brief.
- [var newsProvider: some AppSchemaEntity](./newsprovider.md)
  An entity schema for news provider.
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
- [var song: some AppSchemaEntity](./song.md)
  An entity schema for a song.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/audioentity/album)*