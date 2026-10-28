# UserTargetPresentForID

**Framework**: SCSIControllerDriverKit  
**Kind**: method  
**Role**: Instance Method

Checks if a specific target is present.

**Availability**:
- DriverKit

## Declaration

```cpp
virtual kern_return_t UserTargetPresentForID(SCSIDeviceIdentifier targetID, bool *result);
```

## Return Value

A value that indicates the result of checking for the target’s existence. [`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) indicates success. For error definitions, see [IOKit Constants](../../iokit/iokit_constants.md).

## Discussion

Your driver extension can call this method to determine if a target ID is actually present.

## Parameters

- `targetID`: The ID of the target to check.
- `result`: A pointer to a Boolean value that the framework sets to `true` if the target is present and `false` otherwise.

## See Also

### Managing targets
- [UserInitializeTargetForID](./userinitializetargetforid.md)
  Initializes a target device in response to a call from the framework.
- [UserCreateTargetForID](./usercreatetargetforid.md)
  Creates the specified target.
- [UserDestroyTargetForID](./userdestroytargetforid.md)
  Destroys the specified target.
- [UserSetTargetProperties](./usersettargetproperties.md)
  Sets properties on the target.
- [UserRemoveTargetProperties](./userremovetargetproperties.md)
  Removes properties from a target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsicontrollerdriverkit/iouserscsiparallelinterfacecontroller/usertargetpresentforid)*