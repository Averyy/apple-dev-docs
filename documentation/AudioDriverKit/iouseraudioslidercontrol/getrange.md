# GetRange

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Gets the range of possible values for the slider.

**Availability**:
- DriverKit 21.0+

## Declaration

```c
IOUserAudioSliderRange GetRange();
```

#### Return Value

The range of possible values for the slider.

#### Discussion

This method synchronizes by using the work queue created by the object.

## See Also

### Accessing the Value
- [SetControlValue](./setcontrolvalue.md)
  Sets the value of the slider control.
- [GetControlValue](./getcontrolvalue.md)
  Gets the value of the slider control.
- [SetRange](./setrange.md)
  Sets the range of possible values for the slider.
- [IOUserAudioSliderRange](../iouseraudiosliderrange.md)
  A type that indicates minimum and maximum values for slider controls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudioslidercontrol/getrange)*