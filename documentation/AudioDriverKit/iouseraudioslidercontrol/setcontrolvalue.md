# SetControlValue

**Framework**: AudioDriverKit  
**Kind**: method

Sets the value of the slider control.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
kern_return_t SetControlValue(uint32_t in_control_value);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. For a list of error codes, see [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

If successful, changing the control value sends a notification to the host to update the object state.

This method synchronizes by using the work queue created by the object.

## Parameters

- `in_control_value`: The slider value to set.

## See Also

- [GetControlValue](iouseraudioslidercontrol/getcontrolvalue.md)
  Gets the value of the slider control.
- [SetRange](iouseraudioslidercontrol/setrange.md)
  Sets the range of possible values for the slider.
- [GetRange](iouseraudioslidercontrol/getrange.md)
  Gets the range of possible values for the slider.
- [IOUserAudioSliderRange](iouseraudiosliderrange.md)
  A type that indicates minimum and maximum values for slider controls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudioslidercontrol/setcontrolvalue)*