# SetRange

**Framework**: AudioDriverKit  
**Kind**: method

Sets the range of possible values for the slider.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
kern_return_t SetRange(IOUserAudioSliderRange in_range);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. For a list of error codes, see [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

If successful, changing the range sends a notification to the host to update the object state.

This method synchronizes by using the work queue created by the object.

## Parameters

- `in_range`: The range to set.

## See Also

- [SetControlValue](iouseraudioslidercontrol/setcontrolvalue.md)
  Sets the value of the slider control.
- [GetControlValue](iouseraudioslidercontrol/getcontrolvalue.md)
  Gets the value of the slider control.
- [GetRange](iouseraudioslidercontrol/getrange.md)
  Gets the range of possible values for the slider.
- [IOUserAudioSliderRange](iouseraudiosliderrange.md)
  A type that indicates minimum and maximum values for slider controls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudioslidercontrol/setrange)*