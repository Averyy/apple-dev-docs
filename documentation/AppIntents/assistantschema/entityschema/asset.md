# asset

**Framework**: App Intents  
**Kind**: property

The app entity describes a media asset.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var asset: some AssistantSchemas.Entity { get }
```

#### Overview

To integrate your app’s functionality with Siri and Apple Intelligence, you use Swift macros that generate additional properties and add protocol conformance for your app entity implementation.

For more information about the `.photos` app intent domain, see [`Making photo and video actions available to Siri and Apple Intelligence`](making-photo-and-video-actions-available-to-siri-and-apple-intelligence.md). For general information about app intent domains, see [`Integrating actions with Siri and Apple Intelligence`](integrating-actions-with-siri-and-apple-intelligence.md).

The following example shows an app entity that conforms to the `.photos.asset` schema:

```swift
@AssistantEntity(schema: .photos.asset)
struct PhotoEntity: AppEntity {
    struct Query: EntityStringQuery {
        func entities(for identifiers: [PhotoEntity.ID]) async throws -> [PhotoEntity] { [] }
        func entities(matching string: String) async throws -> [PhotoEntity] { [] }
    }
    static var defaultQuery = Query()
    var displayRepresentation: DisplayRepresentation { "Asset" }

    let id = UUID()

    @Property
    var creationDate: Date?

    @Property
    var location: CLPlacemark?

    @Property
    var assetType: PhotoAssetType?

    @Property
    var isFavorite: Bool

    @Property
    var isHidden: Bool

    @Property
    var hasSuggestedEdits: Bool
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschema/entityschema/asset)*