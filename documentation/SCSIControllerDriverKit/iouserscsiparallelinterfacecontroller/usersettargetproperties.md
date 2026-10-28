# UserSetTargetProperties

**Framework**: SCSIControllerDriverKit  
**Kind**: method  
**Role**: Instance Method

Sets properties on the target.

**Availability**:
- DriverKit

## Declaration

```cpp
virtual kern_return_t UserSetTargetProperties(SCSIDeviceIdentifier targetID, OSDictionary *properties);
```

## Return Value

A value that indicates the result of setting the target’s properties. [`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) indicates success. For error definitions, see [IOKit Constants](../../iokit/iokit_constants.md).

## Discussion

Your driver extension calls this method to set the specified target’s properties. The `properties` directory can contain the following keys:

- [`kIOPropertySASAddressKey`](../../kernel/kiopropertysasaddresskey.md)
- [`kIOPropertyFibreChannelNodeWorldWideNameKey`](../../kernel/kiopropertyfibrechannelnodeworldwidenamekey.md)
- [`kIOPropertyFibreChannelPortWorldWideNameKey`](../../kernel/kiopropertyfibrechannelportworldwidenamekey.md)
- [`kIOPropertyFibreChannelAddressIdentifierKey`](../../kernel/kiopropertyfibrechanneladdressidentifierkey.md)
- [`kIOPropertyFibreChannelALPAKey`](../../kernel/kiopropertyfibrechannelalpakey.md).

The value of each property should be a pointer to a valid [`OSString`](../../DriverKit/osstring.md) object that represents the value for the property. The value must be of the proper type and size for the specified key.

## Parameters

- `targetID`: The ID of the target with the properties you want to set.
- `properties`: A dictionary containing key-value pairs of properties to set.

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
- [UserRemoveTargetProperties](./userremovetargetproperties.md)
  Removes properties from a target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsicontrollerdriverkit/iouserscsiparallelinterfacecontroller/usersettargetproperties)*