# AppSchema.AudioIntent

**Framework**: App Intents  
**Kind**: protocol  
**Role**: Protocol

Identifies intent schemas in the audio domain.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
protocol AudioIntent : AppSchema.Kind
```

## Topics

### Instance Properties
- [var addToLibrary: some AppSchemaIntent](./audiointent/addtolibrary.md)
  An intent schema that adds an audio item to the person’s library.
- [var addToPlaylist: some AppSchemaIntent](./audiointent/addtoplaylist.md)
  An intent schema that adds an audio item to a playlist.
- [var createStation: some AppSchemaIntent](./audiointent/createstation.md)
  An intent schema that starts a station based on the now-playing item.
- [var playAudio: some AppSchemaIntent](./audiointent/playaudio.md)
  An intent schema that plays an audio item.
- [var recognizeAudio: some AppSchemaIntent](./audiointent/recognizeaudio.md)
  An intent schema that finds out what audio is playing nearby.
- [var updateAudioAffinity: some AppSchemaIntent](./audiointent/updateaudioaffinity.md)
  An intent schema that sets the like state of an audio item to liked, unliked, or unset.
- [var warmupAudioQueue: some AppSchemaIntent](./audiointent/warmupaudioqueue.md)
  An intent schema that warms up an audio item by setting the queue without starting playback.

## Relationships

### Inherits From
- [AppSchema.Kind](./kind.md)
### Conforming Types
- [AppSchema.Intent](./intent.md)

## See Also

### Actions
- [var addToLibrary: some AppSchemaIntent](./audiointent/addtolibrary.md)
  An intent schema that adds an audio item to the person’s library.
- [var addToPlaylist: some AppSchemaIntent](./audiointent/addtoplaylist.md)
  An intent schema that adds an audio item to a playlist.
- [var createStation: some AppSchemaIntent](./audiointent/createstation.md)
  An intent schema that starts a station based on the now-playing item.
- [var playAudio: some AppSchemaIntent](./audiointent/playaudio.md)
  An intent schema that plays an audio item.
- [var recognizeAudio: some AppSchemaIntent](./audiointent/recognizeaudio.md)
  An intent schema that finds out what audio is playing nearby.
- [var updateAudioAffinity: some AppSchemaIntent](./audiointent/updateaudioaffinity.md)
  An intent schema that sets the like state of an audio item to liked, unliked, or unset.
- [var warmupAudioQueue: some AppSchemaIntent](./audiointent/warmupaudioqueue.md)
  An intent schema that warms up an audio item by setting the queue without starting playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/audiointent)*