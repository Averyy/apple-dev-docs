# UserDestroyTargetForID

**Framework**: SCSIControllerDriverKit  
**Kind**: method

Destroys the specified target.

**Availability**:
- DriverKit ?+

## Declaration

```swift
kern_return_t UserDestroyTargetForID(SCSITargetIdentifier targetID);
```

#### Return Value

A value that indicates the result of target removal. [`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) indicates success. For error definitions, see [`IOKit Constants`](https://developer.apple.com/documentation/iokit/iokit_constants).

#### Discussion

Your driver extension calls this method to remove the target with the specified `targetID`.

## Parameters

- `targetID`: The ID of the target to destroy.

## See Also

- [UserInitializeTargetForID](iouserscsiparallelinterfacecontroller/userinitializetargetforid.md)
  Initializes a target device in response to a call from the framework.
- [UserCreateTargetForID](iouserscsiparallelinterfacecontroller/usercreatetargetforid.md)
  Creates the specified target.
- [UserTargetPresentForID](iouserscsiparallelinterfacecontroller/usertargetpresentforid.md)
  Checks if a specific target is present.
- [UserSetTargetProperties](iouserscsiparallelinterfacecontroller/usersettargetproperties.md)
  Sets properties on the target.
- [UserRemoveTargetProperties](iouserscsiparallelinterfacecontroller/userremovetargetproperties.md)
  Removes properties from a target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsicontrollerdriverkit/iouserscsiparallelinterfacecontroller/userdestroytargetforid)*