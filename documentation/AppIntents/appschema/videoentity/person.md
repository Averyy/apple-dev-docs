# person

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An entity schema for a person.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- tvOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
var person: some AppSchemaEntity { get }
```

## Discussion

To make your app’s content available to Apple Intelligence, conform your [`AppEntity`](../../appentity.md) to a schema that describes your content to the system. If your app’s functionality aligns with the `video` domain and its content matches the `person` schema, you can generate the properties and protocol conformance the schema requires for your app entity implementation with the `@AppEntity(schema: .video.person)` Swift macro. To make your app work with Siri, see [Apple Intelligence and Siri AI](../../apple-intelligence-and-siri-ai.md).

The following example shows an app entity that conforms to the `person` schema. You can create a type that conforms to the schema by adding the `@AppEntity` macro above the type’s declaration. Xcode inserts a template type into your code for you, which includes the macro, when you type the first few characters of `video_person` and select it from the code-completion suggestions:

```swift
@AppEntity(schema: .video.person)
struct VideoPerson {
    // MARK: Default query

    /// The standard lookup the system runs to find one or more video person entities, unless you provide another.
    static let defaultQuery = VideoPersonQuery()

    // MARK: Entity properties

    /// The unique identifier for the video person entity.
    let id: <#Identifiable.ID#>

    var name: String

    var roles: [<#VideoPersonRole#>]

    var image: <#VideoImage#>?

    var url: URL?

    var description: String?

    var characterNames: [String]

    /// The details the system shows to identify the video person entity to a person, such as a title and image.
    var displayRepresentation: DisplayRepresentation {
        <#DisplayRepresentation#>
    }

    // MARK: Query type

    /// A type that looks up one or more video person entities by their identifiers.
    struct VideoPersonQuery: EntityQuery {
        func entities(for identifiers: [VideoPerson.ID]) async throws -> [VideoPerson] {
            <#code#>
        }
    }
}
```

The schema supports the following system experiences:

- Siri
- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [Getting started with the App Intents framework](../../getting-started-with-the-app-intents-framework.md).

## Properties of the person entity

Each property in the code listing above describes a facet of the entity your app provides to the system. The following table describes what each property represents.

| Property | Type | Origin | Discussion |
| --- | --- | --- | --- |
| `name` | `String` | Swift | Name |
| `roles` | `[@AppEnum(schema: .video.personRole)]` | Your app | Roles `VideoPersonRole` is a placeholder name for a type that conforms to the [`personRole`](../videoenum/personrole.md) enum schema, which your app defines and implements. |
| `image` | `@AppEntity(schema: .video.image)?` | Your app | Image `VideoImage` is a placeholder name for a type that conforms to the [`image`](./image.md) entity schema, which your app defines and implements. |
| `url` | `URL?` | Foundation | URL |
| `description` | `String?` | Swift | Description |
| `characterNames` | `[String]` | Swift | Character Names |

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
- [var tvEpisode: some AppSchemaEntity](./tvepisode.md)
  An entity schema for a tv episode.
- [var tvSeason: some AppSchemaEntity](./tvseason.md)
  An entity schema for a tv season.
- [var tvShow: some AppSchemaEntity](./tvshow.md)
  An entity schema for a tv show.
- [AppSchema.VideoEntity](../videoentity.md)
  Identifies entity schemas in the video domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/videoentity/person)*