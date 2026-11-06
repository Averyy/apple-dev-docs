# tvShow

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An entity schema for a tv show.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- tvOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
var tvShow: some AppSchemaEntity { get }
```

## Discussion

To make your app’s content available to Apple Intelligence, conform your [`AppEntity`](../../appentity.md) to a schema that describes your content to the system. If your app’s functionality aligns with the `video` domain and its content matches the `tvShow` schema, you can generate the properties and protocol conformance the schema requires for your app entity implementation with the `@AppEntity( .video.tvShow)` Swift macro. To make your app work with Siri, see [Apple Intelligence and Siri AI](../../apple-intelligence-and-siri-ai.md).

The following example shows an app entity that conforms to the `tvShow` schema:

```swift
@AppEntity(schema: .video.tvShow)
struct TVShowEntity {
    // MARK: Static

    static let defaultQuery = TVShowEntityQuery()

    // MARK: Properties

    let id: <#Identifiable.ID#>

    var title: String
    var description: String?
    var genres: [String]
    var premiereDate: Date?
    var finaleDate: Date?
    var castAndCrew: [<#VideoPerson#>]
    var images: [<#VideoImage#>]
    var trailers: [URL]
    var seasonCount: Int?
    var contentRatingValue: String?

    var displayRepresentation: DisplayRepresentation {
        <#DisplayRepresentation#>
    }

    // MARK: Query

    struct TVShowEntityQuery: EntityQuery {
        func entities(for identifiers: [TVShowEntity.ID]) async throws -> [TVShowEntity] {
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
- [var contentCreator: some AppSchemaEntity](./contentcreator.md)
  An entity schema for a content creator.
- [var freeformVideo: some AppSchemaEntity](./freeformvideo.md)
  An entity schema for a freeform video.
- [var image: some AppSchemaEntity](./image.md)
  An entity schema for an image.
- [var movie: some AppSchemaEntity](./movie.md)
  An entity schema for a movie.
- [var person: some AppSchemaEntity](./person.md)
  An entity schema for a person.
- [var tvEpisode: some AppSchemaEntity](./tvepisode.md)
  An entity schema for a tv episode.
- [var tvSeason: some AppSchemaEntity](./tvseason.md)
  An entity schema for a tv season.
- [AppSchema.VideoEntity](../videoentity.md)
  Identifies entity schemas in the video domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/videoentity/tvshow)*