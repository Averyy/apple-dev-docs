# album

**Framework**: App Intents  
**Kind**: property

The app entity describes an album.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var album: some AssistantSchemas.Entity { get }
```

#### Overview

Use Swift macros that generate additional properties and add protocol conformance for your app entity implementation.The following example shows an app entity that conforms to the `.photos.album` schema:

```swift
@AssistantEntity(schema: .photos.album)
struct PhotoAlbumEntity: AppEntity {
    struct Query: EntityStringQuery {
        func entities(for identifiers: [PhotoAlbumEntity.ID]) async throws -> [PhotoAlbumEntity] { [] }
        func entities(matching string: String) async throws -> [PhotoAlbumEntity] { [] }
    }

    static var defaultQuery = Query()
    var displayRepresentation: DisplayRepresentation { "Photo Album" }

    let id = UUID()

    @Property
    var name: String

    @Property
    var creationDate: Date?

    @Property
    var albumType: PhotoAlbumType
}
```

For more information about the `.photos` app intent domain, see [`Making photo and video actions available to Siri and Apple Intelligence`](making-photo-and-video-actions-available-to-siri-and-apple-intelligence.md). For general information about app intent domains, see [`Integrating actions with Siri and Apple Intelligence`](integrating-actions-with-siri-and-apple-intelligence.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/entityschema/album)*