# AppSchema.AudioIntent

**Framework**: App Intents  
**Kind**: protocol

Identifies intent schemas in the audio domain.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
protocol AudioIntent : AppSchema.Kind
```

## Topics

### Instance Properties
- [var addToLibrary: some AppSchemaIntent](appschema/audiointent/addtolibrary.md)
  An intent schema that adds an audio item to the person’s library.
- [var addToPlaylist: some AppSchemaIntent](appschema/audiointent/addtoplaylist.md)
  An intent schema that adds an audio item to a playlist.
- [var createStation: some AppSchemaIntent](appschema/audiointent/createstation.md)
  An intent schema that starts a station based on the now-playing item.
- [var playAudio: some AppSchemaIntent](appschema/audiointent/playaudio.md)
  An intent schema that plays an audio item.
- [var recognizeAudio: some AppSchemaIntent](appschema/audiointent/recognizeaudio.md)
  An intent schema that finds out what audio is playing nearby.
- [var updateAudioAffinity: some AppSchemaIntent](appschema/audiointent/updateaudioaffinity.md)
  An intent schema that sets the like state of an audio item to liked, unliked, or unset.
- [var warmupAudioQueue: some AppSchemaIntent](appschema/audiointent/warmupaudioqueue.md)
  An intent schema that warms up an audio item by setting the queue without starting playback.

## Relationships

### Inherits From
- [AppSchema.Kind](appschema/kind.md)
### Conforming Types
- [AppSchema.Intent](appschema/intent.md)

## See Also

- [var addToLibrary: some AppSchemaIntent](appschema/audiointent/addtolibrary.md)
  An intent schema that adds an audio item to the person’s library.
- [var addToPlaylist: some AppSchemaIntent](appschema/audiointent/addtoplaylist.md)
  An intent schema that adds an audio item to a playlist.
- [var createStation: some AppSchemaIntent](appschema/audiointent/createstation.md)
  An intent schema that starts a station based on the now-playing item.
- [var playAudio: some AppSchemaIntent](appschema/audiointent/playaudio.md)
  An intent schema that plays an audio item.
- [var recognizeAudio: some AppSchemaIntent](appschema/audiointent/recognizeaudio.md)
  An intent schema that finds out what audio is playing nearby.
- [var updateAudioAffinity: some AppSchemaIntent](appschema/audiointent/updateaudioaffinity.md)
  An intent schema that sets the like state of an audio item to liked, unliked, or unset.
- [var warmupAudioQueue: some AppSchemaIntent](appschema/audiointent/warmupaudioqueue.md)
  An intent schema that warms up an audio item by setting the queue without starting playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/audiointent)*