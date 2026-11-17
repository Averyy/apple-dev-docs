# section

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An entity schema for a section.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var section: some AppSchemaEntity { get }
```

## Discussion

To make your app’s content available to Apple Intelligence, conform your [`AppEntity`](../../appentity.md) to a schema that describes your content to the system. If your app’s functionality aligns with the `reminders` domain and its content matches the `section` schema, you can generate the properties and protocol conformance the schema requires for your app entity implementation with the `@AppEntity(schema: .reminders.section)` Swift macro. To make your app work with Siri, see [Apple Intelligence and Siri AI](../../apple-intelligence-and-siri-ai.md).

The following example shows an app entity that conforms to the `section` schema. You can create a type that conforms to the schema by adding the `@AppEntity` macro above the type’s declaration. Xcode inserts a template type into your code for you, which includes the macro, when you type the first few characters of `reminders_section` and select it from the code-completion suggestions:

```swift
@AppEntity(schema: .reminders.section)
struct SectionEntity {
    // MARK: Default query

    /// The standard lookup the system runs to find one or more section entities, unless you provide another.
    static let defaultQuery = SectionEntityQuery()

    // MARK: Entity properties

    /// The unique identifier for the section entity.
    let id: <#Identifiable.ID#>

    var name: String

    var list: <#ListEntity#>

    /// The details the system shows to identify the section entity to a person, such as a title and image.
    var displayRepresentation: DisplayRepresentation {
        <#DisplayRepresentation#>
    }

    // MARK: Query type

    /// A type that looks up one or more section entities by their identifiers.
    struct SectionEntityQuery: EntityQuery {
        func entities(for identifiers: [SectionEntity.ID]) async throws -> [SectionEntity] {
            <#code#>
        }
    }
}
```

The schema supports the following system experiences:

- Siri
- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [Getting started with the App Intents framework](../../getting-started-with-the-app-intents-framework.md).

## Properties of the section entity

Each property in the code listing above describes a facet of the entity your app provides to the system. The following table describes what each property represents.

| Property | Type | Origin | Discussion |
| --- | --- | --- | --- |
| `name` | `String` | Swift | Name |
| `list` | `@AppEntity(schema: .reminders.list)` | Your app | List `ListEntity` is a placeholder name for a type that conforms to the [`list`](./list.md) entity schema, which your app defines and implements. |

## See Also

### Content and parameter types
- [var group: some AppSchemaEntity](./group.md)
  An entity schema for a group.
- [var list: some AppSchemaEntity](./list.md)
  An entity schema for a list.
- [var locationTrigger: some AppSchemaEntity](./locationtrigger.md)
  An entity schema for a location trigger.
- [var reminder: some AppSchemaEntity](./reminder.md)
  An entity schema for a reminder.
- [AppSchema.RemindersEntity](../remindersentity.md)
  Identifies entity schemas in the reminders domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/remindersentity/section)*