# GetAcquisitionFailure

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Returns the error code for use when box acquisition fails.

**Availability**:
- DriverKit 21.0+

## Declaration

```c
kern_return_t GetAcquisitionFailure();
```

#### Return Value

An error code for use when box acquisition fails.

#### Discussion

Call this method to retrieve the error to return from a failed call to [`HandleChangeAcquireBox`](./handlechangeacquirebox.md).

This method synchronizes by using the work queue created by the object.

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
- [SetAcquisitionFailure](./setacquisitionfailure.md)
  Sets the error code to return when box acquisition fails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiobox/getacquisitionfailure)*