# SetPanningChannels

**Framework**: AudioDriverKit  
**Kind**: method

Sets the current stereo panning channels.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
kern_return_t SetPanningChannels(IOUserAudioObjectPropertyElement in_left_channel, IOUserAudioObjectPropertyElement in_right_channel);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. For a list of error codes, see [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

If successful, changing the panning channels sends a notification to the host to update the object state.

This method synchronizes by using the work queue created by the object.

## Parameters

- `in_left_channel`: The   for the left channel.
- `in_right_channel`: The   for the right channel.

## See Also

- [SetControlValue](iouseraudiostereopancontrol/setcontrolvalue.md)
  Sets the stereo pan value of the control.
- [GetControlValue](iouseraudiostereopancontrol/getcontrolvalue.md)
  Gets the floating-point stereo pan value of the control.
- [GetPanningChannels](iouseraudiostereopancontrol/getpanningchannels.md)
  Gets the current stereo panning channels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiostereopancontrol/setpanningchannels)*