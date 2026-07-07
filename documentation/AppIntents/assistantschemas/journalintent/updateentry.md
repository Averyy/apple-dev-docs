# updateEntry

**Framework**: App Intents  
**Kind**: property

The app intent conforms to the schema for updating a journal entry.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var updateEntry: some AssistantSchemas.Intent { get }
```

#### Overview

Use Swift macros that generate additional properties and add protocol conformance for your app intent implementation. The following example shows an app intent that conforms to the `.journal.updateEntry` schema:

```swift
@AppIntent(schema: .journal.updateEntry)
struct UpdateJournalEntryIntent: AppIntent {
    @Parameter
    var target: JournalEntity

    @Parameter
    var title: String?

    @Parameter
    var message: AttributedString?

    @Parameter
    var mediaItems: [IntentFile]?

    @Parameter
    var entryDate: Date?

    @Parameter
    var location: CLPlacemark?

    func perform() async throws -> some IntentResult {
        .result()
    }
}
```

For more information about the `.journal` app intent domain, see doc:Making-journaling-actions-available-to-siri-and-apple-intelligence. For general information about app intent domains, see doc:Integrating-actions-with-siri-and-apple-intelligence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/journalintent/updateentry)*