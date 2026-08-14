# SetPreferredOutputChannelLayout

**Framework**: AudioDriverKit  
**Kind**: method

Sets the output channel layout, using an array of audio channel label values.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
kern_return_t SetPreferredOutputChannelLayout(IOUserAudioChannelLabel *in_channel_labels, size_t in_num_channels);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/driverkit/kioreturnsuccess) on success, or another value if an error occurs. For a list of error codes, see [`Error Codes`](https://developer.apple.com/documentation/driverkit/error-codes).

## Parameters

- `in_channel_labels`: An array of [`IOUserAudioChannelLabel`](audiodriverkit/iouseraudiochannellabel.md) values.
- `in_num_channels`: The number of items in the `in_channel_labels` array.

## See Also

- [SetPreferredChannelsForStereo](iouseraudiodevice/setpreferredchannelsforstereo.md)
  Sets the channel indices for the prefered stereo pair.
- [GetPreferredChannelsForStereo](iouseraudiodevice/getpreferredchannelsforstereo.md)
  Returns the channel indices for the prefered stereo pair.
- [SetPreferredInputChannelLayout](iouseraudiodevice/setpreferredinputchannellayout.md)
  Sets the input channel layout, using an array of audio channel label values.
- [IOUserAudioChannelLabel](audiodriverkit/iouseraudiochannellabel.md)
  Constants to set the preferred channel layout on an audio device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiodevice/setpreferredoutputchannellayout)*