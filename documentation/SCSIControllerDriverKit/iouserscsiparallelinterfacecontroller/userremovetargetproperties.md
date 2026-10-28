# UserRemoveTargetProperties

**Framework**: SCSIControllerDriverKit  
**Kind**: method  
**Role**: Instance Method

Removes properties from a target.

**Availability**:
- DriverKit

## Declaration

```cpp
virtual kern_return_t UserRemoveTargetProperties(SCSIDeviceIdentifier targetID, OSArray *properties);
```

## Return Value

A value that indicates the result of setting the target’s specified properties. [`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) indicates success. For error definitions, see [IOKit Constants](../../iokit/iokit_constants.md).

## Discussion

Your driver extension calls this method to remove the specified properties from the target.

## Parameters

- `targetID`: The ID of the target with the properties you want to remove.
- `properties`: An array containing keys of the properties to remove.

## See Also

### Managing targets
- [UserInitializeTargetForID](./userinitializetargetforid.md)
  Initializes a target device in response to a call from the framework.
- [UserCreateTargetForID](./usercreatetargetforid.md)
  Creates the specified target.
- [UserDestroyTargetForID](./userdestroytargetforid.md)
  Destroys the specified target.
- [UserTargetPresentForID](./usertargetpresentforid.md)
  Checks if a specific target is present.
- [UserSetTargetProperties](./usersettargetproperties.md)
  Sets properties on the target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsicontrollerdriverkit/iouserscsiparallelinterfacecontroller/userremovetargetproperties)*