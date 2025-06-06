# Audio Graph Errors

**Framework**: Audio Toolbox

## Topics

### Constants
- [var kAUGraphErr_CannotDoInCurrentContext: OSStatus](kaugrapherr_cannotdoincurrentcontext.md)
  To avoid spinning or waiting in the render thread (a bad idea!), many of the calls to AUGraph can return: `kAUGraphErr_CannotDoInCurrentContext`. This result is only generated when you call an AUGraph API from its render callback. It means that the lock that it required was held at that time, by another thread. If you see this result code, you can generally attempt the action again - typically the NEXT render cycle (so in the mean time the lock can be cleared), or you can delegate that call to another thread in your app. You should not spin or put-to-sleep the render thread.
- [var kAUGraphErr_InvalidAudioUnit: OSStatus](kaugrapherr_invalidaudiounit.md)
- [var kAUGraphErr_InvalidConnection: OSStatus](kaugrapherr_invalidconnection.md)
  The attempted connection between two nodes cannot be made.
- [var kAUGraphErr_NodeNotFound: OSStatus](kaugrapherr_nodenotfound.md)
  The specified node cannot be found.
- [var kAUGraphErr_OutputNodeErr: OSStatus](kaugrapherr_outputnodeerr.md)
  Audio processing graphs can only contain one output unit. This error is returned if trying to add a second output unit or if the graph’s output unit is removed while the graph is running.

## See Also

- [Audio Unit Attenuation Properties](1534112-audio-unit-attenuation-propertie.md)
- [Audio Unit Instrument Errors](1584141-audio-unit-instrument-errors.md)
- [Anonymous](1534019-anonymous.md)
- [Anonymous](1534074-anonymous.md)
- [Audio Converter Property ID](1624333-audio-converter-property-id.md)
- [Anonymous](1621044-anonymous.md)
- [Anonymous](1618426-anonymous.md)
- [Anonymous](1618742-anonymous.md)
- [Anonymous](1619479-anonymous.md)
- [Anonymous](1619504-anonymous.md)
- [Anonymous](1533960-anonymous.md)
- [Anonymous](1534225-anonymous.md)
- [Music Device Properties](1534089-music-device-properties.md)
- [3D Mixer Audio Unit Properties](1534063-3d_mixer_audio_unit_properties.md)
  Properties for the Apple 3D Mixer audio unit.
- [var kAudioSession_AudioRouteChangeKey_OldRoute: String](kaudiosession_audioroutechangekey_oldroute.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/1537630-audio-graph-errors)*