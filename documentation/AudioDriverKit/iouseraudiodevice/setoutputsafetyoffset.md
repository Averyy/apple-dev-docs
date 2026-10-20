# SetOutputSafetyOffset

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Specifies the output safety offset of the device.

**Availability**:
- DriverKit 21.0+

## Declaration

```c
kern_return_t SetOutputSafetyOffset(uint32_t in_safety_offset);
```

#### Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. For a list of error codes, see [Error Codes](../../DriverKit/error-codes.md).

#### Discussion

The safety offset indicates the number for frames ahead of the current hardware position that’s safe to perform output I/O.

## Parameters

- `in_safety_offset`: The output safety offset value, as a [`uint32_t`](../../kernel/uint32_t.md).

## See Also

### Working with Safety Offset Behvaior
- [SetInputSafetyOffset](./setinputsafetyoffset.md)
  Specifies the input safety offset of the device.
- [GetInputSafetyOffset](./getinputsafetyoffset.md)
  Returns the input safety offset of the device.
- [GetOutputSafetyOffset](./getoutputsafetyoffset.md)
  Returns the output safety offset of the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiodevice/setoutputsafetyoffset)*