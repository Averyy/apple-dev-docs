# ListenbackControl

**Framework**: AudioDriverKit  
**Kind**: case  
**Role**: Enumeration Case

The identifier for the audio listenback control class.

**Availability**:
- DriverKit 21.0+

## Declaration

```c
ListenbackControl
```

#### Discussion

This class is a subclass of the [`IOUserAudioBooleanControl`](../../iouseraudiobooleancontrol.md) class where a `true` value indcates an enabled listenback channel. This control is for listenback channels outside of the regular I/O channels. If the listenback channel is among the normal I/O channels, it uses [`MuteControl`](./mutecontrol.md).

## See Also

### Boolean Controls
- [BooleanControl](./booleancontrol.md)
  The identifier for the audio Boolean control class.
- [LFEMuteControl](./lfemutecontrol.md)
  The identifier for the low-frequency effect mute control class.
- [SoloControl](./solocontrol.md)
  The identifier for the audio solo control class.
- [JackControl](./jackcontrol.md)
  The identifier for the audio jack control class.
- [PhantomPowerControl](./phantompowercontrol.md)
  The identifier for the audio phantom power control class.
- [PhaseInvertControl](./phaseinvertcontrol.md)
  The identifier for the audio phase invert control class.
- [ClipLightControl](./cliplightcontrol.md)
  The identifier for the audio clip light control class.
- [TalkbackControl](./talkbackcontrol.md)
  The identifier for the audio talkback control class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/audiodriverkit/iouseraudioclassid/listenbackcontrol)*