# HandleChangeSelectedValues

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Tells the selection control the value is changing.

**Availability**:
- DriverKit 21.0+

## Declaration

```cpp
virtual kern_return_t HandleChangeSelectedValues(const IOUserAudioSelectorValue *in_control_values, size_t in_num_values);
```

#### Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. For a list of error codes, see [Error Codes](../../DriverKit/error-codes.md).

#### Discussion

The default implementation calls [`SetCurrentSelectedValues`](./setcurrentselectedvalues.md) and returns [`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md). Subclass and override this method to handle changes to the stream format and return [`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) upon success.

## Parameters

- `in_control_values`: An array of [`IOUserAudioSelectorValue`](../iouseraudioselectorvalue.md) values to set as the current selection of the control.
- `in_num_values`: The number of values in `in_control_values`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudioselectorcontrol/handlechangeselectedvalues)*