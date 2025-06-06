# Audio Input Routes

**Framework**: Audio Toolbox

Strings that identify the various audio input sources for a device.

#### Overview

These strings are used as values for the [`kAudioSession_AudioRouteKey_Type`](kaudiosession_audioroutekey_type.md) key for the dictionary associated with the [`kAudioSession_AudioRouteKey_Inputs`](kaudiosession_audioroutekey_inputs.md) array.

## Topics

### Constants
- [let kAudioSessionInputRoute_LineIn: CFString!](kaudiosessioninputroute_linein.md)
  A line in input
- [let kAudioSessionInputRoute_BuiltInMic: CFString!](kaudiosessioninputroute_builtinmic.md)
  A built-in microphone input.
- [let kAudioSessionInputRoute_HeadsetMic: CFString!](kaudiosessioninputroute_headsetmic.md)
  A microphone that is part of a headset.
- [let kAudioSessionInputRoute_BluetoothHFP: CFString!](kaudiosessioninputroute_bluetoothhfp.md)
  A microphone that is part of a Bluetooth Hands-Free Profile (HFP) device.
- [let kAudioSessionInputRoute_USBAudio: CFString!](kaudiosessioninputroute_usbaudio.md)
  A Universal Serial Bus (USB) input, accessed through the device 30-pin connector.

## See Also

- [Audio Route Change Reasons](1618380-audio-route-change-reasons.md)
  Identifiers for the various reasons that an audio route can change while your app is running.
- [Audio Route Description Dictionary Keys](audio-route-description-dictionary-keys.md)
  Keys for the [`kAudioSessionProperty_AudioRouteDescription`](kaudiosessionproperty_audioroutedescription.md) dictionary.
- [Audio Route Type Key](audio-route-type-key.md)
  The one key for an audio route input or output dictionary.
- [Audio Output Routes](audio-output-routes.md)
  The various audio output destinations available for an iOS device.
- [Audio Route Change Dictionary Keys](audio-route-change-dictionary-keys.md)
  Keys for obtaining information about an audio hardware route change.
- [Alternative Audio Route Change Reason Dictionary Key](alternative-audio-route-change-reason-dictionary-key.md)
  An alternate key for obtaining information about the reason for an audio route change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audio-input-routes)*