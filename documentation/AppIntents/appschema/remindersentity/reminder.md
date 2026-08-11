# reminder

**Framework**: App Intents  
**Kind**: property

An entity schema for a reminder.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var reminder: some AppSchemaEntity { get }
```

#### Discussion

To make your app’s content available to Apple Intelligence, conform your [`AppEntity`](appentity.md) to a schema that describes your content to the system. If your app’s functionality aligns with the `reminders` domain and its content matches the `reminder` schema, you can generate the properties and protocol conformance the schema requires for your app entity implementation with the `@AppEntity( .reminders.reminder)` Swift macro. To make your app work with Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

The following example shows an app entity that conforms to the `reminder` schema:

```swift
@AppEntity(schema: .reminders.reminder)
struct ReminderEntity {
    // MARK: Static

    static let defaultQuery = ReminderEntityQuery()

    // MARK: Properties

    let id: <#Identifiable.ID#>

    var title: String
    var note: AttributedString?
    var tags: Set<String>
    var urls: [URL]
    var dueDate: DateComponents?
    var recurrence: Calendar.RecurrenceRule?
    var isCompleted: Bool
    var isFlagged: Bool?
    var creationDate: Date?
    var completionDate: Date?
    var list: <#ListEntity#>
    var locationTrigger: <#LocationTriggerEntity#>?

    var displayRepresentation: DisplayRepresentation {
        <#DisplayRepresentation#>
    }

    // MARK: Query

    struct ReminderEntityQuery: EntityQuery {
        func entities(for identifiers: [ReminderEntity.ID]) async throws -> [ReminderEntity] {
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

- [var group: some AppSchemaEntity](appschema/remindersentity/group.md)
  An entity schema for a group.
- [var list: some AppSchemaEntity](appschema/remindersentity/list.md)
  An entity schema for a list.
- [var locationTrigger: some AppSchemaEntity](appschema/remindersentity/locationtrigger.md)
  An entity schema for a location trigger.
- [var section: some AppSchemaEntity](appschema/remindersentity/section.md)
  An entity schema for a section.
- [AppSchema.RemindersEntity](appschema/remindersentity.md)
  Identifies entity schemas in the reminders domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/remindersentity/reminder)*