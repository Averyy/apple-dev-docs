# SetAcquisitionFailure

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Sets the error code to return when box acquisition fails.

**Availability**:
- DriverKit 21.0+

## Declaration

```c
kern_return_t SetAcquisitionFailure(kern_return_t in_failure_code);
```

## Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. For a list of error codes, see [Error Codes](../../DriverKit/error-codes.md).

## Discussion

Set this code to provide the error to return from failed calls to [`HandleChangeAcquireBox`](./handlechangeacquirebox.md).

If successful, changing the acquisition failure code sends a notification to the host to update the object state.

This method synchronizes by using the work queue created by the object.

## Parameters

- `in_failure_code`: An error code to return when box acquisition fails.

## See Also

### Managing Acquirability
- [HandleChangeAcquireBox](./handlechangeacquirebox.md)
  Informs the box of a change to its acquisition state.
- [SetIsAcquired](./setisacquired.md)
  Set the box’s acquisition state.
- [IsAcquired](./isacquired.md)
  Returns a Boolean value that indicates the box’s acquisition state.
- [SetIsAcquirable](./setisacquirable.md)
  Set the box’s acquirability state.
- [IsAcquirable](./isacquirable.md)
  Returns a Boolean value that indicates the box’s acquirabilty state.
- [GetAcquisitionFailure](./getacquisitionfailure.md)
  Returns the error code for use when box acquisition fails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiobox/setacquisitionfailure)*