# UserRemoveTargetProperties

**Framework**: SCSIControllerDriverKit  
**Kind**: method

Removes properties from a target.

**Availability**:
- DriverKit ?+

## Declaration

```swift
kern_return_t UserRemoveTargetProperties(SCSIDeviceIdentifier targetID, OSArray * properties);
```

#### Return Value

A value that indicates the result of setting the target’s specified properties. [`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) indicates success. For error definitions, see [`IOKit Constants`](https://developer.apple.com/documentation/iokit/iokit_constants).

#### Discussion

Your driver extension calls this method to remove the specified properties from the target.

## Parameters

- `targetID`: The ID of the target with the properties you want to remove.
- `properties`: An array containing keys of the properties to remove.

## See Also

- [UserInitializeTargetForID](iouserscsiparallelinterfacecontroller/userinitializetargetforid.md)
  Initializes a target device in response to a call from the framework.
- [UserCreateTargetForID](iouserscsiparallelinterfacecontroller/usercreatetargetforid.md)
  Creates the specified target.
- [UserDestroyTargetForID](iouserscsiparallelinterfacecontroller/userdestroytargetforid.md)
  Destroys the specified target.
- [UserTargetPresentForID](iouserscsiparallelinterfacecontroller/usertargetpresentforid.md)
  Checks if a specific target is present.
- [UserSetTargetProperties](iouserscsiparallelinterfacecontroller/usersettargetproperties.md)
  Sets properties on the target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsicontrollerdriverkit/iouserscsiparallelinterfacecontroller/userremovetargetproperties)*