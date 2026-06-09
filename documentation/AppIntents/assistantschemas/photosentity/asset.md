# asset

**Framework**: App Intents  
**Kind**: property

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
var asset: some AssistantSchemas.Entity { get }
```

#### Overview

To integrate your app’s functionality with Siri and Apple Intelligence, you use Swift macros that generate additional properties and add protocol conformance for your app entity implementation.

For general information about app intent domains, see doc:Integrating-actions-with-siri-and-apple-intelligence.

The following example shows an app entity that conforms to the `photos.asset` schema:

```swift
@AppEntity(schema: .photos.asset)
struct PhotoEntity: CollaborativeEntity {
    struct PhotoEntityQuery: EntityQuery {
        func entities(for identifiers: [PhotoEntity.ID]) async throws -> [PhotoEntity] {
            <#code#>
        }
    }
    static let defaultQuery = PhotoEntityQuery()

    static var sharedWith = <#[IntentPerson]#>

    let displayRepresentation: DisplayRepresentation = {
        <#DisplayRepresentation#>
    }

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

    let id: <#Identifiable.ID#>
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/photosentity/asset)*