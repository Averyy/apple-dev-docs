# GetOutputSafetyOffset

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Returns the output safety offset of the device.

**Availability**:
- DriverKit 21.0+

## Declaration

```c
uint32_t GetOutputSafetyOffset();
```

## Return Value

The output safety offset value, as a [`uint32_t`](../../kernel/uint32_t.md).

## Discussion

The safety offset indicates the number for frames ahead of the current hardware position that’s safe to perform output I/O.

## See Also

### Working with Safety Offset Behvaior
- [SetInputSafetyOffset](./setinputsafetyoffset.md)
  Specifies the input safety offset of the device.
- [GetInputSafetyOffset](./getinputsafetyoffset.md)
  Returns the input safety offset of the device.
- [SetOutputSafetyOffset](./setoutputsafetyoffset.md)
  Specifies the output safety offset of the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiodevice/getoutputsafetyoffset)*