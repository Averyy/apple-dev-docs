# SetRange

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Sets the range of possible values for the slider.

**Availability**:
- DriverKit 21.0+

## Declaration

```c
kern_return_t SetRange(IOUserAudioSliderRange in_range);
```

#### Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. For a list of error codes, see [Error Codes](../../DriverKit/error-codes.md).

#### Discussion

If successful, changing the range sends a notification to the host to update the object state.

This method synchronizes by using the work queue created by the object.

## Parameters

- `in_range`: The range to set.

## See Also

### Accessing the Value
- [SetControlValue](./setcontrolvalue.md)
  Sets the value of the slider control.
- [GetControlValue](./getcontrolvalue.md)
  Gets the value of the slider control.
- [GetRange](./getrange.md)
  Gets the range of possible values for the slider.
- [IOUserAudioSliderRange](../iouseraudiosliderrange.md)
  A type that indicates minimum and maximum values for slider controls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudioslidercontrol/setrange)*