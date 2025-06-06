# IsAcquirable

**Framework**: AudioDriverKit  
**Kind**: method

Returns a Boolean value that indicates the box’s acquirabilty state.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
bool IsAcquirable();
```

#### Return Value

`true` if the box is acquirable; `false` otherwise.

#### Discussion

This method synchronizes by using the work queue created by the object.

## See Also

- [HandleChangeAcquireBox](iouseraudiobox/handlechangeacquirebox.md)
  Informs the box of a change to its acquisition state.
- [SetIsAcquired](iouseraudiobox/setisacquired.md)
  Set the box’s acquisition state.
- [IsAcquired](iouseraudiobox/isacquired.md)
  Returns a Boolean value that indicates the box’s acquisition state.
- [SetIsAcquirable](iouseraudiobox/setisacquirable.md)
  Set the box’s acquirability state.
- [SetAcquisitionFailure](iouseraudiobox/setacquisitionfailure.md)
  Sets the error code to return when box acquisition fails.
- [GetAcquisitionFailure](iouseraudiobox/getacquisitionfailure.md)
  Returns the error code for use when box acquisition fails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiobox/isacquirable)*