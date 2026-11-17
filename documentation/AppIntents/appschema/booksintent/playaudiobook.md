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

## Discussion

To make your app’s actions available to Apple Intelligence, conform your [`AppIntent`](../../appintent.md) to a schema that describes your action to the system. If your app’s functionality aligns with the `books` domain and one of your app’s actions matches the `playAudiobook` schema, you can generate the properties and protocol conformance the schema requires for your intent implementation with the `@AppIntent(schema: .books.playAudiobook)` Swift macro.

The following example shows an intent that conforms to the `playAudiobook` schema. You can create a type that conforms to the schema by adding the `@AppIntent` macro above the type’s declaration. Xcode inserts a template type into your code for you, which includes the macro, when you type the first few characters of `books_playAudiobook` and select it from the code-completion suggestions:

```swift
@AppIntent(schema: .books.playAudiobook)
struct PlayAudiobookIntent: AudioStartingIntent {
    /// Audiobook to open.
    var target: <#AudiobookEntity#>

    func perform() async throws -> some IntentResult {
        <#code#>
    }
}
```

The schema supports the following system experiences:

- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [Getting started with the App Intents framework](../../getting-started-with-the-app-intents-framework.md).

## Parameters for the play-audiobook intent

Each parameter in the code listing above plays a specific role when your app performs this action. The following table describes what each parameter represents and any behavior to account for when you set it.

| Parameter | Type | Origin | Discussion |
| --- | --- | --- | --- |
| `target` | `@AppEntity(schema: .books.audiobook)` | Your app | Audiobook to open. `AudiobookEntity` is a placeholder name for a type that conforms to the [`audiobook`](../booksentity/audiobook.md) entity schema, which your app defines and implements. |

## See Also

### Deprecated schemas
- [var search: some AppSchemaIntent](./search.md)
  An intent schema that opens the app and searches for the given term.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/booksintent/playaudiobook)*