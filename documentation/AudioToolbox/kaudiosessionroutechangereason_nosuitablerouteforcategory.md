# kAudioSessionRouteChangeReason_NoSuitableRouteForCategory

**Framework**: Audio Toolbox  
**Kind**: var

There is no audio hardware route for the audio session category.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

## Declaration

```swift
var kAudioSessionRouteChangeReason_NoSuitableRouteForCategory: Int { get }
```

#### Discussion

For example, the [`kAudioSessionCategory_RecordAudio`](kaudiosessioncategory_recordaudio.md) is set but there is no audio input device.

## See Also

- [var kAudioSessionRouteChangeReason_Unknown: Int](kaudiosessionroutechangereason_unknown.md)
  The audio route changed but the reason is not known.
- [var kAudioSessionRouteChangeReason_NewDeviceAvailable: Int](kaudiosessionroutechangereason_newdeviceavailable.md)
  A new audio hardware device became available; for example, a headset was plugged in.
- [var kAudioSessionRouteChangeReason_OldDeviceUnavailable: Int](kaudiosessionroutechangereason_olddeviceunavailable.md)
  The previously-used audio hardware device is now unavailable; for example, a headset was unplugged.
- [var kAudioSessionRouteChangeReason_CategoryChange: Int](kaudiosessionroutechangereason_categorychange.md)
  The audio session category has changed.
- [var kAudioSessionRouteChangeReason_Override: Int](kaudiosessionroutechangereason_override.md)
  The audio route has been overridden.
- [var kAudioSessionRouteChangeReason_WakeFromSleep: Int](kaudiosessionroutechangereason_wakefromsleep.md)
  The device woke from sleep.
- [var kAudioSessionRouteChangeReason_RouteConfigurationChange: Int](kaudiosessionroutechangereason_routeconfigurationchange.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionroutechangereason_nosuitablerouteforcategory)*