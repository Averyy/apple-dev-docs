# ManagedAppIdentitiesProvider

**Framework**: ManagedApp  
**Kind**: class

A class that provides identities that an MDM admin provisions for a managed app or extension.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- visionOS 2.4+

## Declaration

```swift
class ManagedAppIdentitiesProvider
```

## Mentions

- [Accessing provisioned secrets with identifiers](accessing-provisioned-secrets-with-identifiers.md)

#### Overview

Create an instance of this class when your app needs to access identities that the MDM admin provisions for your app from their MDM server.

## Topics

### Initializing an identities provider
- [init()](managedappidentitiesprovider/init.md)
  Initializes an identities provider.
### Identifying identities
- [var identifiers: some AsyncSequence<Array<String>, Never>](managedappidentitiesprovider/identifiers.md)
  An asynchronous sequence of arrays of identity identifiers provided by the MDM server.
### Accessing identities
- [func identity(withIdentifier: String) async throws(ManagedAppError) -> SecIdentity](managedappidentitiesprovider/identity(withidentifier:).md)
  Provides an identity by its identifier.

## See Also

- [Accessing provisioned secrets with identifiers](accessing-provisioned-secrets-with-identifiers.md)
  Specify the secrets your app requires for device management features, receive secrets from MDM servers and use secrets in your app.
- [class ManagedAppCertificatesProvider](managedappcertificatesprovider.md)
  A class that provides certificates that an MDM admin provisions for a managed app or extension.
- [class ManagedAppPasswordsProvider](managedapppasswordsprovider.md)
  A class that provides passwords that an MDM admin provisions for a managed app or extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedapp/managedappidentitiesprovider)*