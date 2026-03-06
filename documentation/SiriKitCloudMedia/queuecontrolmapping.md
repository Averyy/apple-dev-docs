# QueueControlMapping

**Framework**: SiriKit Cloud Media  
**Kind**: dictionary

A dictionary of configuration names and the media controls they permit.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```swift
object QueueControlMapping
```

## Properties

- `default` (PlayMediaControl) *(required)*: The default playback control configuration to use for content that doesn’t specify a different control scheme.
- `Any Key` (PlayMediaControl): A playback control configuration with a name you define that [`Content`](content.md) objects can refer to.

## See Also

- [object PlayMediaControl](playmediacontrol.md)
  A configuration for permitted user interactions and other player behaviors during playback.
- [type PlayMediaControlScheme](playmediacontrolscheme.md)
  Default playback controls and settings for common content types.
- [object PlayMediaControlCommandSet](playmediacontrolcommandset.md)
  A set of modifications to apply to the default set of available playback controls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/queuecontrolmapping)*