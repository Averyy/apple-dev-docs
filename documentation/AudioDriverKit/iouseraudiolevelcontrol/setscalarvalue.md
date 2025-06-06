# SetScalarValue

**Framework**: AudioDriverKit  
**Kind**: method

Sets the scalar value of the level control.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
kern_return_t SetScalarValue(float in_scalar);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. For a list of error codes, see [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

If successful, changing the scalar value sends a notification to the host to update the object state.

This method synchronizes by using the work queue created by the object.

## Parameters

- `in_scalar`: The scalar value to set.

## See Also

- [GetScalarValue](iouseraudiolevelcontrol/getscalarvalue.md)
  Gets the scalar value of the level control.
- [SetDecibelValue](iouseraudiolevelcontrol/setdecibelvalue.md)
  Sets the decibel value of the level control.
- [GetDecibelValue](iouseraudiolevelcontrol/getdecibelvalue.md)
  Gets the decibel value of the level control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiolevelcontrol/setscalarvalue)*