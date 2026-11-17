# asset

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An entity schema for an asset.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var asset: some AppSchemaEntity { get }
```

## Discussion

To make your app’s content available to Apple Intelligence, conform your [`AppEntity`](../../appentity.md) to a schema that describes your content to the system. If your app’s functionality aligns with the `photos` domain and its content matches the `asset` schema, you can generate the properties and protocol conformance the schema requires for your app entity implementation with the `@AppEntity(schema: .photos.asset)` Swift macro. To make your app work with Siri, see [Apple Intelligence and Siri AI](../../apple-intelligence-and-siri-ai.md).

The following example shows an app entity that conforms to the `asset` schema. You can create a type that conforms to the schema by adding the `@AppEntity` macro above the type’s declaration. Xcode inserts a template type into your code for you, which includes the macro, when you type the first few characters of `photos_asset` and select it from the code-completion suggestions:

```swift
@AppEntity(schema: .photos.asset)
struct PhotoEntity {
    // MARK: Default query

    /// The standard lookup the system runs to find one or more photo entities, unless you provide another.
    static let defaultQuery = PhotoEntityQuery()

    // MARK: Entity properties

    /// The unique identifier for the photo entity.
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

    /// The details the system shows to identify the photo entity to a person, such as a title and image.
    var displayRepresentation: DisplayRepresentation {
        <#DisplayRepresentation#>
    }

    // MARK: Query type

    /// A type that looks up one or more photo entities by their identifiers.
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

For more information about the App Intents framework and the experiences it supports, see [Getting started with the App Intents framework](../../getting-started-with-the-app-intents-framework.md).

## Properties of the asset entity

Each property in the code listing above describes a facet of the entity your app provides to the system. The following table describes what each property represents.

| Property | Type | Origin | Discussion |
| --- | --- | --- | --- |
| `creationDate` | `Date?` | Foundation | Date Created |
| `location` | `GeoToolbox.PlaceDescriptor?` | GeoToolbox | Location |
| `assetType` | `@AppEnum(schema: .photos.assetType)?` | Your app | Photo Type `PhotoAssetType` is a placeholder name for a type that conforms to the [`assetType`](../photosenum/assettype.md) enum schema, which your app defines and implements. |
| `isFavorite` | `Bool` | Swift | Favorite |
| `isHidden` | `Bool` | Swift | Hidden |
| `hasSuggestedEdits` | `Bool` | Swift | Suggested Edits |
| `aperture` | `Double?` | Swift | Aperture |
| `exposure` | `Double?` | Swift | Exposure |
| `saturation` | `Double?` | Swift | Saturation |
| `warmth` | `Double?` | Swift | Warmth |
| `filter` | `@AppEnum(schema: .photos.filterType)?` | Your app | Filter `PhotoFilterEffectType` is a placeholder name for a type that conforms to the [`filterType`](../photosenum/filtertype.md) enum schema, which your app defines and implements. |
| `isPortraitModeEnabled` | `Bool?` | Swift | Portrait Mode Enablement |

## See Also

### Content and parameter types
- [var album: some AppSchemaEntity](./album.md)
  An entity schema for an album.
- [var recognizedPerson: some AppSchemaEntity](./recognizedperson.md)
  An entity schema for a recognized person.
- [AppSchema.PhotosEntity](../photosentity.md)
  Identifies entity schemas in the photos domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/photosentity/asset)*