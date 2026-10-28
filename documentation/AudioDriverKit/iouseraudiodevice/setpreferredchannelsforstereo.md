# SetPreferredChannelsForStereo

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Sets the channel indices for the prefered stereo pair.

**Availability**:
- DriverKit 21.0+

## Declaration

```c
kern_return_t SetPreferredChannelsForStereo(uint32_t in_left_channel, uint32_t in_right_channel);
```

## Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. For a list of error codes, see [Error Codes](../../DriverKit/error-codes.md).

## Parameters

- `in_left_channel`: The channel index for the left channel.
- `in_right_channel`: The channel index for the right channel.

## See Also

### Working with Channel Layouts
- [GetPreferredChannelsForStereo](./getpreferredchannelsforstereo.md)
  Returns the channel indices for the prefered stereo pair.
- [SetPreferredInputChannelLayout](./setpreferredinputchannellayout.md)
  Sets the input channel layout, using an array of audio channel label values.
- [SetPreferredOutputChannelLayout](./setpreferredoutputchannellayout.md)
  Sets the output channel layout, using an array of audio channel label values.
- [IOUserAudioChannelLabel](../audiodriverkit-page/iouseraudiochannellabel.md)
  Constants to set the preferred channel layout on an audio device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiodevice/setpreferredchannelsforstereo)*