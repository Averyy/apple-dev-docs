# PlayMediaIntent

**Framework**: SiriKit Cloud Media  
**Kind**: dictionary

An object that describes the user’s request to play a media item.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```swift
object PlayMediaIntent
```

## Properties

- `class` (string): The specific type of intent.
- `mediaItems` ([MediaItem]): Particular pieces of media, such as songs, albums, or playlists, to play. In a `resolveMediaItems` request, this value is generally empty. Your service responds with a [`PlayMediaIntentHandlingResolveMediaItemsInvocationResponse`](playmediaintenthandlingresolvemediaitemsinvocationresponse.md) that contains an array of [`MediaItem`](mediaitem.md) results, with the most relevant one first. On subsequent requests to process this intent, this value contains that array.
- `mediaSearch` (MediaSearch): Search parameters that describe the media items the user wants to play.
- `playbackQueueLocation` (PlaybackQueueLocation): The position within the queue to play the requested media items.
- `playbackRepeatMode` (PlaybackRepeatMode): A value that indicates whether to play one or all of the media items more than once. If your service supports repeat modes, repeat the content within the queue you provide. The client doesn’t replay queue segments.
- `playbackSpeed` (double): The rate for the media items to play, relative to normal speed. The default value of this property is `1.0`. The user can request a different playback speed with several Siri utterances, such as “Play slower” or “Play double speed.” However, the client always plays content at the normal speed, as if this value is `1.0`.
- `playShuffled` (boolean): A Boolean value that indicates whether to randomize the order of media items during playback.
- `resumePlayback` (boolean): A Boolean that indicates whether to continue paused content, or to start at the beginning of the requested media item.

## Relationships

### Inherits From
- [Intent](intent.md)

## See Also

- [object PlayMediaIntentHandlingInvocation](playmediaintenthandlinginvocation.md)
  A request to process a play media intent.
- [type PlayMediaIntentHandlingInvocationResponse](playmediaintenthandlinginvocationresponse.md)
  The service’s response to a request to process a play media intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/playmediaintent)*