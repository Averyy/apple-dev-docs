# PlaybackQueueLocation

**Framework**: SiriKit Cloud Media  
**Kind**: typealias  
**Role**: Type

Possible locations in a playback queue to insert a media item.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```
string PlaybackQueueLocation
```

## Possible Values

- `now`: Play the media item immediately, interrupting any current playback.
- `next`: Play the media item after the current item finishes.
- `later`: Add the media item to the end of the current playback queue.
- `unknown`: An unknown playback queue location.

## See Also

### Resolving the Intended Queue Location
- [object PlayMediaIntentHandlingResolvePlaybackQueueLocationInvocationResponse](./playmediaintenthandlingresolveplaybackqueuelocationinvocationresponse.md)
  Your service’s response to a request to resolve the queue location in a play media intent.
- [object PlaybackQueueLocationResolutionResult](./playbackqueuelocationresolutionresult.md)
  Information about whether your service can resolve the specified queue location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/playbackqueuelocation)*