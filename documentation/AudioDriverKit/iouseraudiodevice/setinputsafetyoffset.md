# SetInputSafetyOffset

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Specifies the input safety offset of the device.

**Availability**:
- DriverKit 21.0+

## Declaration

```c
kern_return_t SetInputSafetyOffset(uint32_t in_safety_offset);
```

#### Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. For a list of error codes, see [Error Codes](../../DriverKit/error-codes.md).

#### Discussion

The safety offset indicates the number for frames behind the current hardware position that’s safe to perform input I/O.

## Parameters

- `in_safety_offset`: The input safety offset value, as a [`uint32_t`](../../kernel/uint32_t.md).

## See Also

### Working with Safety Offset Behvaior
- [GetInputSafetyOffset](./getinputsafetyoffset.md)
  Returns the input safety offset of the device.
- [SetOutputSafetyOffset](./setoutputsafetyoffset.md)
  Specifies the output safety offset of the device.
- [GetOutputSafetyOffset](./getoutputsafetyoffset.md)
  Returns the output safety offset of the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiodevice/setinputsafetyoffset)*