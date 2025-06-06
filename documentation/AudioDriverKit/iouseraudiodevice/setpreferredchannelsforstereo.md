# SetPreferredChannelsForStereo

**Framework**: AudioDriverKit  
**Kind**: method

Sets the channel indices for the prefered stereo pair.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
kern_return_t SetPreferredChannelsForStereo(uint32_t in_left_channel, uint32_t in_right_channel);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. For a list of error codes, see [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

## Parameters

- `in_left_channel`: The channel index for the left channel.
- `in_right_channel`: The channel index for the right channel.

## See Also

- [GetPreferredChannelsForStereo](iouseraudiodevice/getpreferredchannelsforstereo.md)
  Returns the channel indices for the prefered stereo pair.
- [SetPreferredInputChannelLayout](iouseraudiodevice/setpreferredinputchannellayout.md)
  Sets the input channel layout, using an array of audio channel label values.
- [SetPreferredOutputChannelLayout](iouseraudiodevice/setpreferredoutputchannellayout.md)
  Sets the output channel layout, using an array of audio channel label values.
- [IOUserAudioChannelLabel](audiodriverkit/iouseraudiochannellabel.md)
  Constants to set the preferred channel layout on an audio device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiodevice/setpreferredchannelsforstereo)*