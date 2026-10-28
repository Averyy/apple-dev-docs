# HandleChangeAcquireBox

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Informs the box of a change to its acquisition state.

**Availability**:
- DriverKit 21.0+

## Declaration

```cpp
virtual kern_return_t HandleChangeAcquireBox(bool in_acquire);
```

## Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. For a list of error codes, see [Error Codes](../../DriverKit/error-codes.md).

## Discussion

The default implementation calls [`SetIsAcquired`](./setisacquired.md) and return [`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md). Custom drivers should override this method to validate the change, then return [`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) to confirm the change. If acquisition fails, return the error code returned from [`GetAcquisitionFailure`](./getacquisitionfailure.md).

## Parameters

- `in_acquire`: A Boolean value that indicates the acquisition state. If this value is `true`, the box is being acquired.

## See Also

### Managing Acquirability
- [SetIsAcquired](./setisacquired.md)
  Set the box’s acquisition state.
- [IsAcquired](./isacquired.md)
  Returns a Boolean value that indicates the box’s acquisition state.
- [SetIsAcquirable](./setisacquirable.md)
  Set the box’s acquirability state.
- [IsAcquirable](./isacquirable.md)
  Returns a Boolean value that indicates the box’s acquirabilty state.
- [SetAcquisitionFailure](./setacquisitionfailure.md)
  Sets the error code to return when box acquisition fails.
- [GetAcquisitionFailure](./getacquisitionfailure.md)
  Returns the error code for use when box acquisition fails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiobox/handlechangeacquirebox)*