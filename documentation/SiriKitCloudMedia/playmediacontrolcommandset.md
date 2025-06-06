# PlayMediaControlCommandSet

**Framework**: SiriKit Cloud Media  
**Kind**: dictionary

A set of modifications to apply to the default set of available playback controls.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```swift
object PlayMediaControlCommandSet
```

#### Discussion

Provide `true` to enable a control that isn’t available by default in the current [`PlayMediaControlScheme`](playmediacontrolscheme.md), and `false` to disable a control that’s available by default in the `PlayMediaControlScheme`. Omit entries for any controls that need to respect the default behavior of the current scheme.

When the user interacts with these controls, the client sends that information to the [`Report Playback Progress and Activity`](updateactivity.md) endpoint. This is separate from the user telling Siri they like some content, which the client sends to the [`Process an Update Media Affinity Intent`](updatemediaaffinity.md) endpoint.

## See Also

- [object QueueControlMapping](queuecontrolmapping.md)
  A dictionary of configuration names and the media controls they permit.
- [object PlayMediaControl](playmediacontrol.md)
  A configuration for permitted user interactions and other player behaviors during playback.
- [type PlayMediaControlScheme](playmediacontrolscheme.md)
  Default playback controls and settings for common content types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/playmediacontrolcommandset)*