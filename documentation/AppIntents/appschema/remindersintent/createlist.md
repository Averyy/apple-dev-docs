# createList

**Framework**: App Intents  
**Kind**: property

An intent schema that creates a new reminder list.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var createList: some AppSchemaIntent { get }
```

#### Discussion

To make your app’s actions available to Apple Intelligence, conform your [`AppIntent`](appintent.md) to a schema that describes your action to the system. If your app’s functionality aligns with the `reminders` domain and one of your app’s actions matches the `createList` schema, you can generate the properties and protocol conformance the schema requires for your intent implementation with the `@AppIntent( .reminders.createList)` Swift macro. To make your app work with Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

The following example shows an intent that conforms to the `createList` schema:

```swift
@AppIntent(schema: .reminders.createList)
struct CreateListIntent {
    var type: <#ListType#>
    var name: String

    func perform() async throws -> some ReturnsValue<<#ListEntity#>> {
        <#code#>
    }
}
```

The schema supports the following system experiences:

- Siri
- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [`Getting started with the App Intents framework`](getting-started-with-the-app-intents-framework.md).

## See Also

- [var createReminder: some AppSchemaIntent](appschema/remindersintent/createreminder.md)
  An intent schema that creates a new reminder.
- [var createSection: some AppSchemaIntent](appschema/remindersintent/createsection.md)
  An intent schema that creates a new reminder list section.
- [var deleteReminders: some AppSchemaIntent](appschema/remindersintent/deletereminders.md)
  An intent schema that deletes reminders.
- [var updateReminder: some AppSchemaIntent](appschema/remindersintent/updatereminder.md)
  An intent schema that updates a reminder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/remindersintent/createlist)*