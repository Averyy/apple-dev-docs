# GetControlValueDescriptions

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Gets value descriptions used by the selector control.

**Availability**:
- DriverKit 21.0+

## Declaration

```c
size_t GetControlValueDescriptions(IOUserAudioSelectorValueDescription *out_control_value_descriptions, size_t in_num_value_descriptions);
```

## Return Value

The number of values populated in the `out_control_value_descriptions` buffer.

## Discussion

This method synchronizes by using the work queue created by the object.

## Parameters

- `out_control_value_descriptions`: A pointer to a buffer of type [`IOUserAudioSelectorValueDescription`](../iouseraudioselectorvaluedescription.md), with a size of `in_num_value_descriptions`. On return, this buffer contains the value descriptions.
- `in_num_value_descriptions`: The number of descriptions in `out_control_value_descriptions`.

## See Also

### Accessing the Selected Values
- [SetCurrentSelectedValues](./setcurrentselectedvalues.md)
  Sets the current selections of the selector.
- [GetCurrentSelectedValues](./getcurrentselectedvalues.md)
  Gets the current selections of the selector.
- [GetControlValuesCount](./getcontrolvaluescount.md)
  Gets the number of available selector values.
- [IOUserAudioSelectorValue](../iouseraudioselectorvalue.md)
  The type of values managed by a selector control.
- [AddControlValueDescriptions](./addcontrolvaluedescriptions.md)
  Add value descriptions to the selector control.
- [RemoveControlValueDescriptions](./removecontrolvaluedescriptions.md)
  Removes value descriptions from the selector control.
- [IOUserAudioSelectorValueDescription](../iouseraudioselectorvaluedescription.md)
  A type that describes a value in a selection control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudioselectorcontrol/getcontrolvaluedescriptions)*