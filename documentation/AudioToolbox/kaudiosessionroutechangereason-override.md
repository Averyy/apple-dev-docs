# kAudioSessionRouteChangeReason_Override

**Framework**: Audio Toolbox  
**Kind**: var

The audio route has been overridden.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

## Declaration

```swift
var kAudioSessionRouteChangeReason_Override: Int { get }
```

#### Discussion

For example, while using the [`kAudioSessionCategory_PlayAndRecord`](kaudiosessioncategory_playandrecord.md) category, output audio has been redirected to the speaker using the [`kAudioSessionProperty_OverrideAudioRoute`](kaudiosessionproperty_overrideaudioroute.md) property.

## See Also

- [var kAudioSessionRouteChangeReason_Unknown: Int](kaudiosessionroutechangereason_unknown.md)
  The audio route changed but the reason is not known.
- [var kAudioSessionRouteChangeReason_NewDeviceAvailable: Int](kaudiosessionroutechangereason_newdeviceavailable.md)
  A new audio hardware device became available; for example, a headset was plugged in.
- [var kAudioSessionRouteChangeReason_OldDeviceUnavailable: Int](kaudiosessionroutechangereason_olddeviceunavailable.md)
  The previously-used audio hardware device is now unavailable; for example, a headset was unplugged.
- [var kAudioSessionRouteChangeReason_CategoryChange: Int](kaudiosessionroutechangereason_categorychange.md)
  The audio session category has changed.
- [var kAudioSessionRouteChangeReason_WakeFromSleep: Int](kaudiosessionroutechangereason_wakefromsleep.md)
  The device woke from sleep.
- [var kAudioSessionRouteChangeReason_NoSuitableRouteForCategory: Int](kaudiosessionroutechangereason_nosuitablerouteforcategory.md)
  There is no audio hardware route for the audio session category.
- [var kAudioSessionRouteChangeReason_RouteConfigurationChange: Int](kaudiosessionroutechangereason_routeconfigurationchange.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionroutechangereason_override)*