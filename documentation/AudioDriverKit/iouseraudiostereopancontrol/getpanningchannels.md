# GetPanningChannels

**Framework**: AudioDriverKit  
**Kind**: method

Gets the current stereo panning channels.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
void GetPanningChannels(IOUserAudioObjectPropertyElement * out_left_channel, IOUserAudioObjectPropertyElement * out_right_channel);
```

#### Discussion

This method synchronizes by using the work queue created by the object.

## Parameters

- `out_left_channel`: On return, the   for the left channel.
- `out_right_channel`: On return, the   for the right channel.

## See Also

- [SetControlValue](iouseraudiostereopancontrol/setcontrolvalue.md)
  Sets the stereo pan value of the control.
- [GetControlValue](iouseraudiostereopancontrol/getcontrolvalue.md)
  Gets the floating-point stereo pan value of the control.
- [SetPanningChannels](iouseraudiostereopancontrol/setpanningchannels.md)
  Sets the current stereo panning channels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiostereopancontrol/getpanningchannels)*