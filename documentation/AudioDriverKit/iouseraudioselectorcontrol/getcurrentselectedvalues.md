# GetCurrentSelectedValues

**Framework**: AudioDriverKit  
**Kind**: method

Gets the current selections of the selector.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
size_t GetCurrentSelectedValues(IOUserAudioSelectorValue * out_values, size_t in_num_values);
```

#### Return Value

The number of values populated in the `out_values` buffer.

#### Discussion

This method synchronizes by using the work queue created by the object.

## Parameters

- `out_values`: A pointer to a buffer of type  , with a size of  . On return, this buffer contains the selected values.
- `in_num_values`: The size of the   array.

## See Also

- [SetCurrentSelectedValues](iouseraudioselectorcontrol/setcurrentselectedvalues.md)
  Sets the current selections of the selector.
- [GetControlValuesCount](iouseraudioselectorcontrol/getcontrolvaluescount.md)
  Gets the number of available selector values.
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

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudioselectorcontrol/getcurrentselectedvalues)*