# createAudioEntry

**Framework**: App Intents  
**Kind**: property

An intent schema that creates a new audio journal entry.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var createAudioEntry: some AppSchemaIntent { get }
```

#### Discussion

To make your app’s actions available to Apple Intelligence, conform your [`AppIntent`](appintent.md) to a schema that describes your action to the system. If your app’s functionality aligns with the `journal` domain and one of your app’s actions matches the `createAudioEntry` schema, you can generate the properties and protocol conformance the schema requires for your intent implementation with the `@AppIntent( .journal.createAudioEntry)` Swift macro. To make your app work with Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

The following example shows an intent that conforms to the `createAudioEntry` schema:

```swift
@AppIntent(schema: .journal.createAudioEntry)
struct CreateJournalAudioEntryIntent: AudioStartingIntent {
    func perform() async throws -> some IntentResult {
        <#code#>
    }
}
```

The schema supports the following system experiences:

- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [`Getting started with the App Intents framework`](getting-started-with-the-app-intents-framework.md).

## See Also

- [var createEntry: some AppSchemaIntent](appschema/journalintent/createentry.md)
  An intent schema that creates a new journal entry.
- [var deleteEntry: some AppSchemaIntent](appschema/journalintent/deleteentry.md)
  An intent schema that deletes the specified journal entries.
- [var updateEntry: some AppSchemaIntent](appschema/journalintent/updateentry.md)
  An intent schema that updates journal entry.
- [AppSchema.JournalIntent](appschema/journalintent.md)
  Identifies intent schemas in the journal domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/journalintent/createaudioentry)*