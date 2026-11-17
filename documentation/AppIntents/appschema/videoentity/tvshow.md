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

To make your app’s content available to Apple Intelligence, conform your [`AppEntity`](../../appentity.md) to a schema that describes your content to the system. If your app’s functionality aligns with the `video` domain and its content matches the `tvShow` schema, you can generate the properties and protocol conformance the schema requires for your app entity implementation with the `@AppEntity(schema: .video.tvShow)` Swift macro. To make your app work with Siri, see [Apple Intelligence and Siri AI](../../apple-intelligence-and-siri-ai.md).

The following example shows an app entity that conforms to the `tvShow` schema. You can create a type that conforms to the schema by adding the `@AppEntity` macro above the type’s declaration. Xcode inserts a template type into your code for you, which includes the macro, when you type the first few characters of `video_tvShow` and select it from the code-completion suggestions:

```swift
@AppEntity(schema: .video.tvShow)
struct TVShowEntity {
    // MARK: Default query

    /// The standard lookup the system runs to find one or more tv show entities, unless you provide another.
    static let defaultQuery = TVShowEntityQuery()

    // MARK: Entity properties

    /// The unique identifier for the tv show entity.
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

    /// The details the system shows to identify the tv show entity to a person, such as a title and image.
    var displayRepresentation: DisplayRepresentation {
        <#DisplayRepresentation#>
    }

    // MARK: Query type

    /// A type that looks up one or more tv show entities by their identifiers.
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

## Properties of the tv-show entity

Each property in the code listing above describes a facet of the entity your app provides to the system. The following table describes what each property represents.

| Property | Type | Origin | Discussion |
| --- | --- | --- | --- |
| `title` | `String` | Swift | Title |
| `description` | `String?` | Swift | Description |
| `genres` | `[String]` | Swift | Genres |
| `premiereDate` | `Date?` | Foundation | Premiere Date |
| `finaleDate` | `Date?` | Foundation | Finale Date |
| `castAndCrew` | `[@AppEntity(schema: .video.person)]` | Your app | Cast and Crew `VideoPerson` is a placeholder name for a type that conforms to the [`person`](./person.md) entity schema, which your app defines and implements. |
| `images` | `[@AppEntity(schema: .video.image)]` | Your app | Images `VideoImage` is a placeholder name for a type that conforms to the [`image`](./image.md) entity schema, which your app defines and implements. |
| `trailers` | `[URL]` | Foundation | Trailers |
| `seasonCount` | `Int?` | Swift | Season Count |

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