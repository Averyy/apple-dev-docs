# GetControlValuesCount

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Gets the number of available selector values.

**Availability**:
- DriverKit 21.0+

## Declaration

```c
size_t GetControlValuesCount();
```

## Return Value

The number of available selector values.

## Discussion

This method synchronizes by using the work queue created by the object.

## See Also

### Accessing the Selected Values
- [SetCurrentSelectedValues](./setcurrentselectedvalues.md)
  Sets the current selections of the selector.
- [GetCurrentSelectedValues](./getcurrentselectedvalues.md)
  Gets the current selections of the selector.
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

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudioselectorcontrol/getcontrolvaluescount)*