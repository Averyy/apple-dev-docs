# HandleChangeScalarValue

**Framework**: AudioDriverKit  
**Kind**: method

Tells the slider control the scalar value is changing.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
kern_return_t HandleChangeScalarValue(float in_scalar_value);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. For a list of error codes, see [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

The default implementation calls [`SetScalarValue`](iouseraudiolevelcontrol/setscalarvalue.md) and returns [`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess). Subclass and override this method to handle changes to the stream format and return [`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) upon success.

## Parameters

- `in_scalar_value`: The new scalar value to set.

## See Also

- [HandleChangeDecibelValue](iouseraudiolevelcontrol/handlechangedecibelvalue.md)
  Tells the slider control the decibel value is changing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiolevelcontrol/handlechangescalarvalue)*