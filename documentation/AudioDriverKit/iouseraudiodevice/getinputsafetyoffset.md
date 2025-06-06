# GetInputSafetyOffset

**Framework**: AudioDriverKit  
**Kind**: method

Returns the input safety offset of the device.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
uint32_t GetInputSafetyOffset();
```

#### Return Value

The input safety offset value, as a [`uint32_t`](https://developer.apple.com/documentation/kernel/uint32_t).

#### Discussion

The safety offset indicates the number for frames behind the current hardware position that’s safe to perform input I/O.

## See Also

- [SetInputSafetyOffset](iouseraudiodevice/setinputsafetyoffset.md)
  Specifies the input safety offset of the device.
- [SetOutputSafetyOffset](iouseraudiodevice/setoutputsafetyoffset.md)
  Specifies the output safety offset of the device.
- [GetOutputSafetyOffset](iouseraudiodevice/getoutputsafetyoffset.md)
  Returns the output safety offset of the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiodevice/getinputsafetyoffset)*