# HMUser

**Framework**: HomeKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface HMUser : NSObject
```

## Topics

### Getting Information About the User
- [var name: String](./hmuser/name.md)
  The name of the user.
- [var uniqueIdentifier: UUID](./hmuser/uniqueidentifier.md)
  A unique identifier for the user.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
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

### Managing users
- [func manageUsers(completionHandler: ((any Error)?) -> Void)](./hmhome/manageusers%28completionhandler%29.md)
  Presents a view controller to manage users of the home.
- [var currentUser: HMUser](./hmhome/currentuser.md)
  The current HomeKit user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmuser)*