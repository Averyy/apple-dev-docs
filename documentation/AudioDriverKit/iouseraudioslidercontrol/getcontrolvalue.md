# GetControlValue

**Framework**: AudioDriverKit  
**Kind**: method

Gets the value of the slider control.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
uint32_t GetControlValue();
```

#### Return Value

The value of the slider.

#### Discussion

This method synchronizes by using the work queue created by the object.

## See Also

- [SetControlValue](iouseraudioslidercontrol/setcontrolvalue.md)
  Sets the value of the slider control.
- [SetRange](iouseraudioslidercontrol/setrange.md)
  Sets the range of possible values for the slider.
- [GetRange](iouseraudioslidercontrol/getrange.md)
  Gets the range of possible values for the slider.
- [IOUserAudioSliderRange](iouseraudiosliderrange.md)
  A type that indicates minimum and maximum values for slider controls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudioslidercontrol/getcontrolvalue)*