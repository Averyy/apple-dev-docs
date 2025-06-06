# createEntry

**Framework**: App Intents  
**Kind**: property

The app intent conforms to the schema for creating a journal entry.

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
var createEntry: some AssistantSchemas.Intent { get }
```

## Mentions

- [Making journaling actions available to Siri and Apple Intelligence](making-journaling-actions-available-to-siri-and-apple-intelligence.md)

#### Overview

To integrate your app’s functionality with Siri and Apple Intelligence, you use Swift macros that generate additional properties and add protocol conformance for your app intent implementation.

For more information about the `.journal` app intent domain, see [`Making journaling actions available to Siri and Apple Intelligence`](making-journaling-actions-available-to-siri-and-apple-intelligence.md). For general information about app intent domains, see [`Integrating actions with Siri and Apple Intelligence`](integrating-actions-with-siri-and-apple-intelligence.md).

The following example shows an app intent that conforms to the `.journal.createEntry` schema:

```swift
@AssistantIntent(schema: .journal.createEntry)
struct CreateJournalEntryIntent: AppIntent {
    @Parameter
    var message: AttributedString

    @Parameter
    var title: String?

    @Parameter
    var entryDate: Date?

    @Parameter
    var location: CLPlacemark?

    @Parameter(default: [])
    var mediaItems: [IntentFile]

    func perform() async throws -> some ReturnsValue<JournalEntity> {
        .result(value: JournalEntity())
    }
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/journalintent/createentry)*