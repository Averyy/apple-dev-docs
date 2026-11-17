# freeformVideo

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An entity schema for a freeform video.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- tvOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
var freeformVideo: some AppSchemaEntity { get }
```

## Discussion

To make your app’s content available to Apple Intelligence, conform your [`AppEntity`](../../appentity.md) to a schema that describes your content to the system. If your app’s functionality aligns with the `video` domain and its content matches the `freeformVideo` schema, you can generate the properties and protocol conformance the schema requires for your app entity implementation with the `@AppEntity(schema: .video.freeformVideo)` Swift macro. To make your app work with Siri, see [Apple Intelligence and Siri AI](../../apple-intelligence-and-siri-ai.md).

The following example shows an app entity that conforms to the `freeformVideo` schema. You can create a type that conforms to the schema by adding the `@AppEntity` macro above the type’s declaration. Xcode inserts a template type into your code for you, which includes the macro, when you type the first few characters of `video_freeformVideo` and select it from the code-completion suggestions:

```swift
@AppEntity(schema: .video.freeformVideo)
struct FreeformVideoEntity {
    // MARK: Default query

    /// The standard lookup the system runs to find one or more freeform video entities, unless you provide another.
    static let defaultQuery = FreeformVideoEntityQuery()

    // MARK: Entity properties

    /// The unique identifier for the freeform video entity.
    let id: <#Identifiable.ID#>

    var title: String

    var creator: <#VideoContentCreator#>?

    var images: [<#VideoImage#>]

    var url: URL?

    var collaborators: [<#VideoContentCreator#>]

    var tags: [String]

    var description: String?

    var contentType: <#VideoContentType#>

    var viewCount: Int?

    var releaseDate: Date?

    var duration: Duration?

    var isExplicitContent: Bool

    /// The details the system shows to identify the freeform video entity to a person, such as a title and image.
    var displayRepresentation: DisplayRepresentation {
        <#DisplayRepresentation#>
    }

    // MARK: Query type

    /// A type that looks up one or more freeform video entities by their identifiers.
    struct FreeformVideoEntityQuery: EntityQuery {
        func entities(for identifiers: [FreeformVideoEntity.ID]) async throws -> [FreeformVideoEntity] {
            <#code#>
        }
    }
}
```

The schema supports the following system experiences:

- Siri
- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [Getting started with the App Intents framework](../../getting-started-with-the-app-intents-framework.md).

## Properties of the freeform-video entity

Each property in the code listing above describes a facet of the entity your app provides to the system. The following table describes what each property represents.

| Property | Type | Origin | Discussion |
| --- | --- | --- | --- |
| `title` | `String` | Swift | Title |
| `creator` | `@AppEntity(schema: .video.contentCreator)?` | Your app | Creator `VideoContentCreator` is a placeholder name for a type that conforms to the [`contentCreator`](./contentcreator.md) entity schema, which your app defines and implements. |
| `images` | `[@AppEntity(schema: .video.image)]` | Your app | Images `VideoImage` is a placeholder name for a type that conforms to the [`image`](./image.md) entity schema, which your app defines and implements. |
| `url` | `URL?` | Foundation | URL |
| `collaborators` | `[@AppEntity(schema: .video.contentCreator)]` | Your app | Collaborators `VideoContentCreator` is a placeholder name for a type that conforms to the [`contentCreator`](./contentcreator.md) entity schema, which your app defines and implements. |
| `tags` | `[String]` | Swift | Tags |
| `description` | `String?` | Swift | Description |
| `contentType` | `@AppEnum(schema: .video.videoContentType)` | Your app | Video Content Type `VideoContentType` is a placeholder name for a type that conforms to the [`videoContentType`](../videoenum/videocontenttype.md) enum schema, which your app defines and implements. |
| `viewCount` | `Int?` | Swift | View Count |
| `releaseDate` | `Date?` | Foundation | Release Date |
| `duration` | `Duration?` | Swift | Duration |
| `isExplicitContent` | `Bool` | Swift | Is Explicit Content |

## See Also

### Content and parameter types
- [var contentCreator: some AppSchemaEntity](./contentcreator.md)
  An entity schema for a content creator.
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
- [var tvShow: some AppSchemaEntity](./tvshow.md)
  An entity schema for a tv show.
- [AppSchema.VideoEntity](../videoentity.md)
  Identifies entity schemas in the video domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/videoentity/freeformvideo)*