# SetControlValue

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Sets the value of the slider control.

**Availability**:
- DriverKit 21.0+

## Declaration

```c
kern_return_t SetControlValue(uint32_t in_control_value);
```

#### Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. For a list of error codes, see [Error Codes](../../DriverKit/error-codes.md).

#### Discussion

If successful, changing the control value sends a notification to the host to update the object state.

This method synchronizes by using the work queue created by the object.

## Parameters

- `in_control_value`: The slider value to set.

## See Also

### Accessing the Value
- [GetControlValue](./getcontrolvalue.md)
  Gets the value of the slider control.
- [SetRange](./setrange.md)
  Sets the range of possible values for the slider.
- [GetRange](./getrange.md)
  Gets the range of possible values for the slider.
- [IOUserAudioSliderRange](../iouseraudiosliderrange.md)
  A type that indicates minimum and maximum values for slider controls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudioslidercontrol/setcontrolvalue)*