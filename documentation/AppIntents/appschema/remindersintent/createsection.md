# createSection

**Framework**: App Intents  
**Kind**: property

An intent schema that creates a new reminder list section.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var createSection: some AppSchemaIntent { get }
```

#### Discussion

To make your app’s actions available to Apple Intelligence, conform your [`AppIntent`](appintent.md) to a schema that describes your action to the system. If your app’s functionality aligns with the `reminders` domain and one of your app’s actions matches the `createSection` schema, you can generate the properties and protocol conformance the schema requires for your intent implementation with the `@AppIntent( .reminders.createSection)` Swift macro. To make your app work with Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

The following example shows an intent that conforms to the `createSection` schema:

```swift
@AppIntent(schema: .reminders.createSection)
struct CreateSectionIntent {
    var name: String
    var list: <#ListEntity#>

    func perform() async throws -> some ReturnsValue<<#SectionEntity#>> {
        <#code#>
    }
}
```

The schema supports the following system experiences:

- Siri
- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [`Getting started with the App Intents framework`](getting-started-with-the-app-intents-framework.md).

## See Also

- [var createList: some AppSchemaIntent](appschema/remindersintent/createlist.md)
  An intent schema that creates a new reminder list.
- [var createReminder: some AppSchemaIntent](appschema/remindersintent/createreminder.md)
  An intent schema that creates a new reminder.
- [var deleteReminders: some AppSchemaIntent](appschema/remindersintent/deletereminders.md)
  An intent schema that deletes reminders.
- [var updateGroup: some AppSchemaIntent](appschema/remindersintent/updategroup.md)
  An intent schema that updates a reminder list group.
- [var updateList: some AppSchemaIntent](appschema/remindersintent/updatelist.md)
  An intent schema that updates a reminder list.
- [var updateReminder: some AppSchemaIntent](appschema/remindersintent/updatereminder.md)
  An intent schema that updates a reminder.
- [var updateSection: some AppSchemaIntent](appschema/remindersintent/updatesection.md)
  An intent schema that updates a reminder list section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/remindersintent/createsection)*