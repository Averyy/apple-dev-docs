# reminder

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An entity schema for a reminder.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var reminder: some AppSchemaEntity { get }
```

## Discussion

To make your app’s content available to Apple Intelligence, conform your [`AppEntity`](../../appentity.md) to a schema that describes your content to the system. If your app’s functionality aligns with the `reminders` domain and its content matches the `reminder` schema, you can generate the properties and protocol conformance the schema requires for your app entity implementation with the `@AppEntity(schema: .reminders.reminder)` Swift macro. To make your app work with Siri, see [Apple Intelligence and Siri AI](../../apple-intelligence-and-siri-ai.md).

The following example shows an app entity that conforms to the `reminder` schema. You can create a type that conforms to the schema by adding the `@AppEntity` macro above the type’s declaration. Xcode inserts a template type into your code for you, which includes the macro, when you type the first few characters of `reminders_reminder` and select it from the code-completion suggestions:

```swift
@AppEntity(schema: .reminders.reminder)
struct ReminderEntity {
    // MARK: Default query

    /// The standard lookup the system runs to find one or more reminder entities, unless you provide another.
    static let defaultQuery = ReminderEntityQuery()

    // MARK: Entity properties

    /// The unique identifier for the reminder entity.
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

    /// The details the system shows to identify the reminder entity to a person, such as a title and image.
    var displayRepresentation: DisplayRepresentation {
        <#DisplayRepresentation#>
    }

    // MARK: Query type

    /// A type that looks up one or more reminder entities by their identifiers.
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

For more information about the App Intents framework and the experiences it supports, see [Getting started with the App Intents framework](../../getting-started-with-the-app-intents-framework.md).

## Properties of the reminder entity

Each property in the code listing above describes a facet of the entity your app provides to the system. The following table describes what each property represents.

| Property | Type | Origin | Discussion |
| --- | --- | --- | --- |
| `title` | `String` | Swift | Title |
| `note` | `AttributedString?` | Foundation | Note |
| `tags` | `Set<String>` | Swift | Tags |
| `urls` | `[URL]` | Foundation | URLs |
| `dueDate` | `DateComponents?` | Foundation | Due Date |
| `recurrence` | `Calendar.RecurrenceRule?` | Foundation | Recurrence |
| `isCompleted` | `Bool` | Swift | Is Completed |
| `isFlagged` | `Bool?` | Swift | Is Flagged |
| `creationDate` | `Date?` | Foundation | Creation Date |
| `completionDate` | `Date?` | Foundation | Completion Date |
| `list` | `@AppEntity(schema: .reminders.list)` | Your app | List `ListEntity` is a placeholder name for a type that conforms to the [`list`](./list.md) entity schema, which your app defines and implements. |
| `locationTrigger` | `@AppEntity(schema: .reminders.locationTrigger)?` | Your app | Location `LocationTriggerEntity` is a placeholder name for a type that conforms to the [`locationTrigger`](./locationtrigger.md) entity schema, which your app defines and implements. |

## See Also

### Content and parameter types
- [var group: some AppSchemaEntity](./group.md)
  An entity schema for a group.
- [var list: some AppSchemaEntity](./list.md)
  An entity schema for a list.
- [var locationTrigger: some AppSchemaEntity](./locationtrigger.md)
  An entity schema for a location trigger.
- [var section: some AppSchemaEntity](./section.md)
  An entity schema for a section.
- [AppSchema.RemindersEntity](../remindersentity.md)
  Identifies entity schemas in the reminders domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/remindersentity/reminder)*