# HandleChangeScalarValue

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Tells the slider control the scalar value is changing.

**Availability**:
- DriverKit 21.0+

## Declaration

```cpp
virtual kern_return_t HandleChangeScalarValue(float in_scalar_value);
```

#### Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. For a list of error codes, see [Error Codes](../../DriverKit/error-codes.md).

#### Discussion

The default implementation calls [`SetScalarValue`](./setscalarvalue.md) and returns [`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md). Subclass and override this method to handle changes to the stream format and return [`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) upon success.

## Parameters

- `in_scalar_value`: The new scalar value to set.

## See Also

### Supporting Value Changes
- [HandleChangeDecibelValue](./handlechangedecibelvalue.md)
  Tells the slider control the decibel value is changing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiolevelcontrol/handlechangescalarvalue)*