# entry

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An entity schema for an entry.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var entry: some AppSchemaEntity { get }
```

## Discussion

To make your app’s content available to Apple Intelligence, conform your [`AppEntity`](../../appentity.md) to a schema that describes your content to the system. If your app’s functionality aligns with the `journal` domain and its content matches the `entry` schema, you can generate the properties and protocol conformance the schema requires for your app entity implementation with the `@AppEntity(schema: .journal.entry)` Swift macro.

The following example shows an app entity that conforms to the `entry` schema. You can create a type that conforms to the schema by adding the `@AppEntity` macro above the type’s declaration. Xcode inserts a template type into your code for you, which includes the macro, when you type the first few characters of `journal_entry` and select it from the code-completion suggestions:

```swift
@AppEntity(schema: .journal.entry)
struct JournalEntity {
    // MARK: Default query

    /// The standard lookup the system runs to find one or more journal entry entities, unless you provide another.
    static let defaultQuery = JournalEntityQuery()

    // MARK: Entity properties

    /// The unique identifier for the journal entry entity.
    let id: <#Identifiable.ID#>

    var title: String?

    var message: AttributedString?

    var mediaItems: [IntentFile]

    var entryDate: Date?

    var location: GeoToolbox.PlaceDescriptor?

    /// The details the system shows to identify the journal entry entity to a person, such as a title and image.
    var displayRepresentation: DisplayRepresentation {
        <#DisplayRepresentation#>
    }

    // MARK: Query type

    /// A type that looks up one or more journal entry entities by their identifiers.
    struct JournalEntityQuery: EntityQuery {
        func entities(for identifiers: [JournalEntity.ID]) async throws -> [JournalEntity] {
            <#code#>
        }
    }
}
```

The schema supports the following system experiences:

- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [Getting started with the App Intents framework](../../getting-started-with-the-app-intents-framework.md).

## Properties of the entry entity

Each property in the code listing above describes a facet of the entity your app provides to the system. The following table describes what each property represents.

| Property | Type | Origin | Discussion |
| --- | --- | --- | --- |
| `title` | `String?` | Swift | Title |
| `message` | `AttributedString?` | Foundation | Message |
| `mediaItems` | `[IntentFile]` | App Intents | Media Items |
| `entryDate` | `Date?` | Foundation | Entry Date |
| `location` | `GeoToolbox.PlaceDescriptor?` | GeoToolbox | Location |

## See Also

### Content and parameter types
- [AppSchema.JournalEntity](../journalentity.md)
  Identifies entity schemas in the journal domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/journalentity/entry)*