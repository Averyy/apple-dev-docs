# GetControlValue

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Gets the floating-point stereo pan value of the control.

**Availability**:
- DriverKit 21.0+

## Declaration

```c
float GetControlValue();
```

## Return Value

The floating-point stereo pan value of the control.

## Discussion

This method synchronizes by using the work queue created by the object.

## See Also

### Accessing the Value
- [SetControlValue](./setcontrolvalue.md)
  Sets the stereo pan value of the control.
- [SetPanningChannels](./setpanningchannels.md)
  Sets the current stereo panning channels.
- [GetPanningChannels](./getpanningchannels.md)
  Gets the current stereo panning channels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiostereopancontrol/getcontrolvalue)*