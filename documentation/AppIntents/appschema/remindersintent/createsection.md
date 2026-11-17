# createSection

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An intent schema that creates a new reminder list section.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var createSection: some AppSchemaIntent { get }
```

## Discussion

To make your app’s actions available to Apple Intelligence, conform your [`AppIntent`](../../appintent.md) to a schema that describes your action to the system. If your app’s functionality aligns with the `reminders` domain and one of your app’s actions matches the `createSection` schema, you can generate the properties and protocol conformance the schema requires for your intent implementation with the `@AppIntent(schema: .reminders.createSection)` Swift macro. To make your app work with Siri, see [Apple Intelligence and Siri AI](../../apple-intelligence-and-siri-ai.md).

The following example shows an intent that conforms to the `createSection` schema. You can create a type that conforms to the schema by adding the `@AppIntent` macro above the type’s declaration. Xcode inserts a template type into your code for you, which includes the macro, when you type the first few characters of `reminders_createSection` and select it from the code-completion suggestions:

```swift
@AppIntent(schema: .reminders.createSection)
struct CreateSectionIntent {
    /// The name of the section to create.
    var name: String

    /// The list to which the section belongs.
    var list: <#ListEntity#>

    func perform() async throws -> some ReturnsValue<<#SectionEntity#>> {
        <#code#>
    }
}
```

The schema supports the following system experiences:

- Siri
- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [Getting started with the App Intents framework](../../getting-started-with-the-app-intents-framework.md).

## Parameters for the create-section intent

Each parameter in the code listing above plays a specific role when your app performs this action. The following table describes what each parameter represents and any behavior to account for when you set it.

| Parameter | Type | Origin | Discussion |
| --- | --- | --- | --- |
| `name` | `String` | Swift | The name of the section to create. |
| `list` | `@AppEntity(schema: .reminders.list)` | Your app | The list to which the section belongs. `ListEntity` is a placeholder name for a type that conforms to the [`list`](../remindersentity/list.md) entity schema, which your app defines and implements. |

## See Also

### Actions
- [var createList: some AppSchemaIntent](./createlist.md)
  An intent schema that creates a new reminder list.
- [var createReminder: some AppSchemaIntent](./createreminder.md)
  An intent schema that creates a new reminder.
- [var deleteReminders: some AppSchemaIntent](./deletereminders.md)
  An intent schema that deletes reminders.
- [var updateReminder: some AppSchemaIntent](./updatereminder.md)
  An intent schema that updates a reminder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/remindersintent/createsection)*