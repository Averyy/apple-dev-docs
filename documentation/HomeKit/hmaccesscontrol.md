# HMAccessControl

**Framework**: HomeKit  
**Kind**: class  
**Role**: Class

An abstract superclass for accessing user privileges.

**Availability**:
- iOS 11.2+
- iPadOS 11.2+
- Mac Catalyst 11.2+
- tvOS 11.2+
- visionOS 1.0+
- watchOS 4.2+

## Declaration

```swift
class HMAccessControl
```

```objc
@interface HMAccessControl : NSObject
```

#### Overview

Use a concrete subclass, like [`HMHomeAccessControl`](./hmhomeaccesscontrol.md), instead.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [HMHomeAccessControl](./hmhomeaccesscontrol.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Controlling user access
- [func homeAccessControl(for: HMUser) -> HMHomeAccessControl](./hmhome/homeaccesscontrol%28for%29.md)
  Retrieves the access level of a user associated with the home.
- [class HMHomeAccessControl](./hmhomeaccesscontrol.md)
  The access privileges of a user associated with a home.
- [let HMUserFailedAccessoriesKey: String](./hmuserfailedaccessorieskey.md)
  The key for retrieving details of what accessories failed to add or remove a user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaccesscontrol)*