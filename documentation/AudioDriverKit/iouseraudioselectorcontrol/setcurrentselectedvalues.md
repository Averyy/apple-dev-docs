# SetCurrentSelectedValues

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Sets the current selections of the selector.

**Availability**:
- DriverKit 21.0+

## Declaration

```c
kern_return_t SetCurrentSelectedValues(const IOUserAudioSelectorValue *in_values, size_t in_num_values);
```

#### Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. For a list of error codes, see [Error Codes](../../DriverKit/error-codes.md).

#### Discussion

If successful, changing the control’s selected values sends a notification to the host to update the object state.

This method synchronizes by using the work queue created by the object.

## Parameters

- `in_values`: An array of [`IOUserAudioSelectorValue`](../iouseraudioselectorvalue.md) values to set as the current selection of the control.
- `in_num_values`: The number of values in `in_values`.

## See Also

### Accessing the Selected Values
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
- [GetControlValueDescriptions](./getcontrolvaluedescriptions.md)
  Gets value descriptions used by the selector control.
- [IOUserAudioSelectorValueDescription](../iouseraudioselectorvaluedescription.md)
  A type that describes a value in a selection control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudioselectorcontrol/setcurrentselectedvalues)*