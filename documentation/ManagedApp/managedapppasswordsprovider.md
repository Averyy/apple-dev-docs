# ManagedAppPasswordsProvider

**Framework**: ManagedApp  
**Kind**: class

A class that provides passwords that an MDM admin provisions for a managed app or extension.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- visionOS 2.4+

## Declaration

```swift
class ManagedAppPasswordsProvider
```

## Mentions

- [Accessing provisioned secrets with identifiers](accessing-provisioned-secrets-with-identifiers.md)

#### Overview

Create an instance of this class when your app needs to access passwords that the MDM admin provisions for your app from their MDM server.

## Topics

### Initializing a passwords provider
- [init()](managedapppasswordsprovider/init.md)
  Initializes a passwords provider.
### Identifying passwords
- [var identifiers: some AsyncSequence<Array<String>, Never>](managedapppasswordsprovider/identifiers.md)
  An asynchronous sequence of arrays of password identifiers provided by the MDM server.
### Accessing passwords
- [func password(withIdentifier: String) async throws(ManagedAppError) -> String](managedapppasswordsprovider/password(withidentifier:).md)
  Provides a password by its identifier.

## See Also

- [Accessing provisioned secrets with identifiers](accessing-provisioned-secrets-with-identifiers.md)
  Specify the secrets your app requires for device management features, receive secrets from MDM servers and use secrets in your app.
- [class ManagedAppCertificatesProvider](managedappcertificatesprovider.md)
  A class that provides certificates that an MDM admin provisions for a managed app or extension.
- [class ManagedAppIdentitiesProvider](managedappidentitiesprovider.md)
  A class that provides identities that an MDM admin provisions for a managed app or extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedapp/managedapppasswordsprovider)*