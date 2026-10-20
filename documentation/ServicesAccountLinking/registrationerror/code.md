# RegistrationError.Code

**Framework**: ServicesAccountLinking  
**Kind**: enum  
**Role**: Enumeration

Registration error codes.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+

## Declaration

```swift
enum Code
```

```c
enum SALRegistrationError : NSInteger;
```

## Topics

### Enumeration Cases
- [RegistrationError.Code.failed](./code/failed.md)
  Registration failed.
- [RegistrationError.Code.notEligible](./code/noteligible.md)
  The application is not registered as an authorized partner.
- [RegistrationError.Code.rateLimited](./code/ratelimited.md)
  The server rate-limited the request.
### Initializers
- [init?(rawValue: Int)](./code/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/servicesaccountlinking/registrationerror/code)*