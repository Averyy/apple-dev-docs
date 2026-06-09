# album

**Framework**: App Intents  
**Kind**: property

An entity schema for an album.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
var album: some AppSchemaEntity { get }
```

#### Discussion

To make your app’s content available to Apple Intelligence, conform your [`AppEntity`](appentity.md) to a schema that describes your content to the system. If your app’s functionality aligns with the `photos` domain and its content matches the `album` schema, you can generate the properties and protocol conformance the schema requires for your app entity implementation with the `@AppEntity( .photos.album)` Swift macro. To make your app work with Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

The following example shows an app entity that conforms to the `album` schema:

```swift
@AppEntity(schema: .photos.album)
struct PhotoAlbumEntity {
    // MARK: Static

    static let defaultQuery = PhotoAlbumEntityQuery()

    // MARK: Properties

    let id: <#Identifiable.ID#>

    var name: String
    var creationDate: Date?
    var albumType: <#PhotoAlbumType#>

    var displayRepresentation: DisplayRepresentation {
        <#DisplayRepresentation#>
    }

    // MARK: Query

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

For more information about the App Intents framework and the experiences it supports, see [`Getting started with the App Intents framework`](getting-started-with-the-app-intents-framework.md).

## See Also

- [var asset: some AppSchemaEntity](appschema/photosentity/asset.md)
  An entity schema for an asset.
- [var recognizedPerson: some AppSchemaEntity](appschema/photosentity/recognizedperson.md)
  An entity schema for a recognized person.
- [AppSchema.PhotosEntity](appschema/photosentity.md)
  Identifies entity schemas in the photos domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/photosentity/album)*