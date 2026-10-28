# UserInitializeTargetForID

**Framework**: SCSIControllerDriverKit  
**Kind**: method  
**Role**: Instance Method

Initializes a target device in response to a call from the framework.

**Availability**:
- DriverKit

## Declaration

```cpp
virtual kern_return_t UserInitializeTargetForID(SCSITargetIdentifier targetID);
```

## Return Value

A value that indicates the result of initialization. [`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) indicates success. For error definitions, see [IOKit Constants](../../iokit/iokit_constants.md).

## Discussion

The host bus adapter (HBA) can use this method to probe the target or do anything else necessary before IOKit registers the device object for matching.

## Parameters

- `targetID`: The target to initialize.

## See Also

### Managing targets
- [UserCreateTargetForID](./usercreatetargetforid.md)
  Creates the specified target.
- [UserDestroyTargetForID](./userdestroytargetforid.md)
  Destroys the specified target.
- [UserTargetPresentForID](./usertargetpresentforid.md)
  Checks if a specific target is present.
- [UserSetTargetProperties](./usersettargetproperties.md)
  Sets properties on the target.
- [UserRemoveTargetProperties](./userremovetargetproperties.md)
  Removes properties from a target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsicontrollerdriverkit/iouserscsiparallelinterfacecontroller/userinitializetargetforid)*