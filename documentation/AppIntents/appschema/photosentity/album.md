# album

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An entity schema for an album.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var album: some AppSchemaEntity { get }
```

## Discussion

To make your app’s content available to Apple Intelligence, conform your [`AppEntity`](../../appentity.md) to a schema that describes your content to the system. If your app’s functionality aligns with the `photos` domain and its content matches the `album` schema, you can generate the properties and protocol conformance the schema requires for your app entity implementation with the `@AppEntity(schema: .photos.album)` Swift macro. To make your app work with Siri, see [Apple Intelligence and Siri AI](../../apple-intelligence-and-siri-ai.md).

The following example shows an app entity that conforms to the `album` schema. You can create a type that conforms to the schema by adding the `@AppEntity` macro above the type’s declaration. Xcode inserts a template type into your code for you, which includes the macro, when you type the first few characters of `photos_album` and select it from the code-completion suggestions:

```swift
@AppEntity(schema: .photos.album)
struct PhotoAlbumEntity {
    // MARK: Default query

    /// The standard lookup the system runs to find one or more album entities, unless you provide another.
    static let defaultQuery = PhotoAlbumEntityQuery()

    // MARK: Entity properties

    /// The unique identifier for the album entity.
    let id: <#Identifiable.ID#>

    var name: String

    var creationDate: Date?

    var albumType: <#PhotoAlbumType#>

    /// The details the system shows to identify the album entity to a person, such as a title and image.
    var displayRepresentation: DisplayRepresentation {
        <#DisplayRepresentation#>
    }

    // MARK: Query type

    /// A type that looks up one or more album entities by their identifiers.
    struct PhotoAlbumEntityQuery: EntityQuery {
        func entities(for identifiers: [PhotoAlbumEntity.ID]) async throws -> [PhotoAlbumEntity] {
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
| `name` | `String` | Swift | Name |
| `creationDate` | `Date?` | Foundation | Date Created |
| `albumType` | `@AppEnum(schema: .photos.albumType)` | Your app | Type `PhotoAlbumType` is a placeholder name for a type that conforms to the [`albumType`](../photosenum/albumtype.md) enum schema, which your app defines and implements. |

## See Also

### Content and parameter types
- [var asset: some AppSchemaEntity](./asset.md)
  An entity schema for an asset.
- [var recognizedPerson: some AppSchemaEntity](./recognizedperson.md)
  An entity schema for a recognized person.
- [AppSchema.PhotosEntity](../photosentity.md)
  Identifies entity schemas in the photos domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/photosentity/album)*