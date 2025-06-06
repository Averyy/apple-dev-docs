# PlayMediaControlScheme

**Framework**: SiriKit Cloud Media  
**Kind**: typealias

Default playback controls and settings for common content types.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```swift
string PlayMediaControlScheme
```

#### Discussion

The controls for `likeTrack`, `dislikeTrack`, and `bookmarkTrack` aren’t available by default for any of these schemes. You may enable them in any control scheme except for `internetRadio`.

## See Also

- [object QueueControlMapping](queuecontrolmapping.md)
  A dictionary of configuration names and the media controls they permit.
- [object PlayMediaControl](playmediacontrol.md)
  A configuration for permitted user interactions and other player behaviors during playback.
- [object PlayMediaControlCommandSet](playmediacontrolcommandset.md)
  A set of modifications to apply to the default set of available playback controls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/playmediacontrolscheme)*