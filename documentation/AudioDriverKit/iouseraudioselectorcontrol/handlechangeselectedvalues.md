# HandleChangeSelectedValues

**Framework**: AudioDriverKit  
**Kind**: method

Tells the selection control the value is changing.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
kern_return_t HandleChangeSelectedValues(const IOUserAudioSelectorValue * in_control_values, size_t in_num_values);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. For a list of error codes, see [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

The default implementation calls [`SetCurrentSelectedValues`](iouseraudioselectorcontrol/setcurrentselectedvalues.md) and returns [`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess). Subclass and override this method to handle changes to the stream format and return [`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) upon success.

## Parameters

- `in_control_values`: An array of   values to set as the current selection of the control.
- `in_num_values`: The number of values in  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudioselectorcontrol/handlechangeselectedvalues)*