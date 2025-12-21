# RegistrationError

**Framework**: ServicesAccountLinking  
**Kind**: struct

Registration error codes.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+

## Declaration

```swift
struct RegistrationError
```

## Topics

### Type Properties
- [static var errorDomain: String](registrationerror/errordomain.md)
- [static var failed: RegistrationError.Code](registrationerror/failed.md)
  Registration failed.
- [static var notEligible: RegistrationError.Code](registrationerror/noteligible.md)
  The application is not registered as an authorized partner.
### Enumerations
- [RegistrationError.Code](registrationerror/code.md)
  Registration error codes.

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let RegistrationErrorDomain: String](registrationerrordomain.md)
  Error domain for account registration failures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/servicesaccountlinking/registrationerror)*