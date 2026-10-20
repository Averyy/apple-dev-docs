# TalkbackControl

**Framework**: AudioDriverKit  
**Kind**: case

The identifier for the audio talkback control class.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
TalkbackControl
```

#### Discussion

This class is a subclass of the [`IOUserAudioBooleanControl`](iouseraudiobooleancontrol.md) class where a `true` value indcates an enabled talkback channel. This control is for talkback channels outside of the regular I/O channels. If the talkback channel is among the normal I/O channels, it uses [`MuteControl`](audiodriverkit/iouseraudioclassid/mutecontrol.md).

## See Also

- [BooleanControl](audiodriverkit/iouseraudioclassid/booleancontrol.md)
  The identifier for the audio Boolean control class.
- [LFEMuteControl](audiodriverkit/iouseraudioclassid/lfemutecontrol.md)
  The identifier for the low-frequency effect mute control class.
- [SoloControl](audiodriverkit/iouseraudioclassid/solocontrol.md)
  The identifier for the audio solo control class.
- [JackControl](audiodriverkit/iouseraudioclassid/jackcontrol.md)
  The identifier for the audio jack control class.
- [PhantomPowerControl](audiodriverkit/iouseraudioclassid/phantompowercontrol.md)
  The identifier for the audio phantom power control class.
- [PhaseInvertControl](audiodriverkit/iouseraudioclassid/phaseinvertcontrol.md)
  The identifier for the audio phase invert control class.
- [ClipLightControl](audiodriverkit/iouseraudioclassid/cliplightcontrol.md)
  The identifier for the audio clip light control class.
- [ListenbackControl](audiodriverkit/iouseraudioclassid/listenbackcontrol.md)
  The identifier for the audio listenback control class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/audiodriverkit/iouseraudioclassid/talkbackcontrol)*