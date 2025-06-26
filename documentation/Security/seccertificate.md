# SecCertificate

**Framework**: Security  
**Kind**: class

An abstract Core Foundation-type object representing an X.509 certificate.

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
class SecCertificate
```

## Mentions

- [Storing a DER-Encoded X.509 Certificate](storing-a-der-encoded-x-509-certificate.md)
- [Getting a Certificate](getting-a-certificate.md)
- [Storing an Identity in the Keychain](storing-an-identity-in-the-keychain.md)

#### Overview

A [`SecCertificate`](seccertificate.md) object for a certificate that is stored in a keychain can be safely cast to a [`SecKeychainItem`](seckeychainitem.md) for manipulation as a keychain item. On the other hand, if the [`SecCertificate`](seccertificate.md) is not stored in a keychain, casting the object to a [`SecKeychainItem`](seckeychainitem.md) and passing it to Keychain Services functions returns errors.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seccertificate)*