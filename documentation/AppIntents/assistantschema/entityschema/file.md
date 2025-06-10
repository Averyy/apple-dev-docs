# file

**Framework**: App Intents  
**Kind**: property

The app entity describes a file.

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
var file: some AssistantSchemas.Entity { get }
```

#### Overview

Use Swift macros that generate additional properties and add protocol conformance for your app entity implementation. The following example shows an app entity that conforms to the `.files.file` schema:

```swift
@AssistantEntity(schema: .files.file)
struct ExampleFileEntity: FileEntity {
    var displayRepresentation: AppIntents.DisplayRepresentation { "Example File" }

    static var supportedContentTypes = [UTType.image]

    var id: FileEntityIdentifier

    @Property
    var creationDate: Date?

    @Property
    var fileModificationDate: Date?

    struct Query: EntityStringQuery {
        func entities(for identifiers: [ExampleFileEntity.ID]) async throws -> [ExampleFileEntity] { [] }
        func entities(matching string: String) async throws -> [ExampleFileEntity] { [] }
    }
}
```

For more information about the `.files` app intent domain, see [`Making file management actions available to Siri and Apple Intelligence`](making-file-management-actions-available-to-siri-and-apple-intelligence.md). For general information about app intent domains, see [`Integrating actions with Siri and Apple Intelligence`](integrating-actions-with-siri-and-apple-intelligence.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschema/entityschema/file)*