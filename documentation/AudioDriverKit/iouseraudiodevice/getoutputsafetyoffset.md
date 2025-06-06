# GetOutputSafetyOffset

**Framework**: AudioDriverKit  
**Kind**: method

Returns the output safety offset of the device.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
uint32_t GetOutputSafetyOffset();
```

#### Return Value

The output safety offset value, as a [`uint32_t`](https://developer.apple.com/documentation/kernel/uint32_t).

#### Discussion

The safety offset indicates the number for frames ahead of the current hardware position that’s safe to perform output I/O.

## See Also

- [SetInputSafetyOffset](iouseraudiodevice/setinputsafetyoffset.md)
  Specifies the input safety offset of the device.
- [GetInputSafetyOffset](iouseraudiodevice/getinputsafetyoffset.md)
  Returns the input safety offset of the device.
- [SetOutputSafetyOffset](iouseraudiodevice/setoutputsafetyoffset.md)
  Specifies the output safety offset of the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiodevice/getoutputsafetyoffset)*