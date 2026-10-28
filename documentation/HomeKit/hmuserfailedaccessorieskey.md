# HMUserFailedAccessoriesKey

**Framework**: HomeKit  
**Kind**: var  
**Role**: Global Variable

The key for retrieving details of what accessories failed to add or remove a user.

**Availability**:
- iOS 8.0+ - Deprecated in 27.0
- iPadOS 8.0+ - Deprecated in 27.0
- Mac Catalyst 8.0+ - Deprecated in 27.0
- tvOS 10.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 2.0+ - Deprecated in 27.0

> **Deprecated**: No longer supported

## Declaration

```swift
let HMUserFailedAccessoriesKey: String
```

```c
extern NSString * const HMUserFailedAccessoriesKey;
```

## Discussion

The value associated with this key is an [`NSArray`](../Foundation/nsarray.md) of [`NSDictionary`](../Foundation/nsdictionary.md) objects. Each dictionary contains the [`NSUUID`](../Foundation/nsuuid.md) of the accessory that failed to be added/removed and the value corresponding to the dictionary key is an [`NSError`](../Foundation/nserror.md) that provides more details on the underlying error for that accessory.

## See Also

### Controlling user access
- [func homeAccessControl(for: HMUser) -> HMHomeAccessControl](./hmhome/homeaccesscontrol%28for%29.md)
  Retrieves the access level of a user associated with the home.
- [class HMHomeAccessControl](./hmhomeaccesscontrol.md)
  The access privileges of a user associated with a home.
- [class HMAccessControl](./hmaccesscontrol.md)
  An abstract superclass for accessing user privileges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmuserfailedaccessorieskey)*