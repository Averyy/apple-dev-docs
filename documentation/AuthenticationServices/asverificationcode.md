# ASVerificationCode

**Framework**: Authentication Services  
**Kind**: struct

This is an instance of a verification code.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct ASVerificationCode
```

#### Overview

It represents a code at a specific point in time.

## Topics

### Initializers
- [init(code: String, timestamp: Date, domain: String?, embeddedDomains: [String], id: UUID)](asverificationcode/init(code:timestamp:domain:embeddeddomains:id:).md)
### Instance Properties
- [var code: String](asverificationcode/code.md)
  The system’s best understanding of the code that can be used for verification purposes.
- [var domain: String?](asverificationcode/domain.md)
  The domain associated with the code, if one exists.
- [var embeddedDomains: [String]](asverificationcode/embeddeddomains.md)
  Embedded page or frame domains. For domain-bound codes, this array contains all the domains specified after the code field.
- [var timestamp: Date](asverificationcode/timestamp.md)
  Date when the message was received by the device.

## Relationships

### Conforms To
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Identifiable](../swift/identifiable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asverificationcode)*