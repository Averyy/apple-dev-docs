# SecQWACTLSBindingError

**Framework**: Security  
**Kind**: enum  
**Role**: Enumeration

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum SecQWACTLSBindingError
```

```c
enum SecQWACTLSBindingError : CFIndex;
```

## Overview

Codes in kSecQWACTLSBindingErrorDomain, describing why a 2-QWAC TLS certificate binding was rejected.

certificate validation is not enabled on this device. No validation was attempted.

the JWS Compact Serialization that ETSI TS 119 411-5 Annex B requires.

conform to the Annex B profile, for example a wrong content type, a signed detached-content descriptor that is absent or not marked critical, or an unsupported digest algorithm.

did not verify against the public key of the 2-QWAC.

carried by the binding did not validate. The underlying error describes the trust failure.

correctly signed by a valid 2-QWAC, but does not commit to the TLS certificate of the connection that was passed in. The binding belongs to some other connection.

window, or is older than the maximum age accepted for a binding.

## Topics

### Enumeration Cases
- [SecQWACTLSBindingError.certificate](./secqwactlsbindingerror/certificate.md)
- [SecQWACTLSBindingError.expired](./secqwactlsbindingerror/expired.md)
- [SecQWACTLSBindingError.malformed](./secqwactlsbindingerror/malformed.md)
- [SecQWACTLSBindingError.notBound](./secqwactlsbindingerror/notbound.md)
- [SecQWACTLSBindingError.profile](./secqwactlsbindingerror/profile.md)
- [SecQWACTLSBindingError.signature](./secqwactlsbindingerror/signature.md)
- [SecQWACTLSBindingError.unavailable](./secqwactlsbindingerror/unavailable.md)
### Initializers
- [init?(rawValue: CFIndex)](./secqwactlsbindingerror/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secqwactlsbindingerror)*