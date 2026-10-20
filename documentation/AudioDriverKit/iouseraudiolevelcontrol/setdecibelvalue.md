# SetDecibelValue

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Sets the decibel value of the level control.

**Availability**:
- DriverKit 21.0+

## Declaration

```c
kern_return_t SetDecibelValue(float in_decibel_value);
```

#### Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. For a list of error codes, see [Error Codes](../../DriverKit/error-codes.md).

#### Discussion

If successful, changing the scalar value sends a notification to the host to update the object state.

This method synchronizes by using the work queue created by the object.

## Parameters

- `in_decibel_value`: The decibel value to set.

## See Also

### Accessing the Value
- [SetScalarValue](./setscalarvalue.md)
  Sets the scalar value of the level control.
- [GetScalarValue](./getscalarvalue.md)
  Gets the scalar value of the level control.
- [GetDecibelValue](./getdecibelvalue.md)
  Gets the decibel value of the level control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiolevelcontrol/setdecibelvalue)*