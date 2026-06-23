# playAudio

**Framework**: App Intents  
**Kind**: property

An intent schema that plays an audio item.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var playAudio: some AppSchemaIntent { get }
```

#### Discussion

To make your app’s actions available to Apple Intelligence, conform your [`AppIntent`](appintent.md) to a schema that describes your action to the system. If your app’s functionality aligns with the `audio` domain and one of your app’s actions matches the `playAudio` schema, you can generate the properties and protocol conformance the schema requires for your intent implementation with the `@AppIntent( .audio.playAudio)` Swift macro. To make your app work with Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

The following example shows an intent that conforms to the `playAudio` schema:

```swift
@AppIntent(schema: .audio.playAudio)
struct PlayAudioIntent: AudioStartingIntent {
    var audioEntity: <#AudioItem#>
    var playbackAttributes: Set<<#PlaybackAttributes#>>
    var warmupAudioQueueResult: <#WarmupAudioQueueResult#>?
    var queueLocation: <#QueueInsertionLocation#>?

    func perform() async throws -> some IntentResult {
        <#code#>
    }
}
```

The schema supports the following system experiences:

- Siri
- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [`Getting started with the App Intents framework`](getting-started-with-the-app-intents-framework.md).

## See Also

- [var addToLibrary: some AppSchemaIntent](appschema/audiointent/addtolibrary.md)
  An intent schema that adds an audio item to the person’s library.
- [var addToPlaylist: some AppSchemaIntent](appschema/audiointent/addtoplaylist.md)
  An intent schema that adds an audio item to a playlist.
- [var createStation: some AppSchemaIntent](appschema/audiointent/createstation.md)
  An intent schema that starts a station based on the now-playing item.
- [var recognizeAudio: some AppSchemaIntent](appschema/audiointent/recognizeaudio.md)
  An intent schema that finds out what audio is playing nearby.
- [var updateAudioAffinity: some AppSchemaIntent](appschema/audiointent/updateaudioaffinity.md)
  An intent schema that sets the like state of an audio item to liked, unliked, or unset.
- [var warmupAudioQueue: some AppSchemaIntent](appschema/audiointent/warmupaudioqueue.md)
  An intent schema that warms up an audio item by setting the queue without starting playback.
- [AppSchema.AudioIntent](appschema/audiointent.md)
  Identifies intent schemas in the audio domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/audiointent/playaudio)*