# recognizedPerson

**Framework**: App Intents  
**Kind**: property

The app entity describes a person who appears in an asset.

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
var recognizedPerson: some AssistantSchemas.Entity { get }
```

#### Overview

Use Swift macros that generate additional properties and add protocol conformance for your app entity implementation. The following example shows an app entity that conforms to the `.photos.recognizedPerson` schema:

```swift
@AppEntity(schema: .photos.recognizedPerson)
struct PhotoPersonEntity: AppEntity {
    struct Query: EntityStringQuery {
        func entities(for identifiers: [PhotoPersonEntity.ID]) async throws -> [PhotoPersonEntity] { [] }
        func entities(matching string: String) async throws -> [PhotoPersonEntity] { [] }
    }

    static var defaultQuery = Query()
    var displayRepresentation: DisplayRepresentation { "Photo Person" }

    let id = UUID()

    @Property
    var name: String

    @Property
    var isFavorite: Bool
}
```

For more information about the `.photos` app intent domain, see doc:Making-photo-and-video-actions-available-to-siri-and-apple-intelligence. For general information about app intent domains, see doc:Integrating-actions-with-siri-and-apple-intelligence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/photosentity/recognizedperson)*