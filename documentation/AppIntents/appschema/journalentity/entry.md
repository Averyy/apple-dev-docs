# entry

**Framework**: App Intents  
**Kind**: property

An entity schema for an entry.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
var entry: some AppSchemaEntity { get }
```

#### Discussion

To make your app’s content available to Apple Intelligence, conform your [`AppEntity`](appentity.md) to a schema that describes your content to the system. If your app’s functionality aligns with the `journal` domain and its content matches the `entry` schema, you can generate the properties and protocol conformance the schema requires for your app entity implementation with the `@AppEntity( .journal.entry)` Swift macro. To make your app work with Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

The following example shows an app entity that conforms to the `entry` schema:

```swift
@AppEntity(schema: .journal.entry)
struct JournalEntity {
    // MARK: Static

    static let defaultQuery = JournalEntityQuery()

    // MARK: Properties

    let id: <#Identifiable.ID#>

    var title: String?
    var message: AttributedString?
    var mediaItems: [IntentFile]
    var entryDate: Date?
    var location: GeoToolbox.PlaceDescriptor?

    var displayRepresentation: DisplayRepresentation {
        <#DisplayRepresentation#>
    }

    // MARK: Query

    struct JournalEntityQuery: EntityQuery {
        func entities(for identifiers: [JournalEntity.ID]) async throws -> [JournalEntity] {
            <#code#>
        }
    }
}
```

The schema supports the following system experiences:

- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [`Getting started with the App Intents framework`](getting-started-with-the-app-intents-framework.md).

## See Also

- [AppSchema.JournalEntity](appschema/journalentity.md)
  Identifies entity schemas in the journal domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/journalentity/entry)*