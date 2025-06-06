# UserSetTargetProperties

**Framework**: SCSIControllerDriverKit  
**Kind**: method

Sets properties on the target.

**Availability**:
- DriverKit ?+

## Declaration

```swift
kern_return_t UserSetTargetProperties(SCSIDeviceIdentifier targetID, OSDictionary * properties);
```

#### Return Value

A value that indicates the result of setting the target’s properties. [`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) indicates success. For error definitions, see [`IOKit Constants`](https://developer.apple.com/documentation/iokit/iokit_constants).

#### Discussion

Your driver extension calls this method to set the specified target’s properties. The `properties` directory can contain the following keys:

- [`kIOPropertySASAddressKey`](https://developer.apple.com/documentation/kernel/kiopropertysasaddresskey)
- [`kIOPropertyFibreChannelNodeWorldWideNameKey`](https://developer.apple.com/documentation/kernel/kiopropertyfibrechannelnodeworldwidenamekey)
- [`kIOPropertyFibreChannelPortWorldWideNameKey`](https://developer.apple.com/documentation/kernel/kiopropertyfibrechannelportworldwidenamekey)
- [`kIOPropertyFibreChannelAddressIdentifierKey`](https://developer.apple.com/documentation/kernel/kiopropertyfibrechanneladdressidentifierkey)
- [`kIOPropertyFibreChannelALPAKey`](https://developer.apple.com/documentation/kernel/kiopropertyfibrechannelalpakey).

The value of each property should be a pointer to a valid [`OSString`](https://developer.apple.com/documentation/DriverKit/OSString) object that represents the value for the property. The value must be of the proper type and size for the specified key.

## Parameters

- `targetID`: The ID of the target with the properties you want to set.
- `properties`: A dictionary containing key-value pairs of properties to set.

## See Also

- [UserInitializeTargetForID](iouserscsiparallelinterfacecontroller/userinitializetargetforid.md)
  Initializes a target device in response to a call from the framework.
- [UserCreateTargetForID](iouserscsiparallelinterfacecontroller/usercreatetargetforid.md)
  Creates the specified target.
- [UserDestroyTargetForID](iouserscsiparallelinterfacecontroller/userdestroytargetforid.md)
  Destroys the specified target.
- [UserTargetPresentForID](iouserscsiparallelinterfacecontroller/usertargetpresentforid.md)
  Checks if a specific target is present.
- [UserRemoveTargetProperties](iouserscsiparallelinterfacecontroller/userremovetargetproperties.md)
  Removes properties from a target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsicontrollerdriverkit/iouserscsiparallelinterfacecontroller/usersettargetproperties)*