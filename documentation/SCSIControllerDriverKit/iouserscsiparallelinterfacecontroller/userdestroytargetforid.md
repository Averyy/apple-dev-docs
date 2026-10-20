# UserDestroyTargetForID

**Framework**: SCSIControllerDriverKit  
**Kind**: method  
**Role**: Instance Method

Destroys the specified target.

**Availability**:
- DriverKit

## Declaration

```cpp
virtual kern_return_t UserDestroyTargetForID(SCSITargetIdentifier targetID);
```

#### Return Value

A value that indicates the result of target removal. [`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) indicates success. For error definitions, see [IOKit Constants](../../iokit/iokit_constants.md).

#### Discussion

Your driver extension calls this method to remove the target with the specified `targetID`.

## Parameters

- `targetID`: The ID of the target to destroy.

## See Also

### Managing targets
- [UserInitializeTargetForID](./userinitializetargetforid.md)
  Initializes a target device in response to a call from the framework.
- [UserCreateTargetForID](./usercreatetargetforid.md)
  Creates the specified target.
- [UserTargetPresentForID](./usertargetpresentforid.md)
  Checks if a specific target is present.
- [UserSetTargetProperties](./usersettargetproperties.md)
  Sets properties on the target.
- [UserRemoveTargetProperties](./userremovetargetproperties.md)
  Removes properties from a target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsicontrollerdriverkit/iouserscsiparallelinterfacecontroller/userdestroytargetforid)*