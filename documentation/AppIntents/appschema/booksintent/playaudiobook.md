# playAudiobook

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An intent schema that plays an audiobook.

**Availability**:
- iOS 18.0+ - Deprecated in 27.0
- iPadOS 18.0+ - Deprecated in 27.0
- Mac Catalyst 18.0+ - Deprecated in 27.0
- macOS 15.0+ - Deprecated in 27.0
- visionOS 2.0+ - Deprecated in 27.0

> **Deprecated**: Use .audio.playAudio instead

## Declaration

```swift
var playAudiobook: some AppSchemaIntent { get }
```

#### Discussion

To make your app’s actions available to Apple Intelligence, conform your [`AppIntent`](../../appintent.md) to a schema that describes your action to the system. If your app’s functionality aligns with the `books` domain and one of your app’s actions matches the `playAudiobook` schema, you can generate the properties and protocol conformance the schema requires for your intent implementation with the `@AppIntent( .books.playAudiobook)` Swift macro. To make your app work with Siri, see [Apple Intelligence and Siri AI](../../apple-intelligence-and-siri-ai.md).

The following example shows an intent that conforms to the `playAudiobook` schema:

```swift
@AppIntent(schema: .books.playAudiobook)
struct PlayAudiobookIntent: AudioStartingIntent {
    var target: <#AudiobookEntity#>

    func perform() async throws -> some IntentResult {
        <#code#>
    }
}
```

The schema supports the following system experiences:

- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [Getting started with the App Intents framework](../../getting-started-with-the-app-intents-framework.md).

## See Also

### Deprecated schemas
- [var search: some AppSchemaIntent](./search.md)
  An intent schema that opens the app and searches for the given term.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/booksintent/playaudiobook)*