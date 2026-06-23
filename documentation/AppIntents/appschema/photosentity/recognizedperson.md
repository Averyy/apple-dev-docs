# recognizedPerson

**Framework**: App Intents  
**Kind**: property

An entity schema for a recognized person.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var recognizedPerson: some AppSchemaEntity { get }
```

#### Discussion

To make your app’s content available to Apple Intelligence, conform your [`AppEntity`](appentity.md) to a schema that describes your content to the system. If your app’s functionality aligns with the `photos` domain and its content matches the `recognizedPerson` schema, you can generate the properties and protocol conformance the schema requires for your app entity implementation with the `@AppEntity( .photos.recognizedPerson)` Swift macro. To make your app work with Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

The following example shows an app entity that conforms to the `recognizedPerson` schema:

```swift
@AppEntity(schema: .photos.recognizedPerson)
struct PhotoPersonEntity {
    // MARK: Static

    static let defaultQuery = PhotoPersonEntityQuery()

    // MARK: Properties

    let id: <#Identifiable.ID#>

    var name: String
    var isFavorite: Bool

    var displayRepresentation: DisplayRepresentation {
        <#DisplayRepresentation#>
    }

    // MARK: Query

    struct PhotoPersonEntityQuery: EntityQuery {
        func entities(for identifiers: [PhotoPersonEntity.ID]) async throws -> [PhotoPersonEntity] {
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

- [var album: some AppSchemaEntity](appschema/photosentity/album.md)
  An entity schema for an album.
- [var asset: some AppSchemaEntity](appschema/photosentity/asset.md)
  An entity schema for an asset.
- [AppSchema.PhotosEntity](appschema/photosentity.md)
  Identifies entity schemas in the photos domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/photosentity/recognizedperson)*