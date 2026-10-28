# GetControlValue

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Gets the value of the slider control.

**Availability**:
- DriverKit 21.0+

## Declaration

```c
uint32_t GetControlValue();
```

## Return Value

The value of the slider.

## Discussion

This method synchronizes by using the work queue created by the object.

## See Also

### Accessing the Value
- [SetControlValue](./setcontrolvalue.md)
  Sets the value of the slider control.
- [SetRange](./setrange.md)
  Sets the range of possible values for the slider.
- [GetRange](./getrange.md)
  Gets the range of possible values for the slider.
- [IOUserAudioSliderRange](../iouseraudiosliderrange.md)
  A type that indicates minimum and maximum values for slider controls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudioslidercontrol/getcontrolvalue)*