# UserTargetPresentForID

**Framework**: SCSIControllerDriverKit  
**Kind**: method

Checks if a specific target is present.

**Availability**:
- DriverKit ?+

## Declaration

```swift
kern_return_t UserTargetPresentForID(SCSIDeviceIdentifier targetID, bool * result);
```

#### Return Value

A value that indicates the result of checking for the target’s existence. [`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) indicates success. For error definitions, see [`IOKit Constants`](https://developer.apple.com/documentation/iokit/iokit_constants).

#### Discussion

Your driver extension can call this method to determine if a target ID is actually present.

## Parameters

- `targetID`: The ID of the target to check.
- `result`: A pointer to a Boolean value that the framework sets to   if the target is present and   otherwise.

## See Also

- [UserInitializeTargetForID](iouserscsiparallelinterfacecontroller/userinitializetargetforid.md)
  Initializes a target device in response to a call from the framework.
- [UserCreateTargetForID](iouserscsiparallelinterfacecontroller/usercreatetargetforid.md)
  Creates the specified target.
- [UserDestroyTargetForID](iouserscsiparallelinterfacecontroller/userdestroytargetforid.md)
  Destroys the specified target.
- [UserSetTargetProperties](iouserscsiparallelinterfacecontroller/usersettargetproperties.md)
  Sets properties on the target.
- [UserRemoveTargetProperties](iouserscsiparallelinterfacecontroller/userremovetargetproperties.md)
  Removes properties from a target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsicontrollerdriverkit/iouserscsiparallelinterfacecontroller/usertargetpresentforid)*