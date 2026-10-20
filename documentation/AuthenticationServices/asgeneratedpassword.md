# ASGeneratedPassword

**Framework**: Authentication Services  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- Mac Catalyst 26.2+
- visionOS 26.2+

## Declaration

```swift
class ASGeneratedPassword
```

```objc
@interface ASGeneratedPassword : NSObject
```

## Topics

### Structures
- [ASGeneratedPassword.Kind](./asgeneratedpassword/kind-swift.struct.md)
### Initializers
- [init?(coder: NSCoder)](./asgeneratedpassword/init%28coder%29.md)
- [init(kind: ASGeneratedPassword.Kind, value: String)](./asgeneratedpassword/init%28kind,value%29.md)
### Instance Properties
- [var kind: ASGeneratedPassword.Kind](./asgeneratedpassword/kind-swift.property.md)
  The kind of password that this represents.
- [var localizedName: String](./asgeneratedpassword/localizedname.md)
  The user-visible description of this password, derived from the kind.
- [var value: String](./asgeneratedpassword/value.md)
  The value of the password.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asgeneratedpassword)*