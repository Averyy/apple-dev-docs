# PlaybackRepeatMode

**Framework**: SiriKit Cloud Media  
**Kind**: typealias  
**Role**: Type

The possible repeat modes for a media queue.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```
string PlaybackRepeatMode
```

## Possible Values

- `none`: Don’t repeat media items.
- `all`: Repeat all media items within the playback queue.
- `one`: Repeat the current media item.
- `unknown`: An unknown repeat mode.

## See Also

### Resolving the Intended Repeat Mode
- [object PlayMediaIntentHandlingResolvePlaybackRepeatModeInvocationResponse](./playmediaintenthandlingresolveplaybackrepeatmodeinvocationresponse.md)
  Your service’s response to a request to resolve the repeat mode in a play media intent.
- [object PlayMediaIntentHandlingResolvePlaybackRepeatModeInvocationResponse.Result](./playmediaintenthandlingresolveplaybackrepeatmodeinvocationresponse/result-data.dictionary.md)
  The result of resolving the repeat mode for a play media intent.
- [object PlaybackRepeatModeResolutionResult](./playbackrepeatmoderesolutionresult.md)
  Information about whether your service can identify the specified repeat mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/playbackrepeatmode)*