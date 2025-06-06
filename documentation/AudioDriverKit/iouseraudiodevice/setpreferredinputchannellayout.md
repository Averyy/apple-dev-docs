# SetPreferredInputChannelLayout

**Framework**: AudioDriverKit  
**Kind**: method

Sets the input channel layout, using an array of audio channel label values.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
kern_return_t SetPreferredInputChannelLayout(IOUserAudioChannelLabel * in_channel_labels, size_t in_num_channels);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. For a list of error codes, see [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

## Parameters

- `in_channel_labels`: An array of   values.
- `in_num_channels`: The number of items in the   array.

## See Also

- [SetPreferredChannelsForStereo](iouseraudiodevice/setpreferredchannelsforstereo.md)
  Sets the channel indices for the prefered stereo pair.
- [GetPreferredChannelsForStereo](iouseraudiodevice/getpreferredchannelsforstereo.md)
  Returns the channel indices for the prefered stereo pair.
- [SetPreferredOutputChannelLayout](iouseraudiodevice/setpreferredoutputchannellayout.md)
  Sets the output channel layout, using an array of audio channel label values.
- [IOUserAudioChannelLabel](audiodriverkit/iouseraudiochannellabel.md)
  Constants to set the preferred channel layout on an audio device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiodevice/setpreferredinputchannellayout)*