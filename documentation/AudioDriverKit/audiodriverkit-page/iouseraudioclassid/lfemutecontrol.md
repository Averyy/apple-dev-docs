# LFEMuteControl

**Framework**: AudioDriverKit  
**Kind**: case  
**Role**: Enumeration Case

The identifier for the low-frequency effect mute control class.

**Availability**:
- DriverKit 21.0+

## Declaration

```c
LFEMuteControl
```

## Discussion

This class is a subclass of the [`IOUserAudioBooleanControl`](../../iouseraudiobooleancontrol.md) class, where `true` means that the LFE channel that results from bass management isn’t audible. If you use normal audio channels to represent LFE channels, you must use the [`VolumeControl`](./volumecontrol.md) class to manipulate the level.

## See Also

### Boolean Controls
- [BooleanControl](./booleancontrol.md)
  The identifier for the audio Boolean control class.
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
- [ListenbackControl](./listenbackcontrol.md)
  The identifier for the audio listenback control class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/audiodriverkit/iouseraudioclassid/lfemutecontrol)*