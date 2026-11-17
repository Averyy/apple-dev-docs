# updateEntry

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An intent schema that updates journal entry.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var updateEntry: some AppSchemaIntent { get }
```

## Discussion

To make your app’s actions available to Apple Intelligence, conform your [`AppIntent`](../../appintent.md) to a schema that describes your action to the system. If your app’s functionality aligns with the `journal` domain and one of your app’s actions matches the `updateEntry` schema, you can generate the properties and protocol conformance the schema requires for your intent implementation with the `@AppIntent(schema: .journal.updateEntry)` Swift macro.

The following example shows an intent that conforms to the `updateEntry` schema. You can create a type that conforms to the schema by adding the `@AppIntent` macro above the type’s declaration. Xcode inserts a template type into your code for you, which includes the macro, when you type the first few characters of `journal_updateEntry` and select it from the code-completion suggestions:

```swift
@AppIntent(schema: .journal.updateEntry)
struct UpdateJournalEntryIntent {
    /// Journal to update.
    var target: <#JournalEntity#>

    /// Title to add to the entry.
    var title: String?

    /// Message to add to the entry.
    var message: AttributedString?

    /// New entry media items.
    var mediaItems: [IntentFile]?

    /// Date to add to the entry.
    var entryDate: Date?

    /// Current location to add to the entry.
    var location: GeoToolbox.PlaceDescriptor?

    func perform() async throws -> some IntentResult {
        <#code#>
    }
}
```

The schema supports the following system experiences:

- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [Getting started with the App Intents framework](../../getting-started-with-the-app-intents-framework.md).

## Parameters for the update-entry intent

Each parameter in the code listing above plays a specific role when your app performs this action. The following table describes what each parameter represents and any behavior to account for when you set it.

| Parameter | Type | Origin | Discussion |
| --- | --- | --- | --- |
| `target` | `@AppEntity(schema: .journal.entry)` | Your app | Journal to update. `JournalEntity` is a placeholder name for a type that conforms to the [`entry`](../journalentity/entry.md) entity schema, which your app defines and implements. |
| `title` | `String?` | Swift | Title to add to the entry. |
| `message` | `AttributedString?` | Foundation | Message to add to the entry. |
| `mediaItems` | `[IntentFile]?` | App Intents | New entry media items. |
| `entryDate` | `Date?` | Foundation | Date to add to the entry. |
| `location` | `GeoToolbox.PlaceDescriptor?` | GeoToolbox | Current location to add to the entry. |

## See Also

### Actions
- [var createAudioEntry: some AppSchemaIntent](./createaudioentry.md)
  An intent schema that creates a new audio journal entry.
- [var createEntry: some AppSchemaIntent](./createentry.md)
  An intent schema that creates a new journal entry.
- [var deleteEntry: some AppSchemaIntent](./deleteentry.md)
  An intent schema that deletes the specified journal entries.
- [AppSchema.JournalIntent](../journalintent.md)
  Identifies intent schemas in the journal domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/journalintent/updateentry)*