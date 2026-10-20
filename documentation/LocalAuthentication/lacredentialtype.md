# LACredentialType

**Framework**: Local Authentication  
**Kind**: enum  
**Role**: Enumeration

The types of credentials to be used for authentication.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
enum LACredentialType
```

```c
enum LACredentialType : NSInteger;
```

## Topics

### Cases
- [LACredentialType.applicationPassword](./lacredentialtype/applicationpassword.md)
  Specifies that a password is provided by the application.
- [LACredentialType.smartCardPIN](./lacredentialtype/smartcardpin.md)
### Constants
- [var kLACredentialTypeApplicationPassword: Int32](./klacredentialtypeapplicationpassword.md)
  Specifies that a password is provided by the application.
- [var kLACredentialSmartCardPIN: Int32](./klacredentialsmartcardpin.md)
### Initializers
- [init?(rawValue: Int)](./lacredentialtype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Managing credentials
- [func setCredential(Data?, type: LACredentialType) -> Bool](./lacontext/setcredential%28_,type%29.md)
  Sets an application-provided credential to be used when evaluating authentication.
- [func isCredentialSet(LACredentialType) -> Bool](./lacontext/iscredentialset%28_%29.md)
  Returns a Boolean value indicating whether the specified credential type is set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/lacredentialtype)*