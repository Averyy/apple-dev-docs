# RemoveControlValueDescriptions

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Removes value descriptions from the selector control.

**Availability**:
- DriverKit 21.0+

## Declaration

```c
kern_return_t RemoveControlValueDescriptions(const IOUserAudioSelectorValueDescription *in_value_descriptions, size_t in_num_value_descriptions);
```

#### Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) if description removal succeeded, or another value if an error occured. For a list of error codes, see [Error Codes](../../DriverKit/error-codes.md).

## Parameters

- `in_value_descriptions`: An array of [`IOUserAudioSelectorValueDescription`](../iouseraudioselectorvaluedescription.md) values to remove as the value descriptions for the selector.
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
- [AddControlValueDescriptions](./addcontrolvaluedescriptions.md)
  Add value descriptions to the selector control.
- [GetControlValueDescriptions](./getcontrolvaluedescriptions.md)
  Gets value descriptions used by the selector control.
- [IOUserAudioSelectorValueDescription](../iouseraudioselectorvaluedescription.md)
  A type that describes a value in a selection control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudioselectorcontrol/removecontrolvaluedescriptions)*