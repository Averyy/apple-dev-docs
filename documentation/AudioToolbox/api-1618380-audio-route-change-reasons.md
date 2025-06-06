# Audio Route Change Reasons

**Framework**: Audio Toolbox

Identifiers for the various reasons that an audio route can change while your app is running.

#### Overview

You encounter these identifiers as values in the [`CFDictionary`](https://developer.apple.com/documentation/CoreFoundation/CFDictionary) object passed to your property listener callback function when it is listening for audio route changes. See the description for [`kAudioSessionProperty_AudioRouteChange`](kaudiosessionproperty_audioroutechange.md).

## Topics

### Constants
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
- [var kAudioSessionRouteChangeReason_NoSuitableRouteForCategory: Int](kaudiosessionroutechangereason_nosuitablerouteforcategory.md)
  There is no audio hardware route for the audio session category.
- [var kAudioSessionRouteChangeReason_RouteConfigurationChange: Int](kaudiosessionroutechangereason_routeconfigurationchange.md)

## See Also

- [Audio Route Description Dictionary Keys](audio-route-description-dictionary-keys.md)
  Keys for the [`kAudioSessionProperty_AudioRouteDescription`](kaudiosessionproperty_audioroutedescription.md) dictionary.
- [Audio Route Type Key](audio-route-type-key.md)
  The one key for an audio route input or output dictionary.
- [Audio Input Routes](audio-input-routes.md)
  Strings that identify the various audio input sources for a device.
- [Audio Output Routes](audio-output-routes.md)
  The various audio output destinations available for an iOS device.
- [Audio Route Change Dictionary Keys](audio-route-change-dictionary-keys.md)
  Keys for obtaining information about an audio hardware route change.
- [Alternative Audio Route Change Reason Dictionary Key](alternative-audio-route-change-reason-dictionary-key.md)
  An alternate key for obtaining information about the reason for an audio route change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/1618380-audio-route-change-reasons)*