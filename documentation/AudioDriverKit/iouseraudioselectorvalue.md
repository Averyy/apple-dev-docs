# IOUserAudioSelectorValue

**Framework**: AudioDriverKit  
**Kind**: typealias

The type of values managed by a selector control.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
typedef uint32_t IOUserAudioSelectorValue;
```

#### Discussion

AudioDriverKit selectors use [`uint32_t`](https://developer.apple.com/documentation/kernel/uint32_t) values.

## See Also

- [SetCurrentSelectedValues](iouseraudioselectorcontrol/setcurrentselectedvalues.md)
  Sets the current selections of the selector.
- [GetCurrentSelectedValues](iouseraudioselectorcontrol/getcurrentselectedvalues.md)
  Gets the current selections of the selector.
- [GetControlValuesCount](iouseraudioselectorcontrol/getcontrolvaluescount.md)
  Gets the number of available selector values.
- [AddControlValueDescriptions](iouseraudioselectorcontrol/addcontrolvaluedescriptions.md)
  Add value descriptions to the selector control.
- [RemoveControlValueDescriptions](iouseraudioselectorcontrol/removecontrolvaluedescriptions.md)
  Removes value descriptions from the selector control.
- [GetControlValueDescriptions](iouseraudioselectorcontrol/getcontrolvaluedescriptions.md)
  Gets value descriptions used by the selector control.
- [IOUserAudioSelectorValueDescription](iouseraudioselectorvaluedescription.md)
  A type that describes a value in a selection control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudioselectorvalue)*