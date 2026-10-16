# spatialPlaybackCapabilitiesChangedNotification

**Framework**: AVFAudio  
**Kind**: property

A notification the system posts when its spatial playback capabilities change.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
class let spatialPlaybackCapabilitiesChangedNotification: NSNotification.Name
```

#### Discussion

The system posts this notification when spatial playback capabilities change due to a change in user preference.

The `userInfo` dictionary of this notification contains the [`AVAudioSessionSpatialAudioEnabledKey`](avaudiosessionspatialaudioenabledkey.md) key, which indicates whether spatial audio is in an enabled state.

A route change may result in a change in the ability for the system to play spatial audio, so observe [`routeChangeNotification`](avaudiosession/routechangenotification.md) and use the [`isSpatialAudioEnabled`](avaudiosessionportdescription/isspatialaudioenabled.md) property to check if the current route supports spatialized playback.

## Topics

### User info keys
- [let AVAudioSessionSpatialAudioEnabledKey: String](avaudiosessionspatialaudioenabledkey.md)
  A user info key that you use to retrieve the state of spatial playback.

## See Also

- [var renderingMode: AVAudioSession.RenderingMode](avaudiosession/renderingmode-swift.property.md)
  The current audio session’s rendering mode.
- [AVAudioSession.RenderingMode](avaudiosession/renderingmode-swift.enum.md)
  Audio session rendering mode identifiers.
- [class let renderingModeChangeNotification: NSNotification.Name](avaudiosession/renderingmodechangenotification.md)
  A notification the system posts when the rendering mode changes.
- [var supportedOutputChannelLayouts: [AVAudioChannelLayout]](avaudiosession/supportedoutputchannellayouts.md)
  The array of channel layouts that the current route supports.
- [class let renderingCapabilitiesChangeNotification: NSNotification.Name](avaudiosession/renderingcapabilitieschangenotification.md)
  A notification the system posts when the rendering capabilities change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/spatialplaybackcapabilitieschangednotification)*