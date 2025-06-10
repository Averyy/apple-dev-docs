# LACredentialType

**Framework**: Local Authentication  
**Kind**: enum

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

## Topics

### Cases
- [LACredentialType.applicationPassword](lacredentialtype/applicationpassword.md)
  Specifies that a password is provided by the application.
- [LACredentialType.smartCardPIN](lacredentialtype/smartcardpin.md)
### Constants
- [var kLACredentialTypeApplicationPassword: Int32](klacredentialtypeapplicationpassword.md)
  Specifies that a password is provided by the application.
- [var kLACredentialSmartCardPIN: Int32](klacredentialsmartcardpin.md)
### Initializers
- [init?(rawValue: Int)](lacredentialtype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func setCredential(Data?, type: LACredentialType) -> Bool](lacontext/setcredential(_:type:).md)
  Sets an application-provided credential to be used when evaluating authentication.
- [func isCredentialSet(LACredentialType) -> Bool](lacontext/iscredentialset(_:).md)
  Returns a Boolean value indicating whether the specified credential type is set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/lacredentialtype)*