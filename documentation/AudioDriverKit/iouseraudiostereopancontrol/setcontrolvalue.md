# SetControlValue

**Framework**: AudioDriverKit  
**Kind**: method

Sets the stereo pan value of the control.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
kern_return_t SetControlValue(float in_control_value);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. For a list of error codes, see [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

If successful, changing the control value sends a notification to the host to update the object state.

This method synchronizes by using the work queue created by the object.

## Parameters

- `in_control_value`: The floating-point stereo pan value to set.

## See Also

- [GetControlValue](iouseraudiostereopancontrol/getcontrolvalue.md)
  Gets the floating-point stereo pan value of the control.
- [SetPanningChannels](iouseraudiostereopancontrol/setpanningchannels.md)
  Sets the current stereo panning channels.
- [GetPanningChannels](iouseraudiostereopancontrol/getpanningchannels.md)
  Gets the current stereo panning channels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiostereopancontrol/setcontrolvalue)*