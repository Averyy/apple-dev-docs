# SetPreferredInputChannelLayout

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Sets the input channel layout, using an array of audio channel label values.

**Availability**:
- DriverKit 21.0+

## Declaration

```c
kern_return_t SetPreferredInputChannelLayout(IOUserAudioChannelLabel *in_channel_labels, size_t in_num_channels);
```

## Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. For a list of error codes, see [Error Codes](../../DriverKit/error-codes.md).

## Parameters

- `in_channel_labels`: An array of [`IOUserAudioChannelLabel`](../audiodriverkit-page/iouseraudiochannellabel.md) values.
- `in_num_channels`: The number of items in the `in_channel_labels` array.

## See Also

### Working with Channel Layouts
- [SetPreferredChannelsForStereo](./setpreferredchannelsforstereo.md)
  Sets the channel indices for the prefered stereo pair.
- [GetPreferredChannelsForStereo](./getpreferredchannelsforstereo.md)
  Returns the channel indices for the prefered stereo pair.
- [SetPreferredOutputChannelLayout](./setpreferredoutputchannellayout.md)
  Sets the output channel layout, using an array of audio channel label values.
- [IOUserAudioChannelLabel](../audiodriverkit-page/iouseraudiochannellabel.md)
  Constants to set the preferred channel layout on an audio device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiodevice/setpreferredinputchannellayout)*