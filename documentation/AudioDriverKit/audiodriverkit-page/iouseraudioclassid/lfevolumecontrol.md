# LFEVolumeControl

**Framework**: AudioDriverKit  
**Kind**: case

The identifier for the low-frequency effect volume control class.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
LFEVolumeControl
```

#### Discussion

This class is a subclass of the [`IOUserAudioLevelControl`](iouseraudiolevelcontrol.md) class for an LFE channel that results from bass management. If you use normal audio channels to represent LFE channels, you must use the [`VolumeControl`](audiodriverkit/iouseraudioclassid/volumecontrol.md) class to manipulate the level.

## See Also

- [LevelControl](audiodriverkit/iouseraudioclassid/levelcontrol.md)
  The identifier for the audio level control class.
- [VolumeControl](audiodriverkit/iouseraudioclassid/volumecontrol.md)
  The identifier for the audio volume control class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/audiodriverkit/iouseraudioclassid/lfevolumecontrol)*