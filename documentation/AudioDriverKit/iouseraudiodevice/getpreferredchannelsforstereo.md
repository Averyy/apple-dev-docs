# GetPreferredChannelsForStereo

**Framework**: AudioDriverKit  
**Kind**: method

Returns the channel indices for the prefered stereo pair.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
void GetPreferredChannelsForStereo(uint32_t * out_left_channel, uint32_t * out_right_channel);
```

## Parameters

- `out_left_channel`: On return, the channel index for the left channel.
- `out_right_channel`: On return, the channel index for the right channel.

## See Also

- [SetPreferredChannelsForStereo](iouseraudiodevice/setpreferredchannelsforstereo.md)
  Sets the channel indices for the prefered stereo pair.
- [SetPreferredInputChannelLayout](iouseraudiodevice/setpreferredinputchannellayout.md)
  Sets the input channel layout, using an array of audio channel label values.
- [SetPreferredOutputChannelLayout](iouseraudiodevice/setpreferredoutputchannellayout.md)
  Sets the output channel layout, using an array of audio channel label values.
- [IOUserAudioChannelLabel](audiodriverkit/iouseraudiochannellabel.md)
  Constants to set the preferred channel layout on an audio device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiodevice/getpreferredchannelsforstereo)*