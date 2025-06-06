# SetAcquisitionFailure

**Framework**: AudioDriverKit  
**Kind**: method

Sets the error code to return when box acquisition fails.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
kern_return_t SetAcquisitionFailure(kern_return_t in_failure_code);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. For a list of error codes, see [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

Set this code to provide the error to return from failed calls to [`HandleChangeAcquireBox`](iouseraudiobox/handlechangeacquirebox.md).

If successful, changing the acquisition failure code sends a notification to the host to update the object state.

This method synchronizes by using the work queue created by the object.

## Parameters

- `in_failure_code`: An error code to return when box acquisition fails.

## See Also

- [HandleChangeAcquireBox](iouseraudiobox/handlechangeacquirebox.md)
  Informs the box of a change to its acquisition state.
- [SetIsAcquired](iouseraudiobox/setisacquired.md)
  Set the box’s acquisition state.
- [IsAcquired](iouseraudiobox/isacquired.md)
  Returns a Boolean value that indicates the box’s acquisition state.
- [SetIsAcquirable](iouseraudiobox/setisacquirable.md)
  Set the box’s acquirability state.
- [IsAcquirable](iouseraudiobox/isacquirable.md)
  Returns a Boolean value that indicates the box’s acquirabilty state.
- [GetAcquisitionFailure](iouseraudiobox/getacquisitionfailure.md)
  Returns the error code for use when box acquisition fails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiobox/setacquisitionfailure)*