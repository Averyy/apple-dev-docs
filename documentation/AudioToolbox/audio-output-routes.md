# Audio Output Routes

**Framework**: Audio Toolbox

The various audio output destinations available for an iOS device.

#### Overview

These strings are used as values for the [`kAudioSession_AudioRouteKey_Type`](kaudiosession_audioroutekey_type.md) key for the dictionary associated with the [`kAudioSession_AudioRouteKey_Outputs`](kaudiosession_audioroutekey_outputs.md) array.

## Topics

### Constants
- [let kAudioSessionOutputRoute_LineOut: CFString!](kaudiosessionoutputroute_lineout.md)
  Analog line-level output.
- [let kAudioSessionOutputRoute_Headphones: CFString!](kaudiosessionoutputroute_headphones.md)
  Speakers in headphones or in a headset.
- [let kAudioSessionOutputRoute_BluetoothHFP: CFString!](kaudiosessionoutputroute_bluetoothhfp.md)
  Speakers that are part of a Bluetooth Hands-Free Profile (HFP) accessory.
- [let kAudioSessionOutputRoute_BluetoothA2DP: CFString!](kaudiosessionoutputroute_bluetootha2dp.md)
  Speakers in a Bluetooth A2DP device.
- [let kAudioSessionOutputRoute_BuiltInReceiver: CFString!](kaudiosessionoutputroute_builtinreceiver.md)
  The built-in speaker you hold to your ear when on a phone call.
- [let kAudioSessionOutputRoute_BuiltInSpeaker: CFString!](kaudiosessionoutputroute_builtinspeaker.md)
  The primary built-in speaker.
- [let kAudioSessionOutputRoute_USBAudio: CFString!](kaudiosessionoutputroute_usbaudio.md)
  Speaker(s) in a Universal Serial Bus (USB) accessory, accessed through the device 30-pin connector.
- [let kAudioSessionOutputRoute_HDMI: CFString!](kaudiosessionoutputroute_hdmi.md)
  An output available through the HDMI interface.
- [let kAudioSessionOutputRoute_AirPlay: CFString!](kaudiosessionoutputroute_airplay.md)
  An output on an AirPlay device.

## See Also

- [Audio Route Change Reasons](1618380-audio-route-change-reasons.md)
  Identifiers for the various reasons that an audio route can change while your app is running.
- [Audio Route Description Dictionary Keys](audio-route-description-dictionary-keys.md)
  Keys for the [`kAudioSessionProperty_AudioRouteDescription`](kaudiosessionproperty_audioroutedescription.md) dictionary.
- [Audio Route Type Key](audio-route-type-key.md)
  The one key for an audio route input or output dictionary.
- [Audio Input Routes](audio-input-routes.md)
  Strings that identify the various audio input sources for a device.
- [Audio Route Change Dictionary Keys](audio-route-change-dictionary-keys.md)
  Keys for obtaining information about an audio hardware route change.
- [Alternative Audio Route Change Reason Dictionary Key](alternative-audio-route-change-reason-dictionary-key.md)
  An alternate key for obtaining information about the reason for an audio route change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audio-output-routes)*