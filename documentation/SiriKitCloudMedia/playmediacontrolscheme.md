# PlayMediaControlScheme

**Framework**: SiriKit Cloud Media  
**Kind**: typealias  
**Role**: Type

Default playback controls and settings for common content types.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```
string PlayMediaControlScheme
```

## Possible Values

- `onDemand`: Enables `nextTrack`, `previousTrack`, `skipForward`, `skipBackward`, and `seekToPlaybackPosition` by default.
- `internetRadio`: No controls are available by default. You may enable `nextTrack`, `previousTrack`, and `seekToPlaybackPosition`. This scheme also respects a queue’s `skipsRemaining` count.
- `liveStreaming`: No controls are available by default. You may enable `skipForward`, `skipBackward`, and `seekToPlaybackPosition`.
- `audioBook`: Enables `skipForward`, `skipBackward`, and `seekToPlaybackPosition` by default. You may enable `nextTrack` and `previousTrack`.
- `podcast`: Enables `skipForward`, `skipBackward`, and `seekToPlaybackPosition` by default. You may enable `nextTrack` and `previousTrack`.
- `advertisement`: No controls are available by default. You may enable `nextTrack`, `previousTrack`, `skipForward`, `skipBackward`, and `seekToPlaybackPosition`. If the user attempts to use one of these controls and it isn’t available, Siri informs the user that they can’t use the control because of the advertisement.
- `custom`: No controls are available by default. You may enable `nextTrack`, `previousTrack`, `skipForward`, `skipBackward`, and `seekToPlaybackPosition`.

## Discussion

The controls for `likeTrack`, `dislikeTrack`, and `bookmarkTrack` aren’t available by default for any of these schemes. You may enable them in any control scheme except for `internetRadio`.

## See Also

### Customizing Playback Controls
- [object QueueControlMapping](./queuecontrolmapping.md)
  A dictionary of configuration names and the media controls they permit.
- [object PlayMediaControl](./playmediacontrol.md)
  A configuration for permitted user interactions and other player behaviors during playback.
- [object PlayMediaControlCommandSet](./playmediacontrolcommandset.md)
  A set of modifications to apply to the default set of available playback controls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/playmediacontrolscheme)*