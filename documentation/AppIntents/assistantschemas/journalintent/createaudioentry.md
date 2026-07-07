# createAudioEntry

**Framework**: App Intents  
**Kind**: property

The app intent conforms to the schema for creating a voice journal entry.

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
var createAudioEntry: some AssistantSchemas.Intent { get }
```

#### Overview

Use Swift macros that generate additional properties and add protocol conformance for your app intent implementation. The following example shows an app intent that conforms to the `.journal.createAudioEntry` schema:

```swift
@AppIntent(schema: .journal.createAudioEntry)
struct CreateAudioEntryIntent: AudioRecordingIntent {

    func perform() async throws -> some ReturnsValue<JournalEntity> {
        .result(value: JournalEntity())
    }
}
```

For more information about the `.journal` app intent domain, see doc:Making-journaling-actions-available-to-siri-and-apple-intelligence. For general information about app intent domains, see doc:Integrating-actions-with-siri-and-apple-intelligence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/journalintent/createaudioentry)*