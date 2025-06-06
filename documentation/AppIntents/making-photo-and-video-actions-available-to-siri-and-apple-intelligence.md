# Making photo and video actions available to Siri and Apple Intelligence

**Framework**: Appintents

Create app intents and entities to integrate your app’s photo and video functionality with Siri and Apple Intelligence.

#### Overview

To integrate your app’s photo and video capabilities with Siri and Apple Intelligence, you use Swift macros that generate additional properties and add protocol conformance for your app intent, app entity, and app enumeration implementation that Apple Intelligence needs.

> **Note**: Siri’s personal context understanding, onscreen awareness, and in-app actions are in development and will be available with a future software update.

For example, if your app allows someone to open a photo, use the [`AssistantIntent(schema:)`](assistantintent(schema:).md) macro and provide the assistant schema that consists of the `.photos` domain and the [`openAsset`](assistantschemas/photosintent/openasset.md) schema:

```swift
@AssistantIntent(schema: .photos.openAsset)
struct OpenAssetIntent: OpenIntent {
    var target: AssetEntity

    @Dependency
    var library: MediaLibrary

    @Dependency
    var navigation: NavigationManager

    @MainActor
    func perform() async throws -> some IntentResult {
        let assets = library.assets(for: [target.id])
        guard let asset = assets.first else {
            throw IntentError.noEntity
        }

        navigation.openAsset(asset)
        return .result()
    }
}
```

To learn more about assistant schemas, see [`Integrating actions with Siri and Apple Intelligence`](integrating-actions-with-siri-and-apple-intelligence.md). For a list of available app intents in the `.photos` domain, see [`AssistantSchemas.PhotosIntent`](assistantschemas/photosintent.md).

##### Ensure Your Entity Meets Requirements

If you use app entities to describe custom data types, annotate the app entity implementation with the [`AssistantEntity(schema:)`](assistantentity(schema:).md) macro. This makes sure Siri and Apple Intelligence can understand your data. For example, the intent in the previous section uses `AssetEntity`. The following code snippet shows how the `AssetEntity` implementation uses the [`AssistantEntity(schema:)`](assistantentity(schema:).md) macro:

```swift
@AssistantEntity(schema: .photos.asset)
struct AssetEntity: IndexedEntity {

    static let defaultQuery = AssetQuery()

    let id: String
    let asset: Asset

    @Property()
    var title: String?

    var creationDate: Date?
    var location: CLPlacemark?
    var assetType: AssetType?
    var isFavorite: Bool
    var isHidden: Bool
    var hasSuggestedEdits: Bool

    var displayRepresentation: DisplayRepresentation {
        DisplayRepresentation(
            title: title.map { "\($0)" } ?? "Unknown",
            subtitle: assetType?.localizedStringResource ?? "Photo"
        )
    }
}
```

The assistant schema for the `AssetEntity` consists of the `.photos` domain and the [`asset`](assistantschemas/photosentity/asset.md) schema.

For a list of available app entity schemas in the `.photos` domain, see [`AssistantSchemas.PhotosEntity`](assistantschemas/photosentity.md).

##### Ensure Your Enumeration Meets Requirements

To make sure Siri and Apple Intelligence understand custom static types for your intent parameters, annotate app enumerations with the [`AssistantEnum(schema:)`](assistantenum(schema:).md) macro. Then, pass the `.photos` domain and a schema to it. The following example uses the [`assetType`](assistantschemas/photosenum/assettype.md) schema:

```swift
@AssistantEnum(schema: .photos.assetType)
enum AssetType: String, AppEnum {
    case photo
    case video

    static let caseDisplayRepresentations: [AssetType: DisplayRepresentation] = [
        .photo: "Photo",
        .video: "Video"
    ]
}
```

For a list of available app enumeration schemas in the `.photos` domain, see [`AssistantSchemas.PhotosEnum`](assistantschemas/photosenum.md).

## See Also

- [AssistantSchemas.PhotosIntent](assistantschemas/photosintent.md)
  Assistant schema conformance for app intents that offer photo and video functionality.
- [AssistantSchemas.PhotosEntity](assistantschemas/photosentity.md)
  Assistant schema conformance for app entities that describe media assets.
- [AssistantSchemas.PhotosEnum](assistantschemas/photosenum.md)
  Assistant schema conformance for types you use to describe photos and videos.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AppIntents/making-photo-and-video-actions-available-to-siri-and-apple-intelligence)*