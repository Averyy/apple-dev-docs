# HandleChangeAcquireBox

**Framework**: AudioDriverKit  
**Kind**: method

Informs the box of a change to its acquisition state.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
kern_return_t HandleChangeAcquireBox(bool in_acquire);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. For a list of error codes, see [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

The default implementation calls [`SetIsAcquired`](iouseraudiobox/setisacquired.md) and return [`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess). Custom drivers should override this method to validate the change, then return [`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) to confirm the change. If acquisition fails, return the error code returned from [`GetAcquisitionFailure`](iouseraudiobox/getacquisitionfailure.md).

## Parameters

- `in_acquire`: A Boolean value that indicates the acquisition state. If this value is  , the box is being acquired.

## See Also

- [SetIsAcquired](iouseraudiobox/setisacquired.md)
  Set the box’s acquisition state.
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

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiobox/handlechangeacquirebox)*