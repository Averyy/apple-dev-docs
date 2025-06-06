# LFEMuteControl

**Framework**: AudioDriverKit  
**Kind**: case

The identifier for the low-frequency effect mute control class.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
LFEMuteControl
```

#### Discussion

This class is a subclass of the [`IOUserAudioBooleanControl`](iouseraudiobooleancontrol.md) class, where `true` means that the LFE channel that results from bass management isn’t audible. If you use normal audio channels to represent LFE channels, you must use the [`VolumeControl`](audiodriverkit/iouseraudioclassid/volumecontrol.md) class to manipulate the level.

## See Also

- [BooleanControl](audiodriverkit/iouseraudioclassid/booleancontrol.md)
  The identifier for the audio Boolean control class.
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
- [TalkbackControl](audiodriverkit/iouseraudioclassid/talkbackcontrol.md)
  The identifier for the audio talkback control class.
- [ListenbackControl](audiodriverkit/iouseraudioclassid/listenbackcontrol.md)
  The identifier for the audio listenback control class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/audiodriverkit/iouseraudioclassid/lfemutecontrol)*