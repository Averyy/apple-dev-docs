# RegistrationError

**Framework**: ServicesAccountLinking  
**Kind**: struct  
**Role**: Structure

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
- [static var errorDomain: String](./registrationerror/errordomain.md)
- [static var failed: RegistrationError.Code](./registrationerror/failed.md)
  Registration failed.
- [static var notEligible: RegistrationError.Code](./registrationerror/noteligible.md)
  The application is not registered as an authorized partner.
- [static var rateLimited: RegistrationError.Code](./registrationerror/ratelimited.md)
### Enumerations
- [RegistrationError.Code](./registrationerror/code.md)
  Registration error codes.

## Relationships

### Conforms To
- [CustomNSError](../Foundation/customnserror.md)
- [Equatable](../Swift/equatable.md)
- [Error](../Swift/error.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Error handling
- [let RegistrationErrorDomain: String](./registrationerrordomain.md)
  Error domain for account registration failures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/servicesaccountlinking/registrationerror)*