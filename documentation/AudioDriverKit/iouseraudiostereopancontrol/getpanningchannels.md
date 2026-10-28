# GetPanningChannels

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Gets the current stereo panning channels.

**Availability**:
- DriverKit 21.0+

## Declaration

```c
void GetPanningChannels(IOUserAudioObjectPropertyElement *out_left_channel, IOUserAudioObjectPropertyElement *out_right_channel);
```

## Discussion

This method synchronizes by using the work queue created by the object.

## Parameters

- `out_left_channel`: On return, the [`IOUserAudioObjectPropertyElement`](../audiodriverkit-page/iouseraudioobjectpropertyelement.md) for the left channel.
- `out_right_channel`: On return, the [`IOUserAudioObjectPropertyElement`](../audiodriverkit-page/iouseraudioobjectpropertyelement.md) for the right channel.

## See Also

### Accessing the Value
- [SetControlValue](./setcontrolvalue.md)
  Sets the stereo pan value of the control.
- [GetControlValue](./getcontrolvalue.md)
  Gets the floating-point stereo pan value of the control.
- [SetPanningChannels](./setpanningchannels.md)
  Sets the current stereo panning channels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiostereopancontrol/getpanningchannels)*