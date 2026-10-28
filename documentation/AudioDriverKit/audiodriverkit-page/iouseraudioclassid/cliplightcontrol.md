# ClipLightControl

**Framework**: AudioDriverKit  
**Kind**: case  
**Role**: Enumeration Case

The identifier for the audio clip light control class.

**Availability**:
- DriverKit 21.0+

## Declaration

```c
ClipLightControl
```

## Discussion

This class is a subclass of the `IOUserAudioBooleanControl` class where a true value indcates the signal for the element has exceeded the sample range. After a clip light turns on, it stays on until either:

A `SetControlValue` call sets the value to `false`.

The current IO session stops and a new IO session starts.

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
- [TalkbackControl](./talkbackcontrol.md)
  The identifier for the audio talkback control class.
- [ListenbackControl](./listenbackcontrol.md)
  The identifier for the audio listenback control class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/audiodriverkit/iouseraudioclassid/cliplightcontrol)*