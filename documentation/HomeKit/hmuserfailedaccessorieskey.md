# HMUserFailedAccessoriesKey

**Framework**: HomeKit  
**Kind**: var

The key for retrieving details of what accessories failed to add or remove a user.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let HMUserFailedAccessoriesKey: String
```

#### Discussion

The value associated with this key is an [`NSArray`](https://developer.apple.com/documentation/Foundation/NSArray) of [`NSDictionary`](https://developer.apple.com/documentation/Foundation/NSDictionary) objects. Each dictionary contains the [`UUID`](https://developer.apple.com/documentation/Foundation/NSUUID/UUID) of the accessory that failed to be added/removed and the value corresponding to the dictionary key is an [`NSError`](https://developer.apple.com/documentation/Foundation/NSError) that provides more details on the underlying error for that accessory.

## See Also

- [func homeAccessControl(for: HMUser) -> HMHomeAccessControl](hmhome/homeaccesscontrol(for:).md)
  Retrieves the access level of a user associated with the home.
- [class HMHomeAccessControl](hmhomeaccesscontrol.md)
  The access privileges of a user associated with a home.
- [class HMAccessControl](hmaccesscontrol.md)
  An abstract superclass for accessing user privileges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmuserfailedaccessorieskey)*