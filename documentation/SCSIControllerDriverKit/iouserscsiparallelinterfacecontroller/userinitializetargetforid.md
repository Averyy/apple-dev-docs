# UserInitializeTargetForID

**Framework**: SCSIControllerDriverKit  
**Kind**: method

Initializes a target device in response to a call from the framework.

**Availability**:
- DriverKit ?+

## Declaration

```swift
kern_return_t UserInitializeTargetForID(SCSITargetIdentifier targetID);
```

#### Return Value

A value that indicates the result of initialization. [`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) indicates success. For error definitions, see [`IOKit Constants`](https://developer.apple.com/documentation/iokit/iokit_constants).

#### Discussion

The host bus adapter (HBA) can use this method to probe the target or do anything else necessary before IOKit registers the device object for matching.

## Parameters

- `targetID`: The target to initialize.

## See Also

- [UserCreateTargetForID](iouserscsiparallelinterfacecontroller/usercreatetargetforid.md)
  Creates the specified target.
- [UserDestroyTargetForID](iouserscsiparallelinterfacecontroller/userdestroytargetforid.md)
  Destroys the specified target.
- [UserTargetPresentForID](iouserscsiparallelinterfacecontroller/usertargetpresentforid.md)
  Checks if a specific target is present.
- [UserSetTargetProperties](iouserscsiparallelinterfacecontroller/usersettargetproperties.md)
  Sets properties on the target.
- [UserRemoveTargetProperties](iouserscsiparallelinterfacecontroller/userremovetargetproperties.md)
  Removes properties from a target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsicontrollerdriverkit/iouserscsiparallelinterfacecontroller/userinitializetargetforid)*