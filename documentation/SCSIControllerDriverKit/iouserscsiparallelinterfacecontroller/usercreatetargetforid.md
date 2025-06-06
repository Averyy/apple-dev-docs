# UserCreateTargetForID

**Framework**: SCSIControllerDriverKit  
**Kind**: method

Creates the specified target.

**Availability**:
- DriverKit ?+

## Declaration

```swift
kern_return_t UserCreateTargetForID(SCSIDeviceIdentifier targetID, OSDictionary * targetDict);
```

#### Return Value

A value that indicates the result of target creation. [`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) indicates success. For error definitions, see [`IOKit Constants`](https://developer.apple.com/documentation/iokit/iokit_constants).

#### Discussion

Your driver extension class calls this method to create a new target for the `targetID`. The framework creates the new target before the call returns.

As part of the [`UserCreateTargetForID`](iouserscsiparallelinterfacecontroller/usercreatetargetforid.md) call, the kernel calls several APIs like [`UserInitializeTargetForID`](iouserscsiparallelinterfacecontroller/userinitializetargetforid.md) which run on the default dispatch queue of the dext. Synchronously calling [`UserCreateTargetForID`](iouserscsiparallelinterfacecontroller/usercreatetargetforid.md) from the default dispatch queue blocks the default dispatch queue until [`UserCreateTargetForID`](iouserscsiparallelinterfacecontroller/usercreatetargetforid.md) finishes. Subsequent calls from the kernel like [`UserInitializeTargetForID`](iouserscsiparallelinterfacecontroller/userinitializetargetforid.md) won’t have a chance to run on the default queue, leading to a deadlock.

You can avoid this problem by calling [`UserCreateTargetForID`](iouserscsiparallelinterfacecontroller/usercreatetargetforid.md) from an asynchronous handler function. Start by creating an async handler function for your custom dext class in its `iig` file, as shown below:

```objc
virtual void AsyncEventHandler ( OSAction *  action TARGET,                                 uint32_t    targetID ) = 0;

virtual void AsyncCreateTargetForID ( OSAction *  action,
                                    uint32_t    targetID )
                                    TYPE ( ExampleSCSIDext::AsyncEventHandler ) QUEUENAME ( AuxiliaryQueue );
```

This handler function can then call [`UserCreateTargetForID`](iouserscsiparallelinterfacecontroller/usercreatetargetforid.md):

```objc
void
IMPL ( MyCustomService, AsyncCreateTargetForID )
{
     kern_return_t ret;
     …
     ret = UserCreateTargetForID (targetID, NULL);
     …
}
```

Then you can call this handler in [`UserStartController`](iouserscsiparallelinterfacecontroller/userstartcontroller.md):

```objc
kern_return_t
IMPL ( MyCustomService, UserStartController )
{
    …
    ret = CreateActionAsyncCreateTargetForID ( sizeof ( void * ), &ivars->fAsyncEventHandler );
    assert ( kIOReturnSuccess == ret );

    AsyncEventHandler ( ivars->fAsyncEventHandler, targetID );
    …
}
```

This implementation ensures [`UserStartController`](iouserscsiparallelinterfacecontroller/userstartcontroller.md) calls the event handler asynchronously, which frees up the default dispatch queue for subsequent calls.

## Parameters

- `targetID`: The ID of the target to create.
- `targetDict`: An   containing all of the target properties.

## See Also

- [UserInitializeTargetForID](iouserscsiparallelinterfacecontroller/userinitializetargetforid.md)
  Initializes a target device in response to a call from the framework.
- [UserDestroyTargetForID](iouserscsiparallelinterfacecontroller/userdestroytargetforid.md)
  Destroys the specified target.
- [UserTargetPresentForID](iouserscsiparallelinterfacecontroller/usertargetpresentforid.md)
  Checks if a specific target is present.
- [UserSetTargetProperties](iouserscsiparallelinterfacecontroller/usersettargetproperties.md)
  Sets properties on the target.
- [UserRemoveTargetProperties](iouserscsiparallelinterfacecontroller/userremovetargetproperties.md)
  Removes properties from a target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsicontrollerdriverkit/iouserscsiparallelinterfacecontroller/usercreatetargetforid)*