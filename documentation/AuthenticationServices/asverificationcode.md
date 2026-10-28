# ASVerificationCode

**Framework**: Authentication Services  
**Kind**: struct  
**Role**: Structure

This is an instance of a verification code.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct ASVerificationCode
```

## Overview

It represents a code at a specific point in time.

## Topics

### Initializers
- [init(code: String, timestamp: Date, domain: String?, embeddedDomains: [String], id: UUID)](./asverificationcode/init%28code,timestamp,domain,embeddeddomains,id%29.md)
### Instance Properties
- [var code: String](./asverificationcode/code.md)
  The system’s best understanding of the code that can be used for verification purposes.
- [var domain: String?](./asverificationcode/domain.md)
  The domain associated with the code, if one exists.
- [var embeddedDomains: [String]](./asverificationcode/embeddeddomains.md)
  Embedded page or frame domains. For domain-bound codes, this array contains all the domains specified after the code field.
- [var timestamp: Date](./asverificationcode/timestamp.md)
  Date when the message was received by the device.

## Relationships

### Conforms To
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Identifiable](../Swift/identifiable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asverificationcode)*