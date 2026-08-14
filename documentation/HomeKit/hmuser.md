# HMUser

**Framework**: HomeKit  
**Kind**: class

A person in the home who may have access to control accessories and services in the home.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class HMUser
```

## Topics

### Getting Information About the User
- [var name: String](hmuser/name.md)
  The name of the user.
- [var uniqueIdentifier: UUID](hmuser/uniqueidentifier.md)
  A unique identifier for the user.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [func manageUsers(completionHandler: ((any Error)?) -> Void)](hmhome/manageusers(completionhandler:).md)
  Presents a view controller to manage users of the home.
- [var currentUser: HMUser](hmhome/currentuser.md)
  The current HomeKit user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmuser)*