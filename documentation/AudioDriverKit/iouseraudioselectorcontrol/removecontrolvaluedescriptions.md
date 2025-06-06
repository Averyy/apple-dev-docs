# RemoveControlValueDescriptions

**Framework**: AudioDriverKit  
**Kind**: method

Removes value descriptions from the selector control.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
kern_return_t RemoveControlValueDescriptions(const IOUserAudioSelectorValueDescription * in_value_descriptions, size_t in_num_value_descriptions);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) if description removal succeeded, or another value if an error occured. For a list of error codes, see [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

## Parameters

- `in_value_descriptions`: An array of   values to remove as the value descriptions for the selector.
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
- [GetControlValueDescriptions](iouseraudioselectorcontrol/getcontrolvaluedescriptions.md)
  Gets value descriptions used by the selector control.
- [IOUserAudioSelectorValueDescription](iouseraudioselectorvaluedescription.md)
  A type that describes a value in a selection control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudioselectorcontrol/removecontrolvaluedescriptions)*