# list

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An entity schema for a list.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var list: some AppSchemaEntity { get }
```

## Discussion

To make your app’s content available to Apple Intelligence, conform your [`AppEntity`](../../appentity.md) to a schema that describes your content to the system. If your app’s functionality aligns with the `reminders` domain and its content matches the `list` schema, you can generate the properties and protocol conformance the schema requires for your app entity implementation with the `@AppEntity(schema: .reminders.list)` Swift macro. To make your app work with Siri, see [Apple Intelligence and Siri AI](../../apple-intelligence-and-siri-ai.md).

The following example shows an app entity that conforms to the `list` schema. You can create a type that conforms to the schema by adding the `@AppEntity` macro above the type’s declaration. Xcode inserts a template type into your code for you, which includes the macro, when you type the first few characters of `reminders_list` and select it from the code-completion suggestions:

```swift
@AppEntity(schema: .reminders.list)
struct ListEntity {
    // MARK: Default query

    /// The standard lookup the system runs to find one or more list entities, unless you provide another.
    static let defaultQuery = ListEntityQuery()

    // MARK: Entity properties

    /// The unique identifier for the list entity.
    let id: <#Identifiable.ID#>

    var name: String

    var type: <#ListType#>

    /// The details the system shows to identify the list entity to a person, such as a title and image.
    var displayRepresentation: DisplayRepresentation {
        <#DisplayRepresentation#>
    }

    // MARK: Query type

    /// A type that looks up one or more list entities by their identifiers.
    struct ListEntityQuery: EntityQuery {
        func entities(for identifiers: [ListEntity.ID]) async throws -> [ListEntity] {
            <#code#>
        }
    }
}
```

The schema supports the following system experiences:

- Siri
- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [Getting started with the App Intents framework](../../getting-started-with-the-app-intents-framework.md).

## Properties of the list entity

Each property in the code listing above describes a facet of the entity your app provides to the system. The following table describes what each property represents.

| Property | Type | Origin | Discussion |
| --- | --- | --- | --- |
| `name` | `String` | Swift | Name |
| `type` | `@AppEnum(schema: .reminders.listType)` | Your app | Type `ListType` is a placeholder name for a type that conforms to the [`listType`](../remindersenum/listtype.md) enum schema, which your app defines and implements. |

## See Also

### Content and parameter types
- [var group: some AppSchemaEntity](./group.md)
  An entity schema for a group.
- [var locationTrigger: some AppSchemaEntity](./locationtrigger.md)
  An entity schema for a location trigger.
- [var reminder: some AppSchemaEntity](./reminder.md)
  An entity schema for a reminder.
- [var section: some AppSchemaEntity](./section.md)
  An entity schema for a section.
- [AppSchema.RemindersEntity](../remindersentity.md)
  Identifies entity schemas in the reminders domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/remindersentity/list)*