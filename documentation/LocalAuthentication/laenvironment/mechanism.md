# LAEnvironment.Mechanism

**Framework**: Local Authentication  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
class Mechanism
```

```objc
@interface LAEnvironmentMechanism : NSObject
```

## Topics

### Instance Properties
- [var iconSystemName: String](./mechanism/iconsystemname.md)
  Name of the SF Symbol representing this authentication mechanism.
- [var isUsable: Bool](./mechanism/isusable.md)
- [var localizedName: String](./mechanism/localizedname.md)
  The localized name of the authentication mechanism, e.g. “Touch ID”, “Face ID” etc.

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [LAEnvironment.MechanismBiometry](./mechanismbiometry.md)
- [LAEnvironment.MechanismCompanion](./mechanismcompanion.md)
- [LAEnvironment.MechanismUserPassword](./mechanismuserpassword.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/laenvironment/mechanism)*