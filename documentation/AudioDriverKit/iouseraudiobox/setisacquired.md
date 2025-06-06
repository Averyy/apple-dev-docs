# SetIsAcquired

**Framework**: AudioDriverKit  
**Kind**: method

Set the box’s acquisition state.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
kern_return_t SetIsAcquired(bool in_is_acquired);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. For a list of error codes, see [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

If successful, changing the acquisition state sends a notification to the host to update the object state.

This method synchronizes by using the work queue created by the object.

## Parameters

- `in_is_acquired`: The new value of the box’s acquisition state.

## See Also

- [HandleChangeAcquireBox](iouseraudiobox/handlechangeacquirebox.md)
  Informs the box of a change to its acquisition state.
- [IsAcquired](iouseraudiobox/isacquired.md)
  Returns a Boolean value that indicates the box’s acquisition state.
- [SetIsAcquirable](iouseraudiobox/setisacquirable.md)
  Set the box’s acquirability state.
- [IsAcquirable](iouseraudiobox/isacquirable.md)
  Returns a Boolean value that indicates the box’s acquirabilty state.
- [SetAcquisitionFailure](iouseraudiobox/setacquisitionfailure.md)
  Sets the error code to return when box acquisition fails.
- [GetAcquisitionFailure](iouseraudiobox/getacquisitionfailure.md)
  Returns the error code for use when box acquisition fails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiobox/setisacquired)*