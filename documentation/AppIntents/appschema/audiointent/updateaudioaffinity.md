# updateAudioAffinity

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An intent schema that sets the like state of an audio item to liked, unliked, or unset.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var updateAudioAffinity: some AppSchemaIntent { get }
```

## Discussion

To make your app’s actions available to Apple Intelligence, conform your [`AppIntent`](../../appintent.md) to a schema that describes your action to the system. If your app’s functionality aligns with the `audio` domain and one of your app’s actions matches the `updateAudioAffinity` schema, you can generate the properties and protocol conformance the schema requires for your intent implementation with the `@AppIntent( .audio.updateAudioAffinity)` Swift macro. To make your app work with Siri, see [Apple Intelligence and Siri AI](../../apple-intelligence-and-siri-ai.md).

The following example shows an intent that conforms to the `updateAudioAffinity` schema:

```swift
@AppIntent(schema: .audio.updateAudioAffinity)
struct UpdateAudioAffinityIntent {
    var affinityState: <#AffinityState#>
    var target: <#AudioItem#>

    func perform() async throws -> some IntentResult {
        <#code#>
    }
}
```

Define a `@UnionValue` enumeration for the `target` parameter, as in the following example, by typing the first few characters of `audio_audioItem` in Xcode and selecting it from the code-completion suggestions.

```swift
@UnionValue
enum AudioItem {
    case song(<#SongEntity#>)
    case album(<#AlbumEntity#>)
    case artist(<#ArtistEntity#>)
    case playlist(<#PlaylistEntity#>)
    case songCollection(<#SongCollectionEntity#>)
    case classicalMusicRecording(<#ClassicalMusicRecordingEntity#>)
    case liveRadioStation(<#LiveRadioStationEntity#>)
    case algorithmicRadioStation(<#AlgorithmicRadioStationEntity#>)
    case radioShowEpisode(<#RadioShowEpisodeEntity#>)
    case radioShow(<#RadioShowEntity#>)
    case podcastShow(<#PodcastShowEntity#>)
    case podcastEpisode(<#PodcastEpisodeEntity#>)
    case podcastCollection(<#PodcastCollectionEntity#>)
    case audiobook(<#MediaBookEntity#>)
    case ambientSound(<#AmbientSoundEntity#>)
    case newsBrief(<#NewsBriefEntity#>)
    case newsProvider(<#NewsProviderEntity#>)
}
```

> 💡 **Tip**: Keep the cases that your app supports and remove the rest.

The schema supports the following system experiences:

- Siri
- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [Getting started with the App Intents framework](../../getting-started-with-the-app-intents-framework.md).

## See Also

### Actions
- [var addToLibrary: some AppSchemaIntent](./addtolibrary.md)
  An intent schema that adds an audio item to the person’s library.
- [var addToPlaylist: some AppSchemaIntent](./addtoplaylist.md)
  An intent schema that adds an audio item to a playlist.
- [var createStation: some AppSchemaIntent](./createstation.md)
  An intent schema that starts a station based on the now-playing item.
- [var playAudio: some AppSchemaIntent](./playaudio.md)
  An intent schema that plays an audio item.
- [var recognizeAudio: some AppSchemaIntent](./recognizeaudio.md)
  An intent schema that finds out what audio is playing nearby.
- [var warmupAudioQueue: some AppSchemaIntent](./warmupaudioqueue.md)
  An intent schema that warms up an audio item by setting the queue without starting playback.
- [AppSchema.AudioIntent](../audiointent.md)
  Identifies intent schemas in the audio domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/audiointent/updateaudioaffinity)*