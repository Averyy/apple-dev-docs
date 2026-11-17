# deleteEntry

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An intent schema that deletes the specified journal entries.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var deleteEntry: some AppSchemaIntent { get }
```

## Discussion

To make your app’s actions available to Apple Intelligence, conform your [`AppIntent`](../../appintent.md) to a schema that describes your action to the system. If your app’s functionality aligns with the `journal` domain and one of your app’s actions matches the `deleteEntry` schema, you can generate the properties and protocol conformance the schema requires for your intent implementation with the `@AppIntent(schema: .journal.deleteEntry)` Swift macro.

The following example shows an intent that conforms to the `deleteEntry` schema. You can create a type that conforms to the schema by adding the `@AppIntent` macro above the type’s declaration. Xcode inserts a template type into your code for you, which includes the macro, when you type the first few characters of `journal_deleteEntry` and select it from the code-completion suggestions:

```swift
@AppIntent(schema: .journal.deleteEntry)
struct DeleteJournalEntryIntent: DeleteIntent {
    /// Journal entries to delete.
    var entities: [<#JournalEntity#>]

    func perform() async throws -> some IntentResult {
        <#code#>
    }
}
```

The schema supports the following system experiences:

- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [Getting started with the App Intents framework](../../getting-started-with-the-app-intents-framework.md).

## Parameters for the delete-entry intent

Each parameter in the code listing above plays a specific role when your app performs this action. The following table describes what each parameter represents and any behavior to account for when you set it.

| Parameter | Type | Origin | Discussion |
| --- | --- | --- | --- |
| `entities` | `[@AppEntity(schema: .journal.entry)]` | Your app | Journal entries to delete. `JournalEntity` is a placeholder name for a type that conforms to the [`entry`](../journalentity/entry.md) entity schema, which your app defines and implements. |

## See Also

### Actions
- [var createAudioEntry: some AppSchemaIntent](./createaudioentry.md)
  An intent schema that creates a new audio journal entry.
- [var createEntry: some AppSchemaIntent](./createentry.md)
  An intent schema that creates a new journal entry.
- [var updateEntry: some AppSchemaIntent](./updateentry.md)
  An intent schema that updates journal entry.
- [AppSchema.JournalIntent](../journalintent.md)
  Identifies intent schemas in the journal domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/journalintent/deleteentry)*