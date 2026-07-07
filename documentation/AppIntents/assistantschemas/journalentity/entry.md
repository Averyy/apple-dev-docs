# entry

**Framework**: App Intents  
**Kind**: property

The app entity describes a journal entry.

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
var entry: some AssistantSchemas.Entity { get }
```

#### Overview

Use Swift macros that generate additional properties and add protocol conformance for your app entity implementation. The following example shows an app entity that conforms to the `.journal.entry` schema:

```swift
@AppEntity(schema: .journal.entry)
struct JournalEntity: AppEntity {
    struct Query: EntityStringQuery {
        func entities(for identifiers: [JournalEntity.ID]) async throws -> [JournalEntity] { [] }
        func entities(matching string: String) async throws -> [JournalEntity] { [] }
    }

    static var defaultQuery = Query()
    var displayRepresentation: DisplayRepresentation { "Journal Entry" }

    let id = UUID()

    @Property
    var title: String?

    @Property
    var message: AttributedString?

    @Property
    var mediaItems: [IntentFile]

    @Property
    var entryDate: Date?

    @Property
    var location: CLPlacemark?
}
```

For more information about the `.journal` app intent domain, see doc:Making-journaling-actions-available-to-siri-and-apple-intelligence. For general information about app intent domains, see doc:Integrating-actions-with-siri-and-apple-intelligence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/journalentity/entry)*