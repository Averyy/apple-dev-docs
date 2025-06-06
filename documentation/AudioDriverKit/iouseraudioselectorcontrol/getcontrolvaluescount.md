# GetControlValuesCount

**Framework**: AudioDriverKit  
**Kind**: method

Gets the number of available selector values.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
size_t GetControlValuesCount();
```

#### Return Value

The number of available selector values.

#### Discussion

This method synchronizes by using the work queue created by the object.

## See Also

- [SetCurrentSelectedValues](iouseraudioselectorcontrol/setcurrentselectedvalues.md)
  Sets the current selections of the selector.
- [GetCurrentSelectedValues](iouseraudioselectorcontrol/getcurrentselectedvalues.md)
  Gets the current selections of the selector.
- [IOUserAudioSelectorValue](iouseraudioselectorvalue.md)
  The type of values managed by a selector control.
- [AddControlValueDescriptions](iouseraudioselectorcontrol/addcontrolvaluedescriptions.md)
  Add value descriptions to the selector control.
- [RemoveControlValueDescriptions](iouseraudioselectorcontrol/removecontrolvaluedescriptions.md)
  Removes value descriptions from the selector control.
- [GetControlValueDescriptions](iouseraudioselectorcontrol/getcontrolvaluedescriptions.md)
  Gets value descriptions used by the selector control.
- [IOUserAudioSelectorValueDescription](iouseraudioselectorvaluedescription.md)
  A type that describes a value in a selection control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudioselectorcontrol/getcontrolvaluescount)*