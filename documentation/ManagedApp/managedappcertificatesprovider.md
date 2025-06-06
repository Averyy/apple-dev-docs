# ManagedAppCertificatesProvider

**Framework**: ManagedApp  
**Kind**: class

A class that provides certificates that an MDM admin provisions for a managed app or extension.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- visionOS 2.4+

## Declaration

```swift
class ManagedAppCertificatesProvider
```

## Mentions

- [Accessing provisioned secrets with identifiers](accessing-provisioned-secrets-with-identifiers.md)

#### Overview

Create an instance of this class when your app needs to access certificates that the MDM admin provisions for your app from their MDM server.

## Topics

### Initializing a certificates provider
- [init()](managedappcertificatesprovider/init.md)
  Initializes a managed app certificates provider.
### Identifying cerificates
- [var identifiers: some AsyncSequence<Array<String>, Never>](managedappcertificatesprovider/identifiers.md)
  An asynchronous sequence of arrays of certificate identifiers provided by the MDM server.
### Accessing certificates
- [func certificate(withIdentifier: String) async throws(ManagedAppError) -> SecCertificate](managedappcertificatesprovider/certificate(withidentifier:).md)
  Provides a certificate by its identifier.

## See Also

- [Accessing provisioned secrets with identifiers](accessing-provisioned-secrets-with-identifiers.md)
  Specify the secrets your app requires for device management features, receive secrets from MDM servers and use secrets in your app.
- [class ManagedAppIdentitiesProvider](managedappidentitiesprovider.md)
  A class that provides identities that an MDM admin provisions for a managed app or extension.
- [class ManagedAppPasswordsProvider](managedapppasswordsprovider.md)
  A class that provides passwords that an MDM admin provisions for a managed app or extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedapp/managedappcertificatesprovider)*