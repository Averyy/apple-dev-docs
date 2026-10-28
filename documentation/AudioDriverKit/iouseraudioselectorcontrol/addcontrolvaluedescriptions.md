# AddControlValueDescriptions

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Add value descriptions to the selector control.

**Availability**:
- DriverKit 21.0+

## Declaration

```c
kern_return_t AddControlValueDescriptions(const IOUserAudioSelectorValueDescription *in_value_descriptions, size_t in_num_value_descriptions);
```

## Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. For a list of error codes, see [Error Codes](../../DriverKit/error-codes.md).

## Parameters

- `in_value_descriptions`: An array of [`IOUserAudioSelectorValueDescription`](../iouseraudioselectorvaluedescription.md) values to add as value descriptions for the selector.
- `in_num_value_descriptions`: The number of descriptions in `in_value_descriptions`.

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
- [RemoveControlValueDescriptions](./removecontrolvaluedescriptions.md)
  Removes value descriptions from the selector control.
- [GetControlValueDescriptions](./getcontrolvaluedescriptions.md)
  Gets value descriptions used by the selector control.
- [IOUserAudioSelectorValueDescription](../iouseraudioselectorvaluedescription.md)
  A type that describes a value in a selection control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudioselectorcontrol/addcontrolvaluedescriptions)*