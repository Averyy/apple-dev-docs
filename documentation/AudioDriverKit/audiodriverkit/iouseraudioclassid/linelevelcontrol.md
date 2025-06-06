# LineLevelControl

**Framework**: AudioDriverKit  
**Kind**: case

The identifier for the audio line level control class.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
LineLevelControl
```

#### Discussion

This class is a subclass of the [`IOUserAudioSelectorControl`](iouseraudioselectorcontrol.md) class that identifies the nominal line level for the element. This control isn’t a gain stage, but instead indicates the voltage standard (if any) used for the element, such as +4dBu, -10dBV, instrument, and so on.

## See Also

- [SelectorControl](audiodriverkit/iouseraudioclassid/selectorcontrol.md)
  The identifier for the audio selector control class.
- [DataDestinationControl](audiodriverkit/iouseraudioclassid/datadestinationcontrol.md)
  The identifier for the audio data destination control class.
- [DataSourceControl](audiodriverkit/iouseraudioclassid/datasourcecontrol.md)
  The identifier for the audio data source control class.
- [ClockSourceControl](audiodriverkit/iouseraudioclassid/clocksourcecontrol.md)
  The identifier for the audio clock source control class.
- [HighPassFilterControl](audiodriverkit/iouseraudioclassid/highpassfiltercontrol.md)
  The identifier for the audio high pass filter control class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/audiodriverkit/iouseraudioclassid/linelevelcontrol)*