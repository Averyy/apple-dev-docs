# asset

**Framework**: App Intents  
**Kind**: property

An entity schema for an asset.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var asset: some AppSchemaEntity { get }
```

#### Discussion

To make your app’s content available to Apple Intelligence, conform your [`AppEntity`](appentity.md) to a schema that describes your content to the system. If your app’s functionality aligns with the `photos` domain and its content matches the `asset` schema, you can generate the properties and protocol conformance the schema requires for your app entity implementation with the `@AppEntity( .photos.asset)` Swift macro. To make your app work with Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

The following example shows an app entity that conforms to the `asset` schema:

```swift
@AppEntity(schema: .photos.asset)
struct PhotoEntity {
    // MARK: Static

    static let defaultQuery = PhotoEntityQuery()

    // MARK: Properties

    let id: <#Identifiable.ID#>

    var creationDate: Date?
    var location: GeoToolbox.PlaceDescriptor?
    var assetType: <#PhotoAssetType#>?
    var isFavorite: Bool
    var isHidden: Bool
    var hasSuggestedEdits: Bool
    var aperture: Double?
    var exposure: Double?
    var saturation: Double?
    var warmth: Double?
    var filter: <#PhotoFilterEffectType#>?
    var isPortraitModeEnabled: Bool?

    var displayRepresentation: DisplayRepresentation {
        <#DisplayRepresentation#>
    }

    // MARK: Query

    struct PhotoEntityQuery: EntityQuery {
        func entities(for identifiers: [PhotoEntity.ID]) async throws -> [PhotoEntity] {
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
- [var recognizedPerson: some AppSchemaEntity](appschema/photosentity/recognizedperson.md)
  An entity schema for a recognized person.
- [AppSchema.PhotosEntity](appschema/photosentity.md)
  Identifies entity schemas in the photos domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/photosentity/asset)*