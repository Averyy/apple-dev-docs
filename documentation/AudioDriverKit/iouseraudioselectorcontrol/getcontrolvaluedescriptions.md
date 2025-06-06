# GetControlValueDescriptions

**Framework**: AudioDriverKit  
**Kind**: method

Gets value descriptions used by the selector control.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
size_t GetControlValueDescriptions(IOUserAudioSelectorValueDescription * out_control_value_descriptions, size_t in_num_value_descriptions);
```

#### Return Value

The number of values populated in the `out_control_value_descriptions` buffer.

#### Discussion

This method synchronizes by using the work queue created by the object.

## Parameters

- `out_control_value_descriptions`: A pointer to a buffer of type  , with a size of  . On return, this buffer contains the value descriptions.
- `in_num_value_descriptions`: The number of descriptions in  .

## See Also

- [SetCurrentSelectedValues](iouseraudioselectorcontrol/setcurrentselectedvalues.md)
  Sets the current selections of the selector.
- [GetCurrentSelectedValues](iouseraudioselectorcontrol/getcurrentselectedvalues.md)
  Gets the current selections of the selector.
- [GetControlValuesCount](iouseraudioselectorcontrol/getcontrolvaluescount.md)
  Gets the number of available selector values.
- [IOUserAudioSelectorValue](iouseraudioselectorvalue.md)
  The type of values managed by a selector control.
- [AddControlValueDescriptions](iouseraudioselectorcontrol/addcontrolvaluedescriptions.md)
  Add value descriptions to the selector control.
- [RemoveControlValueDescriptions](iouseraudioselectorcontrol/removecontrolvaluedescriptions.md)
  Removes value descriptions from the selector control.
- [IOUserAudioSelectorValueDescription](iouseraudioselectorvaluedescription.md)
  A type that describes a value in a selection control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudioselectorcontrol/getcontrolvaluedescriptions)*