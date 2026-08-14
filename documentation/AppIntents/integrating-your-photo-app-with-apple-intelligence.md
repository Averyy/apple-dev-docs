# Integrating your photo app with Apple Intelligence

**Framework**: App Intents

Adopt photo schemas so people can edit and manage photos with Siri.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- Xcode 27.0+ (Beta)

#### Overview

This sample app uses the App Intents framework to make its photo functionality discoverable by Apple Intelligence and Siri. After choosing photos from their camera roll, people use Siri to perform actions like rotating a photo, adding it to their Favorites, and more.

#### Make Content Available in Spotlight

To make its content discoverable by Apple Intelligence and let people find photos using semantic search in Spotlight, the sample app describes its assets as app entities that conform to the [`IndexedEntity`](indexedentity.md) protocol:

```swift
@AppEntity(schema: .photos.asset)
struct AssetEntity: IndexedEntity {

    // MARK: Static

    static let defaultQuery = AssetQuery()

    // MARK: Properties

    let id: String
    let asset: Asset

    @Property(title: "Title")
    var title: String?

    var creationDate: Date?
    var location: PlaceDescriptor?
    var assetType: AssetType?
    var isFavorite: Bool
    var isHidden: Bool
    var hasSuggestedEdits: Bool
    var aperture: Double?
    var exposure: Double?
    var saturation: Double?
    var warmth: Double?
    var filter: AssetFilter?
    var isPortraitModeEnabled: Bool?

    var displayRepresentation: DisplayRepresentation {
        DisplayRepresentation(
            title: title.map { "\($0)" } ?? "Unknown",
            subtitle: assetType?.localizedStringResource ?? "Photo"
        )
    }
}
```

By conforming app entities to `IndexedEntity` and donating them to a Spotlight index, the sample app enables people to search for its content in Spotlight and enable semantic search results.

For more information about making content available to Spotlight, see [`Making app entities available in Spotlight`](making-app-entities-available-in-spotlight.md).

#### Make App Entities Shareable

Describing app data as app entities and indexing them in Spotlight is the first step toward making your app discoverable by Apple Intelligence and bringing your app to Siri. To make sure the system can pass the sample app’s content to other apps, the app adopts the [`Transferable`](https://developer.apple.com/documentation/coretransferable/transferable) protocol for its app entities:

```swift
extension AssetEntity: Transferable {
    // ...

    static var transferRepresentation: some TransferRepresentation {
        DataRepresentation(exportedContentType: .png) { entity in
            try await entity.asset.pngData()
        }
    }
}
```

#### Provide Onscreen Context

When a person makes a request that references onscreen content, for example, “Rotate this photo”, Apple Intelligence needs to know which photo is visible onscreen. When you provide this information as context, Siri can respond to a request and perform the action. In addition to conforming to the [`Transferable`](https://developer.apple.com/documentation/coretransferable/transferable) protocol, the `AssetEntity` also conforms to the [`asset`](appschema/photosentity/asset.md) schema. Schema conformance is a prerequisite for providing cues to the system about what’s visible onscreen. To bridge visible content to an app entity that conforms to a schema, you annotate a view or user activity object with an app entity. The `MediaView` shows one photo at a time, so the app annotates a [`NSUserActivity`](https://developer.apple.com/documentation/foundation/nsuseractivity) with the `AssetEntity` that represents the currently visible photo:

```swift
var body: some View {
    // ...
    MediaView(
        image: image,
        duration: asset.duration,
        isFavorite: asset.isFavorite,
        proxy: proxy
    )
    .userActivity(
        "com.example.apple-samplecode.PhotosDomainExample.ViewingPhoto",
        element: asset.entity
    ) { asset, activity in
        activity.title = "Viewing a photo"
        activity.appEntityIdentifier = EntityIdentifier(for: asset)
    }
    // ...
```

For more information about making onscreen content discoverable by Apple Intelligence, see [`Providing contextual cues to Apple Intelligence and Siri`](providing-contextual-cues-to-apple-intelligence-and-siri.md).

#### Create App Intents for Photo Actions

Transferable app entities, Spotlight donations, and user-activity annotations give the system context about your app’s content. To let people perform actions on the content with Siri, create app intents that conform to intent schemas in the `.photos` domain that match photo actions. For example, the sample app implements an intent that conforms to the [`createAlbum`](appschema/photosintent/createalbum.md) schema to let people create a photo album in the app with Siri:

```swift
@AppIntent(schema: .photos.createAlbum)
struct CreateAlbumIntent: AppIntent {
    var name: String

    @Dependency
    var library: MediaLibrary

    @MainActor
    func perform() async throws -> some ReturnsValue<AlbumEntity> {
        let album = try await library.createAlbum(with: name)
        return .result(value: album.entity)
    }
}
```

For more information about making photo actions discoverable by Apple Intelligence and Siri, see [`Making actions and content discoverable by Apple Intelligence`](making-actions-and-content-discoverable-by-apple-intelligence.md) and [`Photos`](app-schema-domain-photos.md).

## See Also

- [Integrating your messaging app with Apple Intelligence](integrating-your-messaging-app-with-apple-intelligence.md)
  Adopt message schemas so people can send messages and manage conversations with Siri.
- [Integrating your calendar app with Apple Intelligence](integrating-your-calendar-app-with-apple-intelligence.md)
  Adopt calendar schemas so people can create, find, and manage events with Siri.
- [Integrating your music app with Apple Intelligence](integrating-your-music-app-with-apple-intelligence.md)
  Adopt the audio and clock schemas so people can play music and set alarms with Siri.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/integrating-your-photo-app-with-apple-intelligence)*