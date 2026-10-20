# SetPanningChannels

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Sets the current stereo panning channels.

**Availability**:
- DriverKit 21.0+

## Declaration

```c
kern_return_t SetPanningChannels(IOUserAudioObjectPropertyElement in_left_channel, IOUserAudioObjectPropertyElement in_right_channel);
```

#### Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. For a list of error codes, see [Error Codes](../../DriverKit/error-codes.md).

#### Discussion

If successful, changing the panning channels sends a notification to the host to update the object state.

This method synchronizes by using the work queue created by the object.

## Parameters

- `in_left_channel`: The [`IOUserAudioObjectPropertyElement`](../audiodriverkit-page/iouseraudioobjectpropertyelement.md) for the left channel.
- `in_right_channel`: The [`IOUserAudioObjectPropertyElement`](../audiodriverkit-page/iouseraudioobjectpropertyelement.md) for the right channel.

## See Also

### Accessing the Value
- [SetControlValue](./setcontrolvalue.md)
  Sets the stereo pan value of the control.
- [GetControlValue](./getcontrolvalue.md)
  Gets the floating-point stereo pan value of the control.
- [GetPanningChannels](./getpanningchannels.md)
  Gets the current stereo panning channels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiostereopancontrol/setpanningchannels)*