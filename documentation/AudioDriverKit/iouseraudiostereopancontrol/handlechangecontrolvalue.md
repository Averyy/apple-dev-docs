# HandleChangeControlValue

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Tells the stereo pan control the value is changing.

**Availability**:
- DriverKit 21.0+

## Declaration

```cpp
virtual kern_return_t HandleChangeControlValue(float in_control_value);
```

#### Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. For a list of error codes, see [Error Codes](../../DriverKit/error-codes.md).

#### Discussion

The default implementation calls [`SetControlValue`](./setcontrolvalue.md) and returns [`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md). Subclass and override this method to handle changes to the stream format and return [`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) upon success.

## Parameters

- `in_control_value`: The new floating-point stereo pan value to set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiostereopancontrol/handlechangecontrolvalue)*