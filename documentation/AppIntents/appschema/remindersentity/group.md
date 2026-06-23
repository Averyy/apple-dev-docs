# group

**Framework**: App Intents  
**Kind**: property

An entity schema for a group.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var group: some AppSchemaEntity { get }
```

#### Discussion

To make your app’s content available to Apple Intelligence, conform your [`AppEntity`](appentity.md) to a schema that describes your content to the system. If your app’s functionality aligns with the `reminders` domain and its content matches the `group` schema, you can generate the properties and protocol conformance the schema requires for your app entity implementation with the `@AppEntity( .reminders.group)` Swift macro. To make your app work with Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

The following example shows an app entity that conforms to the `group` schema:

```swift
@AppEntity(schema: .reminders.group)
struct GroupEntity {
    // MARK: Static

    static let defaultQuery = GroupEntityQuery()

    // MARK: Properties

    let id: <#Identifiable.ID#>

    var name: String
    var lists: [<#ListEntity#>]

    var displayRepresentation: DisplayRepresentation {
        <#DisplayRepresentation#>
    }

    // MARK: Query

    struct GroupEntityQuery: EntityQuery {
        func entities(for identifiers: [GroupEntity.ID]) async throws -> [GroupEntity] {
            <#code#>
        }
    }
}
```

The schema supports the following system experiences:

- Siri
- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [`Getting started with the App Intents framework`](getting-started-with-the-app-intents-framework.md).

## See Also

- [var list: some AppSchemaEntity](appschema/remindersentity/list.md)
  An entity schema for a list.
- [var locationTrigger: some AppSchemaEntity](appschema/remindersentity/locationtrigger.md)
  An entity schema for a location trigger.
- [var reminder: some AppSchemaEntity](appschema/remindersentity/reminder.md)
  An entity schema for a reminder.
- [var section: some AppSchemaEntity](appschema/remindersentity/section.md)
  An entity schema for a section.
- [AppSchema.RemindersEntity](appschema/remindersentity.md)
  Identifies entity schemas in the reminders domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/remindersentity/group)*