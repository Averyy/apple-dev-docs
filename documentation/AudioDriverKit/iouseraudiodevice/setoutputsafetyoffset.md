# SetOutputSafetyOffset

**Framework**: AudioDriverKit  
**Kind**: method

Specifies the output safety offset of the device.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
kern_return_t SetOutputSafetyOffset(uint32_t in_safety_offset);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. For a list of error codes, see [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

The safety offset indicates the number for frames ahead of the current hardware position that’s safe to perform output I/O.

## Parameters

- `in_safety_offset`: The output safety offset value, as a  .

## See Also

- [SetInputSafetyOffset](iouseraudiodevice/setinputsafetyoffset.md)
  Specifies the input safety offset of the device.
- [GetInputSafetyOffset](iouseraudiodevice/getinputsafetyoffset.md)
  Returns the input safety offset of the device.
- [GetOutputSafetyOffset](iouseraudiodevice/getoutputsafetyoffset.md)
  Returns the output safety offset of the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiodevice/setoutputsafetyoffset)*